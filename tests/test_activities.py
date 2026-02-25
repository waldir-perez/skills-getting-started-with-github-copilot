def test_list_activities(client):
    # Arrange
    # (El fixture client ya prepara la app)
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_participant(client):
    # Arrange
    email = "nuevo@mergington.edu"
    activity = "Chess Club"
    
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    
    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]


def test_signup_duplicate(client):
    # Arrange
    email = "michael@mergington.edu"  # Ya inscrito en Chess Club
    activity = "Chess Club"
    
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
