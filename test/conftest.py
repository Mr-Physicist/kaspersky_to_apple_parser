import pytest
from pathlib import Path
from typing import Dict

@pytest.fixture
def sample_website_entry() -> Dict[str, str]:
    return {
        "Website name": "example.com",
        "Website URL": "https://example.com",
        "Login": "user@example.com",
        "Password": "secretpass",
        "Comment": "Test account"
    }

@pytest.fixture
def sample_app_entry() -> Dict[str, str]:
    return {
        "Application": "TestApp",
        "Login": "testuser",
        "Password": "apppass123",
        "Comment": "App account"
    }

@pytest.fixture
def sample_text() -> str:
    return """Website name: example.com
Website URL: https://example.com
Login: user@example.com
Password: secretpass
Comment: Test account
---
Application: TestApp
Login: testuser
Password: apppass123
Comment: App account"""

@pytest.fixture
def temp_input_file(tmp_path: Path, sample_text: str) -> Path:
    input_file = tmp_path / "test_input.txt"
    input_file.write_text(sample_text)
    return input_file