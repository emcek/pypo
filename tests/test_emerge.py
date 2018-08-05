def test_convert2kibibytes():
    from pypo.emerge import convert2kib
    assert convert2kib('12 KiB') == 12
    assert convert2kib('34,567 KiB') == 34567
    assert convert2kib('31 MiB') == 31744
    assert convert2kib('23,34 MiB') == 2390016
    assert convert2kib('2 GiB') == 2097152
    assert convert2kib('1,23 GiB') == 128974848


def test_parse():
    from pypo.emerge import parse, EmergeRecord
    data = '[ebuild   R    ] media-libs/phonon-4.10.1::gentoo  USE="vlc -debug -designer -gstreamer -pulseaudio" 0 KiB\n' \
           '[ebuild   U    ] x11-libs/phonon-vlc-0.10.1::gentoo  USE="-debug" 0 KiB\n'
    er = parse(data)
    assert isinstance(er, list)
    assert isinstance(er[0], EmergeRecord)
    assert len(er) == 2
    assert er[1].action == 'U'
    assert er[1].category == 'x11-libs'
    assert er[1].package == 'phonon-vlc'
    assert er[1].version == '0.10.1'
    assert isinstance(er[0].flags, dict)
    assert er[1].flags['USE'] == '-debug'
    assert er[1].size == 0
