import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0101_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x629
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        0,
        (
            TXT(0x00, '进入地下水路\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_EC'),
        (0x00000001, 'loc_F8'),
        (-1, 'loc_FE'),
    )

    def _loc_EC(): pass

    label('loc_EC')

    NewScene('ED6_DT21/C0500._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_FE')

    def _loc_F8(): pass

    label('loc_F8')

    TalkEnd(0x00FF)

    Jump('loc_FE')

    def _loc_FE(): pass

    label('loc_FE')

    Sleep(30)

    Return()

# id: 0x0001 offset: 0x104
@scena.Code('Init')
def Init():
    FadeOut(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 75350, 0, 18760, 270)
    SetChrPos(0x0001, 75350, 0, 18760, 270)
    SetChrPos(0x0002, 75350, 0, 18760, 270)
    SetChrPos(0x0003, 75350, 0, 18760, 270)
    OP_30(0x00)
    SetMapFlags(0x00000001)
    OP_69(0x0000, 0x00000000)
    FadeIn(1000, 0)
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0002 offset: 0x1AD
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6F(0x000D, 0)
    OP_6D(66130, 0, 55700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_020D')
    def lambda_020D():
        OP_6D(66730, 0, 50970, 5500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_020D)

    FadeIn(1000, 0)
    Sleep(1000)

    OP_70(0x000D, 0x0000003B)
    OP_73(0x000D)
    Sleep(400)

    CreateThread(0x0101, 0x00, 0x01, 0x0003)
    Sleep(1000)

    CreateThread(0x0103, 0x00, 0x01, 0x0004)
    Sleep(1000)

    CreateThread(0x00F8, 0x00, 0x01, 0x0005)
    Sleep(1000)

    CreateThread(0x00F9, 0x00, 0x01, 0x0006)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010461359V#1006F好了……\n',
            '完成一件工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461360V#022F赶快回到原来的工作中吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_331',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461361V#050F就是那个昏睡事件的调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461362V立即重新开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45A')

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_397',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461363V#072F嗯，是昏睡事件的调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461364V立刻重新开始打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45A')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461365V#030F嗯，是昏睡事件的调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461366V立刻重新开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45A')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45A',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461367V#042F嗯，是昏睡事件的调查吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461368V……重新开始打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45A(): pass

    label('loc_45A')

    ChrTalk(
        0x0101,
        (
            '#0010461369V#1002F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x0400)
    OP_28(0x0074, 0x01, 0x0800)
    OP_28(0x0074, 0x04, 0x10)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【搜寻迷路的猫咪】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x4DE
@scena.Code('func_03_4DE')
def func_03_4DE():
    SetChrPos(0x00FE, 66000, 500, 55500, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 66000, 0, 51400, 2000, 0x00)
    OP_8E(0x00FE, 66000, 0, 49000, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0004 offset: 0x524
@scena.Code('func_04_524')
def func_04_524():
    SetChrPos(0x00FE, 66000, 500, 55500, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 66000, 0, 51400, 2000, 0x00)
    OP_8E(0x00FE, 64849, 0, 50570, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0005 offset: 0x56A
@scena.Code('func_05_56A')
def func_05_56A():
    SetChrPos(0x00FE, 66000, 500, 55500, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 66000, 0, 51400, 2000, 0x00)
    OP_8E(0x00FE, 67170, 0, 50570, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x0006 offset: 0x5B0
@scena.Code('func_06_5B0')
def func_06_5B0():
    SetChrPos(0x00FE, 66000, 500, 55500, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 66000, 500, 53420, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    OP_72(0x000D, 0x0800)
    OP_70(0x000D, 0x00000000)
    OP_22(0x0007, 0x00, 0x64)
    OP_73(0x000D)
    OP_71(0x000D, 0x0800)
    Sleep(1000)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 66000, 0, 51400, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
