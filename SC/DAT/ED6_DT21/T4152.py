import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4152_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4152   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4152.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵达登',
            x                   = -89010,
            z                   = 250,
            y                   = -1030,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '比卡',
            x                   = -78290,
            z                   = 0,
            y                   = -2530,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -55400,
            z                   = 0,
            y                   = -3050,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = -78990,
            z                   = 1250,
            y                   = 8029,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -76250,
            z                   = -3500,
            y                   = -30490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·北街区',
            x                   = -39960,
            z                   = 0,
            y                   = 43920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·南街区',
            x                   = -7520,
            z                   = 300,
            y                   = -20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·码头',
            x                   = -117000,
            z                   = 0,
            y                   = -4090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -63040,
            y           = -3750,
            z           = -33480,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = -63390,
            y           = -3750,
            z           = -24940,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -78840,
            y           = 1250,
            z           = 12430,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10004 offset: 0x21A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -72220,
            triggerZ            = -3180,
            triggerY            = -15630,
            triggerRange        = 800,
            actorX              = -72220,
            actorZ              = -2000,
            actorY              = -15630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x23E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x23F
@scena.Code('func_01_23F')
def func_01_23F():
    OP_16(0x02, 4000, -185000, -131000, 2293853)
    OP_71(0x000F, 0x0004)
    OP_71(0x000C, 0x0010)
    OP_72(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_276',
    )

    OP_1B(0x03, 0x00, 0x000E)
    OP_1B(0x01, 0x00, 0x000F)

    def _loc_276(): pass

    label('loc_276')

    Return()

# id: 0x0002 offset: 0x277
@scena.Code('func_02_277')
def func_02_277():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_29A',
    )

    OP_8D(0x00FE, -83110, 1920, -74690, -5430, 3000)

    Jump('func_02_277')

    def _loc_29A(): pass

    label('loc_29A')

    Return()

# id: 0x0003 offset: 0x29B
@scena.Code('func_03_29B')
def func_03_29B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_31F',
    )

    ChrWalkTo(0x00FE, -39990, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55010, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -55910, 0, -3050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(1500)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1500)

    Jump('func_03_29B')

    def _loc_31F(): pass

    label('loc_31F')

    Return()

