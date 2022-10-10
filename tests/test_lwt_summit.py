
"""Test module for Mantium sentiment analysis application."""
from app import analyze_text

def test_clean_input():
    """Test clean_input function."""
    # Arrange
    input = "This is a  test.  \n"

    # Act
    result = analyze_text.clean_input(input)

    # Assert
    assert result == "This is a test."