import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5407_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5407   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '歼灭天使玲'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5407.x'
    header.mapIndex       = 1
    header.bgm            = 28
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4FF
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xD2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 3, 0x1C1B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E5',
    )

    Event(0, 0x0002)

    Jump('loc_E9')

    def _loc_E5(): pass

    label('loc_E5')

    Event(0, 0x0005)

    def _loc_E9(): pass

    label('loc_E9')

    Return()

# id: 0x0001 offset: 0xEA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_108',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_108(): pass

    label('loc_108')

    Return()

# id: 0x0002 offset: 0x109
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_6D(1570, 0, 1270, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x012F, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0008, 0x01, 0x00, 0x0003)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_22(0x009D, 0x00, 0x5A)
    Sleep(1000)

    SetMessageWindowPos(360, 60, -1, -1)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700330070V前往『圣堂』及『引擎室』\n',
            '的通路已经设置了限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700330071V请接受认证检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0008,
        (
            '#0220330072V#263F#6PＮｏ．ⅩⅤ──\n',
            '我是『歼灭天使』玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330073V现在要去『圣堂』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x009C, 0x00, 0x64)
    Sleep(500)

    SetChrName('声音')

    Talk(
        (
            '#3700330074V──认证完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    Call(0, 0x0006)
    Sleep(2000)

    OP_A2(0x10F4)
    NewScene('ED6_DT21/C5400._SN', 125, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2B5
@scena.Code('func_03_2B5')
def func_03_2B5():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, 340, 0, -1480, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_02DC')
    def lambda_02DC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_02DC)

    OP_8E(0x00FE, 520, 0, -70, 2000, 0x00)
    OP_8E(0x00FE, 1650, 0, -70, 2000, 0x00)

    Return()

# id: 0x0004 offset: 0x311
@scena.Code('func_04_311')
def func_04_311():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x00FE, -200, 0, -1500, 0)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0338')
    def lambda_0338():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0338)

    OP_8E(0x00FE, -200, 0, 710, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0005 offset: 0x360
@scena.Code('func_05_360')
def func_05_360():
    EventBegin(0x00)
    OP_6D(990, 0, 1420, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 1590, 0, -160, 90)
    SetChrPos(0x0001, 830, 0, 1050, 90)
    SetChrPos(0x0002, -790, 0, 1400, 90)
    SetChrPos(0x0003, -580, 0, -150, 90)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 1, 0x1C81)),
            Expr.Return,
        ),
        'loc_404',
    )

    Call(0, 0x0007)
    NewScene('ED6_DT21/C5400._SN', 127, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 2, 0x1C82)),
            Expr.Return,
        ),
        'loc_41B',
    )

    Call(0, 0x0006)
    NewScene('ED6_DT21/C5402._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 3, 0x1C83)),
            Expr.Return,
        ),
        'loc_432',
    )

    Call(0, 0x0007)
    NewScene('ED6_DT21/C5400._SN', 125, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_432(): pass

    label('loc_432')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 4, 0x1C84)),
            Expr.Return,
        ),
        'loc_449',
    )

    Call(0, 0x0006)
    NewScene('ED6_DT21/C5400._SN', 124, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 5, 0x1C85)),
            Expr.Return,
        ),
        'loc_460',
    )

    Call(0, 0x0007)
    NewScene('ED6_DT21/C5404._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_460(): pass

    label('loc_460')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 6, 0x1C86)),
            Expr.Return,
        ),
        'loc_477',
    )

    Call(0, 0x0006)
    NewScene('ED6_DT21/C5403._SN', 147, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0390, 7, 0x1C87)),
            Expr.Return,
        ),
        'loc_48E',
    )

    Call(0, 0x0007)
    NewScene('ED6_DT21/C5411._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_4A2')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0391, 0, 0x1C88)),
            Expr.Return,
        ),
        'loc_4A2',
    )

    Call(0, 0x0006)
    NewScene('ED6_DT21/C5404._SN', 153, 0, 0)
    IdleLoop()

    def _loc_4A2(): pass

    label('loc_4A2')

    Return()

# id: 0x0006 offset: 0x4A3
@scena.Code('func_06_4A3')
def func_06_4A3():
    FadeOut(2000, 0, -1)
    OP_22(0x0067, 0x00, 0x64)
    OP_6D(990, -12000, 1420, 2000)
    Sleep(2000)

    Return()

# id: 0x0007 offset: 0x4C9
@scena.Code('func_07_4C9')
def func_07_4C9():
    FadeOut(2000, 0, -1)
    OP_22(0x0067, 0x00, 0x64)
    OP_6D(990, 12000, 1420, 2000)
    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