# id: 0x0004 offset: 0x320
@scena.Code('func_04_320')
def func_04_320():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrWalkTo(0x00FE, -76010, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -81900, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    ChrWalkTo(0x00FE, -78990, 1250, 8029, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1500)

    Jump('func_04_320')

    def _loc_3AC(): pass

    label('loc_3AC')

    Return()

# id: 0x0005 offset: 0x3AD
@scena.Code('func_05_3AD')
def func_05_3AD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这么晚了还去港口？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '千万小心脚下\n',
            '别滑进湖里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x3ED
@scena.Code('func_06_3ED')
def func_06_3ED():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这么晚了啊……\n',
            '回去时走夜路要小心才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x423
@scena.Code('func_07_423')
def func_07_423():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '刚才好像有白色的鸟\n',
            '飞去西边了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x451
@scena.Code('func_08_451')
def func_08_451():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '喂，那边的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚上出门倒不要紧，\n',
            '不过可得多加小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事就\n',
            '大声叫我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x4B8
@scena.Code('func_09_4B8')
def func_09_4B8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这么晚了有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有急事要坐船的话\n',
            '还是天亮的时候再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x506
@scena.Code('func_0A_506')
def func_0A_506():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>　　 売り家　　\n',
            '※飲食店営業も可',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x560
@scena.Code('func_0B_560')
def func_0B_560():
    OP_13(0x00B8)

    Return()

# id: 0x000C offset: 0x564
@scena.Code('func_0C_564')
def func_0C_564():
    OP_13(0x00B7)

    Return()

# id: 0x000D offset: 0x568
@scena.Code('func_0D_568')
def func_0D_568():
    OP_13(0x00AF)

    Return()

# id: 0x000E offset: 0x56C
@scena.Code('func_0E_56C')
def func_0E_56C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A2',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65B',
    )

    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270308V#1063F这里是……地下水路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270309V#1015F……不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270310V#1063F可能性很低吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270311V……去其他地方找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270312V#1002F明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_881')

    def _loc_65B(): pass

    label('loc_65B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_714',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270308V#1063F这里是……地下水路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270309V#1015F……不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270310V#1063F可能性很低吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270311V……去其他地方找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_881')

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7CD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270317V#0022F这里是……地下水路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270309V#1015F……不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270319V#0022F可能性很低啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270320V……去其他地方找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_881')

    def _loc_7CD(): pass

    label('loc_7CD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_881',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270321V#050F这里是……地下水路吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270309V#1015F……不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270323V#050F可能性很低啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270324V……去其他地方找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_881(): pass

    label('loc_881')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_A06')

    def _loc_8A2(): pass

    label('loc_8A2')

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270325V#1002F基库好像也没来……\n',
            '最好去其他地方找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EB')

    def _loc_8F4(): pass

    label('loc_8F4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_948',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270326V#1063F要确认的话这里是最后了。\n',
            '……先去其他地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EB')

    def _loc_948(): pass

    label('loc_948')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_99B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270327V#022F要确认的话这里是最后了。\n',
            '……先去其他地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9EB')

    def _loc_99B(): pass

    label('loc_99B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9EB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270328V#050F要确认的话这里是最后了。\n',
            '……先去其他地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EB(): pass

    label('loc_9EB')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_A06(): pass

    label('loc_A06')

    Jump('loc_B65')

    def _loc_A09(): pass

    label('loc_A09')

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B04',
    )

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270329V#1063F茶会的会场不在这里。\n',
            '……赶快去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A91',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270330V#1002F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AFE')

    def _loc_A91(): pass

    label('loc_A91')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ACA',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270331V#022F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AFE')

    def _loc_ACA(): pass

    label('loc_ACA')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AFE',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270332V#050F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AFE(): pass

    label('loc_AFE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_B4A')

    def _loc_B04(): pass

    label('loc_B04')

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270333V#1063F茶会的会场不在这里。\n',
            '……赶快去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_B4A(): pass

    label('loc_B4A')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_B65(): pass

    label('loc_B65')

    Return()

# id: 0x000F offset: 0xB66
@scena.Code('func_0F_B66')
def func_0F_B66():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C69',
    )

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270334V#1063F北街区之后再去也行吧。\n',
            '先得去这边找找。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF6',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270330V#1002F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C63')

    def _loc_BF6(): pass

    label('loc_BF6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C2F',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270331V#022F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C63')

    def _loc_C2F(): pass

    label('loc_C2F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C63',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270332V#050F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C63(): pass

    label('loc_C63')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_CAF')

    def _loc_C69(): pass

    label('loc_C69')

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270338V#1063F北街区之后再去也行吧。\n',
            '先得去这边找找。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_CAF(): pass

    label('loc_CAF')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_E29')

    def _loc_CCD(): pass

    label('loc_CCD')

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC8',
    )

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270339V#1063F茶会的会场不是这儿。\n',
            '……赶快去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D55',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270330V#1002F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC2')

    def _loc_D55(): pass

    label('loc_D55')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D8E',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270331V#022F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC2')

    def _loc_D8E(): pass

    label('loc_D8E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC2',
    )

    ChrTurnDirection(0x0000, 0x0109, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270332V#050F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC2(): pass

    label('loc_DC2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_E0E')

    def _loc_DC8(): pass

    label('loc_DC8')

    ChrTurnDirection(0x0109, 0x0000, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270343V#1063F茶会的会场不是这儿。\n',
            '……赶快去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_E0E(): pass

    label('loc_E0E')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    def _loc_E29(): pass

    label('loc_E29')

    Return()

# id: 0x0010 offset: 0xE2A
@scena.Code('func_10_E2A')
def func_10_E2A():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
