import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

def _menu_to_vector(menu):
    return [
        menu.kemanisan,
        menu.kepahitan,
        menu.keasaman,
        menu.body,
        menu.aroma,
        int(menu.susu),
        int(menu.suhu),
        menu.jenis,
        menu.kafein,
    ]

def _prefs_to_vector(prefs: dict):
    return [
        int(prefs['kemanisan']),
        int(prefs['kepahitan']),
        int(prefs['keasaman']),
        int(prefs['body']),
        int(prefs['aroma']),
        int(bool(prefs['susu'])),
        int(bool(prefs['suhu'])),
        int(prefs['jenis_kopi']),
        int(prefs['kafein']),
    ]

def get_recommendations(user_preferences: dict, k: int = 3):
    """
    Runs KNN with Euclidean distance + MinMaxScaler.
    Returns list of dicts: [{'menu': MenuKopi, 'similarity': float, 'distance': float}]
    """
    from recommendation.models import MenuKopi

    menus = list(MenuKopi.objects.all())

    if not menus:
        return []

    k = min(k, len(menus))

    # Build feature matrix
    X = np.array([_menu_to_vector(m) for m in menus], dtype=float)
    labels = list(range(len(menus)))

    # Scale features using MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Scale user input vector
    user_vec = np.array([_prefs_to_vector(user_preferences)], dtype=float)
    user_scaled = scaler.transform(user_vec)

    # Fit KNN
    knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn.fit(X_scaled, labels)

    # Get distances and indices
    distances, indices = knn.kneighbors(user_scaled, n_neighbors=k)

    # Max possible Euclidean distance in normalized space = sqrt(n_features)
    max_dist = float(np.sqrt(X_scaled.shape[1]))

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        similarity = max(0.0, (1.0 - dist / max_dist)) * 100
        results.append({
            'menu': menus[int(idx)],
            'similarity': round(similarity, 1),
            'distance': round(float(dist), 4),
        })

    return results
