def test_convert2kibibytes():
    from emerge import convert2kibibytes
    assert convert2kibibytes('12 KiB') == 12
    assert convert2kibibytes('34,567 KiB') == 34567
    assert convert2kibibytes('31 MiB') == 31744
    assert convert2kibibytes('23,34 MiB') == 2390016
    assert convert2kibibytes('2 GiB') == 2097152
    assert convert2kibibytes('1,23 GiB') == 128974848
