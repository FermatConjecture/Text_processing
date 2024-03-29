import pytest
from processing import *

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    ('I used to like The Beatles', 'i use to like the beatl'),
    ('lets go dancing with the stars', 'let go danc with the star'),
    ('you are so funny', 'you are so funni'),
    ('I like to play the piano and the bongoes', 'i like to play the piano and the bongo'),
    ('my computer is broken', 'my comput is broken')
])
def test_stemming_lemmatization(input_text, expected_output):
    processed_text = stemming(lemmatization(input_text))
    assert processed_text == expected_output


