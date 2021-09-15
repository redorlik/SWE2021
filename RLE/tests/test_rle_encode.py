from ..rle import encode,decode
from hypothesis import given,settings
from hypothesis.strategies import text
import hypothesis.strategies as st

def test_encode():
    #RLE eler runlength encoding tæller antallet af symboler og 
    #erstater et antal ens symboler med symbolet og længde
    #
    # 'tttteeeee' erstates 't',4 'e',5

    result = encode('tttteeeee')
    assert result == [('t',4),('e',5)]

def test_empty():
    assert encode('') == [('',0)]

def test_space():
    assert encode(' '*10) == [(' ',10)]
    assert encode('          \\\\') == [(' ',10),('\\',2)]
    assert encode(r'          \\\\') == [(' ',10),('\\',4)]
    assert encode('          ----') == [(' ',10),('-',4)]
    assert encode('111111----') == [('1',6),('-',4)]

def test_unicode():
    assert encode('😇😇😇😇😇') == [('😇',5)]
def test_unicode2():
    assert encode('😇😇😇😇😇👍') == [('😇',5),('👍',1)]
def test_unicode3():
    assert encode('😇😇😇😇😇👍👍👍👍👍👍👍') == [('😇',5),('👍',7)]

def test_decode():
    assert decode([('h',3),('k',5)]) == 'h'*3+'k'*5
    assert decode([('1',3),('3',5)]) == '1'*3+'3'*5

def test_decode_encode():
    s = 'sssssssskkkkk1111   99999😇😇😇😇😇👍👍👍👍👍👍👍'
    assert s == decode(encode(s))
def test_decode_encode2():
    s = 'sssssssskkkkk1111   99999😇😇😇😇😇👍👍👍👍👍👍👍'*1_000
    assert s == decode(encode(s))
def test_decode_encode3():
    s = ''
    assert s == decode(encode(s))

@given(text())
#@settings(max_examples=1_000_000)
def test_invariant(input):
    print(input)
    assert input == decode(encode(input))



@given(st.lists(st.tuples(st.text(min_size=1,max_size=1),st.integers())))
#@settings(max_examples=1_000_000)
def test_invariant2(input):
    print(input)
    assert input == encode(decode(input))