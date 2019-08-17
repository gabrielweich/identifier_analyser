from identifier_analyser.identifier_analyser import ocurrences, flatmap


def test_ocurrences():
    result = ocurrences(["gabriel", "manuel gabriel"])
    assert result["gabriel"] == ["1", "2"]
    assert result["manuel"] == ["2"]


def test_special_characters():
    result = ocurrences(["teste!", "teste@", "teste$"])
    assert result["teste"] == ["1", "2", "3"]


def test_spaces():
    result = ocurrences(["teste  ", "  teste", " teste "])
    assert result["teste"] == ["1", "2", "3"]


def test_dots():
    result = ocurrences(["teste.teste", "  tes.te", " .teste "])
    assert result["teste"] == ["1", "1", "3"]
    assert result["te"] == ["2"]
    assert result["tes"] == ["2"]


def test_flatmap():
    array = [[1, 2], [3, 4]]
    assert flatmap(array) == [1, 2, 3, 4]
