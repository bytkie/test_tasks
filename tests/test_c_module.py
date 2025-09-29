import pytest
import string
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)


def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 2, 3]) == [1, 2, 3] 
    assert unique_sorted([]) == []  
    assert unique_sorted([5, 5, 5]) == [5] 

def test_count_words():
    text = "Tere  tere\nmaailm"
    expected = {"tere": 2, "maailm": 1}
    assert count_words(text) == expected  
    
    text_mixed = "Tere TERE, Maailm!"
    expected_mixed = {"tere": 2, "maailm": 1}
    assert count_words(text_mixed) == expected_mixed  

def test_merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    assert merge_dicts(d1, d2) == {"a": 1, "b": 3, "c": 4}  
    assert merge_dicts({}, d2) == d2
    assert merge_dicts(d1, {}) == d1

def test_find_max_pair():
    nums = [1, 3, 2, 3, 5, 3]
    assert find_max_pair(nums) == (5, 1)  
    with pytest.raises(ValueError):
        find_max_pair([])  

def test_flatten():
    assert flatten([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]  
    assert flatten([]) == [] 

def test_read_write_file(tmp_path):
    file_path = tmp_path / "testfile.txt"
    text = "Tere, maailm!"
    
    # Kirjutamine
    count = write_file(file_path, text)
    assert count == len(text)
    
    # Lugemine
    content = read_file(file_path)
    assert content == text

def test_safe_get():
    d = {"a": 1}
    assert safe_get(d, "a") == 1  
    assert safe_get(d, "b") is None  
    assert safe_get(d, "b", "default") == "default"  

def test_top_n():
    nums = [5, 2, 8, 3, 6]
    assert top_n(nums, 3) == [8, 6, 5]  
    
    with pytest.raises(ValueError):
        top_n(nums, 0)  # n <= 0
        
    with pytest.raises(ValueError):
        top_n(nums, -1)  # n <= 0
    
    with pytest.raises(ValueError):
        top_n(nums, 10)  # n suurem kui listi pikkus

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]  
    assert chunk_list([1, 2, 3], 3) == [[1, 2, 3]]  
    assert chunk_list([], 3) == []  
    
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], 0)  # size <= 0
    
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], -1)  # size <= 0
