import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4137_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4137   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4137.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
            word_3A         = 0,
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
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65536,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65536,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65536,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572864,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572864,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572864,
            chipIndex           = 0,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '巴拉尔',
            x                   = 61020,
            z                   = 0,
            y                   = 2490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '科尼嘉',
            x                   = 65800,
            z                   = 100,
            y                   = -3410,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 60700,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = 61020,
            actorZ              = 1500,
            actorY              = 2490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1E7
@scena.Code('func_01_1E7')
def func_01_1E7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F8(): pass

    label('loc_1F8')

    Return()

# id: 0x0002 offset: 0x1F9
@scena.Code('func_02_1F9')
def func_02_1F9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_20E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_1F9')

    def _loc_20E(): pass

    label('loc_20E')

    Return()

# id: 0x0003 offset: 0x20F
@scena.Code('func_03_20F')
def func_03_20F():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x214
@scena.Code('func_04_214')
def func_04_214():
    TalkBegin(0x000E)
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
            TXT(0x02, '招牌菜『完熟咖喱饭』　900米拉\n'),
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
        'loc_290',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_290(): pass

    label('loc_290')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x384),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_365',
    )

    RemoveMira(900)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 1600)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 1600)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 1600)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 1600)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 1600)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 1600)
    ChrSetStatus(ChrTable['金'], 0xFD, 1600)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 1600)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_357',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x000B)"),
            Expr.Return,
        ),
        'loc_32D',
    )

    Jump('loc_357')

    def _loc_32D(): pass

    label('loc_32D')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '完熟咖喱饭',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_357(): pass

    label('loc_357')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_38B')

    def _loc_365(): pass

    label('loc_365')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_38B(): pass

    label('loc_38B')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000E)

    Return()

    def _loc_39A(): pass

    label('loc_39A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B4',
    )

    FadeIn(300, 0)
    TalkEnd(0x000E)

    Return()

    def _loc_3B4(): pass

    label('loc_3B4')

    FadeIn(300, 0)

    ChrTalk(
        0x000E,
        (
            '看起来挺慌张的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '今天不知为何\n',
            '想晚点再关门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你们慢慢坐，\n',
            '我完全不介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0005 offset: 0x41F
@scena.Code('func_05_41F')
def func_05_41F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这个时间有店开着\n',
            '对我来说真是再开心不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能好好看看\n',
            '新出的利贝尔通讯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
