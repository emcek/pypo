def test_convert2kibibytes():
    from pypo.emerge import convert2kib
    assert convert2kib('12 KiB') == 12
    assert convert2kib('34,567 KiB') == 34567
    assert convert2kib('31 MiB') == 31744
    assert convert2kib('23,34 MiB') == 2390016
    assert convert2kib('2 GiB') == 2097152
    assert convert2kib('1,23 GiB') == 128974848
