import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1410   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1410.x'
    header.mapIndex       = 62
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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
            word_3A         = 62,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '维姆拉',
            x                   = 3200,
            z                   = 0,
            y                   = 33900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3930,
            triggerZ            = 0,
            triggerY            = 39420,
            triggerRange        = 800,
            actorX              = 5010,
            actorZ              = 1500,
            actorY              = 39620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('func_01_F7')
def func_01_F7():
    Return()

# id: 0x0002 offset: 0xF8
@scena.Code('func_02_F8')
def func_02_F8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_F8')

    def _loc_10D(): pass

    label('loc_10D')

    Return()

# id: 0x0003 offset: 0x10E
@scena.Code('func_03_10E')
def func_03_10E():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_321',
    )

    FadeOut(300, 0, 100)

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
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '吃饭\n'),
            TXT(0x03, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_178',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x6F)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FE',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_213',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x19),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1D2',
    )

    ChrSetStatus(0x0003, 0x02, 1)
    ChrSetStatus(0x0003, 0x05, 100)

    Jump('loc_210')

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1EC',
    )

    ChrSetStatus(0x0002, 0x02, 1)
    ChrSetStatus(0x0002, 0x05, 100)

    Jump('loc_210')

    def _loc_1EC(): pass

    label('loc_1EC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_206',
    )

    ChrSetStatus(0x0000, 0x02, 1)
    ChrSetStatus(0x0000, 0x05, 100)

    Jump('loc_210')

    def _loc_206(): pass

    label('loc_206')

    ChrSetStatus(0x0001, 0x02, 1)
    ChrSetStatus(0x0001, 0x05, 100)

    def _loc_210(): pass

    label('loc_210')

    Jump('loc_286')

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_262',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x21),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_23B',
    )

    ChrSetStatus(0x0002, 0x02, 1)
    ChrSetStatus(0x0002, 0x05, 100)

    Jump('loc_25F')

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x42),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_255',
    )

    ChrSetStatus(0x0000, 0x02, 1)
    ChrSetStatus(0x0000, 0x05, 100)

    Jump('loc_25F')

    def _loc_255(): pass

    label('loc_255')

    ChrSetStatus(0x0001, 0x02, 1)
    ChrSetStatus(0x0001, 0x05, 100)

    def _loc_25F(): pass

    label('loc_25F')

    Jump('loc_286')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_27C',
    )

    ChrSetStatus(0x0000, 0x02, 1)
    ChrSetStatus(0x0000, 0x05, 100)

    Jump('loc_286')

    def _loc_27C(): pass

    label('loc_27C')

    ChrSetStatus(0x0001, 0x02, 1)
    ChrSetStatus(0x0001, 0x05, 100)

    def _loc_286(): pass

    label('loc_286')

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '地狱极乐锅',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E4',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0008)"),
            Expr.Return,
        ),
        'loc_2BC',
    )

    Jump('loc_2E4')

    def _loc_2BC(): pass

    label('loc_2BC')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '地狱极乐锅',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E4(): pass

    label('loc_2E4')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_2FE(): pass

    label('loc_2FE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_318',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_318(): pass

    label('loc_318')

    FadeIn(300, 0)

    def _loc_321(): pass

    label('loc_321')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '竟然能来到这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看起来你们是游击士，\n',
            '是因为工作来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里没什么东西招待你们，\n',
            '就请随意休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DB')

    def _loc_3B2(): pass

    label('loc_3B2')

    ChrTalk(
        0x0008,
        (
            '如果有需要的话，\n',
            '床也可以借你们用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DB(): pass

    label('loc_3DB')

    Jump('loc_51B')

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_490',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '真让我吃惊呢，竟然有客人来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看起来好像不是登山者……\n',
            '你们好像很累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在这里休息一下怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这个小屋里\n',
            '要是有你们需要的东西，\n',
            '就请随便用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51B')

    def _loc_490(): pass

    label('loc_490')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_51B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '竟然能来到这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里没什么东西招待你们，\n',
            '请随意休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51B')

    def _loc_4F2(): pass

    label('loc_4F2')

    ChrTalk(
        0x0008,
        (
            '如果有需要的话，\n',
            '床也可以借你们用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51B(): pass

    label('loc_51B')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x51F
@scena.Code('func_04_51F')
def func_04_51F():
    FadeOut(300, 0, 100)

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
        100,
        1,
        (
            TXT(0x00, '休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B8',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5D2',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_5D2(): pass

    label('loc_5D2')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
