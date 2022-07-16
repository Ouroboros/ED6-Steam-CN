import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '魔兽'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '魔兽'),
    TXT(0x08, '缇欧'),
    TXT(0x09, '维鲁'),
    TXT(0x0A, '查儿'),
    TXT(0x0B, '弗兰兹'),
    TXT(0x0C, '汉娜'),
    TXT(0x0D, '艾丝蒂尔'),
    TXT(0x0E, '牛'),
    TXT(0x0F, '牛'),
    TXT(0x10, '目标用摄像机'),
    TXT(0x11, '米尔西街道方向'),
    TXT(0x12, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0401.x'
    header.mapIndex       = 13
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x263D
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00005208,
            dword_04        = 0x00000000,
            dword_08        = 0x00005DC0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00005208,
            dword_04        = 0x00000000,
            dword_08        = 0x00005DC0,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 3000,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10100._CH', 'ED6_DT09/CH10100P._CP'),
        ('ED6_DT09/CH10101._CH', 'ED6_DT09/CH10101P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH01710._CH', 'ED6_DT07/CH01710P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
    ]

# id: 0x10002 offset: 0x146
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
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -75800,
            z                   = 0,
            y                   = 2400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1730,
            z                   = 0,
            y                   = 24300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1730,
            z                   = 0,
            y                   = 23000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -75800,
            z                   = 0,
            y                   = 2400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -75800,
            z                   = 0,
            y                   = 2400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 39010,
            z                   = 600,
            y                   = 23300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 40980,
            z                   = 600,
            y                   = 23300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 23910,
            z                   = 30,
            y                   = 66820,
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

# id: 0x10003 offset: 0x366
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x366
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 41200,
            y           = -500,
            z           = 21800,
            range       = 48300,
            dword_10    = 0x000003E8,
            dword_14    = 0x00004FB0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = 34900,
            y           = -1000,
            z           = 33900,
            range       = 43000,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000AD70,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 38700,
            y           = -500,
            z           = 37000,
            range       = 35200,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000B4DC,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 26000,
            y           = -500,
            z           = 26000,
            range       = 19000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00007148,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 42360,
            y           = -500,
            z           = 15300,
            range       = 50900,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000490C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 35830,
            y           = -1000,
            z           = 26140,
            range       = 34270,
            dword_10    = 0x000003E8,
            dword_14    = 0x00005D2A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 39000,
            y           = -500,
            z           = 42000,
            range       = 1000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = 22700,
            y           = -500,
            z           = 25300,
            range       = 1000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 46100,
            y           = -500,
            z           = 15200,
            range       = 1000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10005 offset: 0x486
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x486
@scena.Code('PreInit')
def PreInit():
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Return,
        ),
        'loc_4C7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 39000, 0, 42000, 270)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    def _loc_4C7(): pass

    label('loc_4C7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_4DB'),
        (0x00000066, 'loc_53A'),
        (0x00000067, 'loc_53A'),
        (-1, 'loc_551'),
    )

    def _loc_4DB(): pass

    label('loc_4DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 0, 0x230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52A',
    )

    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    CameraMove(28000, 0, 41000, 0)
    OP_6C(200000, 0)
    CameraSetDistance(5000, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    FadeIn(3000, 0)
    Event(0, 0x0006)

    Jump('loc_537')

    def _loc_52A(): pass

    label('loc_52A')

    FadeIn(3000, 0)
    Event(0, 0x0009)

    def _loc_537(): pass

    label('loc_537')

    Jump('loc_551')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 1, 0x231)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 2, 0x232)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54E',
    )

    Event(0, 0x000E)

    def _loc_54E(): pass

    label('loc_54E')

    Jump('loc_551')

    def _loc_551(): pass

    label('loc_551')

    Return()

# id: 0x0001 offset: 0x552
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x393),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_570',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_570(): pass

    label('loc_570')

    OP_16(0x02, 4000, -97000, -96000, 196612)
    OP_1B(0x04, 0x00, 0x0022)
    PlaySE(463, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x58D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5A2(): pass

    label('loc_5A2')

    Return()

# id: 0x0003 offset: 0x5A3
@scena.Code('func_03_5A3')
def func_03_5A3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5DD',
    )

    ChrJumpToRelative(0x00FE, -1000, 0, 0, 600, 1600)
    ChrJumpToRelative(0x00FE, 1000, 0, 0, 600, 1600)

    Jump('func_03_5A3')

    def _loc_5DD(): pass

    label('loc_5DD')

    Return()

# id: 0x0004 offset: 0x5DE
@scena.Code('func_04_5DE')
def func_04_5DE():
    PlaySE(400, 0x00, 0x64)

    Return()

# id: 0x0005 offset: 0x5E4
@scena.Code('func_05_5E4')
def func_05_5E4():
    PlaySE(401, 0x00, 0x64)

    Return()

# id: 0x0006 offset: 0x5EA
@scena.Code('func_06_5EA')
def func_06_5EA():
    EventBegin(0x00)
    Sleep(500)

    CreateThread(0x0000, 0x02, 0x00, 0x0008)
    CreateThread(0x0000, 0x01, 0x00, 0x0007)
    OP_6C(225000, 9000)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/T0411._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x61D
@scena.Code('func_07_61D')
def func_07_61D():
    Sleep(2000)

    CameraSetDistance(3000, 9000)

    Return()

# id: 0x0008 offset: 0x62C
@scena.Code('func_08_62C')
def func_08_62C():
    Sleep(2000)

    CameraMove(16700, 0, 18800, 9000)

    Return()

# id: 0x0009 offset: 0x643
@scena.Code('func_09_643')
def func_09_643():
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    CameraMove(26700, 0, 14500, 0)
    OP_6C(225000, 0)
    CameraSetDistance(3500, 0)
    SetChrPos(0x0101, 28000, 0, 14200, 90)
    SetChrPos(0x0102, 25350, 570, 15020, 90)
    EventBegin(0x00)
    CreateThread(0x0000, 0x01, 0x00, 0x000A)
    ChrWalkTo(0x0102, 28200, 0, 15400, 1500, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001453V#004F哇～天色已经这么暗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0001, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001454V#000F喂，约修亚。\n',
            '该怎么巡逻比较好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0001, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001455V#010F是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001456V#010F屋子周围、田地里、牲口棚\n',
            '和温室都要巡视一遍吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001457V#010F这样整个农场都能照顾到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001458V#006F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001459V#001F好的～我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    EventEnd(0x00)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x000A offset: 0x7EA
@scena.Code('func_0A_7EA')
def func_0A_7EA():
    CameraSetDistance(3000, 4500)

    Return()

# id: 0x000B offset: 0x7F4
@scena.Code('func_0B_7F4')
def func_0B_7F4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 1, 0x231)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CE',
    )

    SetScenaFlags(ScenaFlag(0x0046, 1, 0x231))
    OP_28(0x0002, 0x01, 0x0010)
    EventBegin(0x00)
    CameraMove(48090, 480, 19550, 3000)
    Fade(1000)
    SetChrPos(0x0101, 43760, 280, 21120, 135)
    SetChrPos(0x0102, 42420, 370, 21480, 135)
    CameraMove(43760, 280, 21120, 0)
    OP_6C(315000, 0)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010001466V#000F……魔兽好像也不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001467V#010F是啊，到别的地方看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_8CE(): pass

    label('loc_8CE')

    Return()

# id: 0x000C offset: 0x8CF
@scena.Code('func_0C_8CF')
def func_0C_8CF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 3, 0x233)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B63',
    )

    SetScenaFlags(ScenaFlag(0x0046, 3, 0x233))
    OP_28(0x0002, 0x01, 0x0040)
    EventBegin(0x00)
    CameraMove(39020, -300, 38660, 2000)
    Fade(1000)
    SetChrPos(0x0101, 42390, -40, 37580, 270)
    SetChrPos(0x0102, 42500, 30, 38900, 270)
    CameraMove(40310, -300, 38250, 0)
    OP_6C(135000, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001474V#000F#4P真安静啊～……\n',
            '只能听到虫子的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001475V#010F#4P看样子那些魔兽\n',
            '还没有进入菜园里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001476V#010F是因为我们在巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001477V#501F#4P对了，约修亚。\n',
            '你小时候有没有听过这种说法？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001478V#501F就是说，\n',
            '婴儿是从白菜地里长出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001479V#017F#4P又突然说这些了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001480V#010F我倒是听说过\n',
            '是长着银色翅膀的天使送过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001481V#501F#4P嗯……不同的地方说法也不同啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001482V#501F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001483V#010F#4P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001484V#010F我们继续巡逻吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001485V#000F#4P嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_B63(): pass

    label('loc_B63')

    Return()

# id: 0x000D offset: 0xB64
@scena.Code('func_0D_B64')
def func_0D_B64():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 1, 0x231)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 2, 0x232)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E1A',
    )

    SetScenaFlags(ScenaFlag(0x0046, 3, 0x233))
    SetScenaFlags(ScenaFlag(0x0046, 4, 0x234))
    OP_28(0x0002, 0x01, 0x0080)
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x0009, 24900, 50, 30180, 86)
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010001494V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, 35400, 350, 25540, 267)
    SetChrPos(0x0102, 35360, 340, 24500, 261)

    @scena.Lambda('lambda_0BF8')
    def lambda_0BF8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_0BF8')

    DispatchAsync2(0x0101, 0x0001, lambda_0BF8)

    @scena.Lambda('lambda_0C09')
    def lambda_0C09():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_0C09')

    DispatchAsync2(0x0102, 0x0001, lambda_0C09)

    OP_0D()

    @scena.Lambda('lambda_0C1B')
    def lambda_0C1B():
        CameraMove(34540, 80, 30070, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C1B)

    @scena.Lambda('lambda_0C33')
    def lambda_0C33():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C33)

    @scena.Lambda('lambda_0C43')
    def lambda_0C43():
        ChrWalkTo(0x0009, 34390, 70, 30090, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C43)

    WaitForThreadExit(0x0009, 0x0001)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0101, 200)
    Sleep(1000)

    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)
    PlaySE(404, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '咪呜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, 44900, 280, 36930, 12000, 0x00)
    SetChrPos(0x0009, 39000, 0, 42000, 270)

    ChrTalk(
        0x0101,
        (
            '#0010001496V#004F啊，逃跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrWalkTo(0x0101, 35270, 320, 28330, 5000, 0x00)
    SetChrDirection(0x0101, 45, 400)
    TerminateThread(0x0101, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010001497V#005F喂！给我等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 35220, 310, 26830, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001498V#012F气息还没有消失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001499V#012F那只魔兽应该还在菜园里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001500V#009F哼哼，正合我意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001501V#005F绝对要抓住它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(50)

    EventEnd(0x04)
    ClearMapFlags(0x00400000)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    def _loc_E1A(): pass

    label('loc_E1A')

    Return()

# id: 0x000E offset: 0xE1B
@scena.Code('func_0E_E1B')
def func_0E_E1B():
    SetScenaFlags(ScenaFlag(0x0046, 3, 0x233))
    SetScenaFlags(ScenaFlag(0x0046, 4, 0x234))
    OP_28(0x0002, 0x01, 0x0080)
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x0009, 24100, 0, 54800, 0)
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)
    ChrMoveToRelative(0x0101, 1000, 0, 0, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001486V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x0011)
    CreateThread(0x0102, 0x01, 0x00, 0x0011)
    CreateThread(0x0009, 0x01, 0x00, 0x000F)
    ChrWalkTo(0x0009, 23500, 0, 40000, 3000, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0101, 200)
    Sleep(1000)

    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)
    PlaySE(404, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '咪呜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x0010)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, 29000, 0, 29000, 12000, 0x00)
    SetChrPos(0x0009, 39000, 0, 42000, 270)

    ChrTalk(
        0x0101,
        (
            '#0010001488V#004F啊，逃跑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 21950, 0, 39160, 5000, 0x00)
    SetChrDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001489V#005F喂！给我等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001490V#012F气息还没有消失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001491V#012F那只魔兽应该还在菜园里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001492V#009F哼哼，正合我意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001493V#005F绝对要抓住它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    EventEnd(0x00)
    ClearMapFlags(0x00400000)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    Return()

# id: 0x000F offset: 0x1055
@scena.Code('func_0F_1055')
def func_0F_1055():
    CameraMove(24100, 0, 47800, 1000)
    CameraMove(23500, 0, 40000, 4000)

    Return()

# id: 0x0010 offset: 0x1078
@scena.Code('func_10_1078')
def func_10_1078():
    OP_69(0x0101, 1000)

    Return()

# id: 0x0011 offset: 0x1080
@scena.Code('func_11_1080')
def func_11_1080():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1094',
    )

    ChrTurnDirection(0x00FE, 0x0009, 0)
    Yield()

    Jump('func_11_1080')

    def _loc_1094(): pass

    label('loc_1094')

    Return()

# id: 0x0012 offset: 0x1095
@scena.Code('func_12_1095')
def func_12_1095():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10A8',
    )

    Call(0, 0x0015)
    Call(0, 0x001D)

    def _loc_10A8(): pass

    label('loc_10A8')

    Return()

# id: 0x0013 offset: 0x10A9
@scena.Code('func_13_10A9')
def func_13_10A9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10BC',
    )

    Call(0, 0x0015)
    Call(0, 0x001E)

    def _loc_10BC(): pass

    label('loc_10BC')

    Return()

# id: 0x0014 offset: 0x10BD
@scena.Code('func_14_10BD')
def func_14_10BD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10D0',
    )

    Call(0, 0x0015)
    Call(0, 0x001F)

    def _loc_10D0(): pass

    label('loc_10D0')

    Return()

# id: 0x0015 offset: 0x10D1
@scena.Code('func_15_10D1')
def func_15_10D1():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ChrTurnDirection(0x0000, 0x0009, 0)
    ChrTurnDirection(0x0001, 0x0009, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlaySE(404, 0x00, 0x64)
    TerminateThread(0x0009, 0xFF)
    ChrJumpToRelative(0x0009, 0, 0, 0, 800, 12000)
    ChrTurnDirection(0x0009, 0x0000, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001517V#006F太好了，终于抓住了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001518V#006F这次一定要给你们点颜色看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001519V#012F接下来才是动真格的。\n',
            '切记不可疏忽大意啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Battle(0x00000393, 0x00000000, 0x00, 0x0002, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_11D0'),
        (0x00000003, 'loc_11D5'),
        (0x00000000, 'loc_11D6'),
        (-1, 'loc_1DA3'),
    )

    def _loc_11D0(): pass

    label('loc_11D0')

    OP_B4(0x00)

    Jump('loc_1DA3')

    def _loc_11D5(): pass

    label('loc_11D5')

    Return()

    def _loc_11D6(): pass

    label('loc_11D6')

    EventBegin(0x00)
    FadeIn(2000, 0)
    ClearChrFlags(0x000A, 0x0008)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0008)
    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000C, 0x0008)
    ClearChrFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000D, 0x0008)
    ClearChrFlags(0x000D, 0x0080)
    CreateThread(0x000D, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000E, 0x0008)
    ClearChrFlags(0x000E, 0x0080)
    CreateThread(0x000E, 0x03, 0x00, 0x0002)
    SetChrPos(0x000C, 33150, 0, 16129, 225)
    SetChrPos(0x000D, 33390, 0, 15210, 270)
    SetChrPos(0x000E, 32990, 0, 14530, 315)
    SetChrPos(0x0012, 29700, 0, 16600, 0)
    SetChrPos(0x000F, 29000, 0, 14200, 0)
    SetChrPos(0x0010, 28100, 0, 15300, 0)
    SetChrPos(0x0013, 28300, 0, 16400, 0)
    SetChrPos(0x0011, 29300, 0, 17100, 0)
    SetChrPos(0x0101, 30920, 0, 15780, 270)
    SetChrPos(0x0102, 30630, 0, 14650, 315)
    ChrTurnDirection(0x000F, 0x000E, 0)
    ChrTurnDirection(0x0010, 0x000D, 0)
    ChrTurnDirection(0x0011, 0x000E, 0)
    ChrTurnDirection(0x0012, 0x0101, 0)
    ChrTurnDirection(0x0013, 0x0102, 0)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    CreateThread(0x0011, 0x03, 0x00, 0x0017)
    CameraMove(30470, 0, 16280, 0)
    OP_6C(315000, 0)
    CameraSetDistance(3000, 0)
    CameraSetDistance(2800, 3000)
    PlaySE(404, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '咪呜～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0010, 0x03, 0x00, 0x0016)
    PlaySE(404, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '咪～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001522V哎呀，真不愧是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001523V这么轻松就把\n',
            '这群敏捷的家伙抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001524V#000F#4P嘿嘿，过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001525V#000F话说回来，该怎么处理它们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        10,
        0,
        (
            TXT(0x00, '『应该不会再做坏事了吧……』\n'),
            TXT(0x01, '『……非要把它们杀掉不可吗？』\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_14B8'),
        (0x00000001, 'loc_1633'),
        (-1, 'loc_176E'),
    )

    def _loc_14B8(): pass

    label('loc_14B8')

    ChrTalk(
        0x0101,
        (
            '#0010001526V#000F#4P已经教训过它们了，\n',
            '应该不会再做坏事了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001527V#012F#3P艾丝蒂尔……\n',
            '你怎么能感情用事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001528V#012F我们不是为了打倒魔兽而来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001529V#003F#4P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001530V#015F#3P而且，我们这次是\n',
            '代替父亲来执行任务的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001531V#015F如果下次再出现同类的事件，\n',
            '你打算怎么向协会交代？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001532V#007F#4P唔唔……\n',
            '说的也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176E')

    def _loc_1633(): pass

    label('loc_1633')

    ChrTalk(
        0x0101,
        (
            '#0010001533V#003F#4P……非要把它们杀掉不可吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001534V#012F#3P这当然无庸置疑了，艾丝蒂尔。\n',
            '我们是为了打倒魔兽而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001535V#003F#4P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001536V#015F#3P游击士的使命\n',
            '是保卫百姓、维护正义……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001537V#015F绝对不能存有同情魔兽的心态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001538V#007F#4P唔唔……\n',
            '说的也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176E')

    def _loc_176E(): pass

    label('loc_176E')

    ChrTalk(
        0x000F,
        (
            '#0890001539V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0890001540V算了算了，\n',
            '反正受害的只有我们家种的菜而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0890001541V就放了它们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0900001542V是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0900001543V反正它们已经得到应有的教训，\n',
            '这件事就算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001544V#501F#4P缇欧，阿姨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0013, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001545V#012F#3P但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001546V……我也反对杀掉它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001547V它们虽然是魔兽，\n',
            '却也和我们生活在同一片土地上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001548V有时候还是要互相忍让的，\n',
            '大家和睦相处不是很好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001549V约修亚……\n',
            '这次就放了它们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001550V#015F#3P……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001551V#010F……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001552V#010F既然受害者都同意放过它们，\n',
            '那我也没有反对的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001553V真是抱歉，\n',
            '还让你们特地来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0910001554V我们以后也要加固栅栏，\n',
            '想办法避免再遇到这样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001555V#001F#4P那就这样决定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)
    ChrTurnDirection(0x0102, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001556V#006F就是这么回事，\n',
            '你们还不感谢大家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 31440, 0, 15780, 2000, 0x00)
    Sleep(100)

    SetChrFlags(0x0101, 0x0800)
    SetChrChipByIndex(0x0101, 10)
    PlaySE(500, 0x00, 0x64)
    OP_99(0x0101, 0x00, 0x0C, 2000)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0010, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010001557V#005F再有下次的话就送你们下地狱！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x000C, 0, 0, 0, 800, 12000)
    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x000D, 0, 0, 0, 800, 12000)
    ChrTurnDirection(0x000D, 0x0101, 0)
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x000E, 0, 0, 0, 800, 12000)
    ChrTurnDirection(0x000E, 0x0101, 0)
    PlaySE(404, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '咪嘎～～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetChrPos(0x000C, 0, 0, 0, 0)
    SetChrPos(0x0009, 33150, 0, 16129, 0)
    PlaySE(129, 0x00, 0x64)
    CreateThread(0x0009, 0x01, 0x00, 0x0018)
    Sleep(200)

    CreateThread(0x000B, 0x02, 0x00, 0x001B)
    SetChrPos(0x000D, 0, 0, 0, 0)
    SetChrPos(0x000A, 33390, 0, 15210, 0)
    PlaySE(129, 0x00, 0x64)
    CreateThread(0x000A, 0x01, 0x00, 0x0019)
    Sleep(200)

    SetChrPos(0x000E, 0, 0, 0, 0)
    SetChrPos(0x000B, 32990, 0, 14530, 0)
    PlaySE(129, 0x00, 0x64)
    CreateThread(0x000B, 0x01, 0x00, 0x001A)
    Sleep(1000)

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrTurnDirection(0x0101, 0x000B, 0)
    Sleep(2000)

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#0910001559V好了，终于解决了。\n',
            '已经这么晚了，都该睡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000F, 0x01, 0x00, 0x001C)
    CreateThread(0x0010, 0x01, 0x00, 0x001C)
    CreateThread(0x0011, 0x01, 0x00, 0x001C)
    CreateThread(0x0013, 0x01, 0x00, 0x001C)
    TerminateThread(0x0101, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0101, 0x0800)
    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0010, 400)
    ChrTurnDirection(0x0102, 0x0012, 400)

    ChrTalk(
        0x0012,
        (
            '#0910001560V你们也留下好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001561V#001F#4P好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001562V#010F#3P又给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 5, 0x235)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D68',
    )

    OP_2B(0x0002, 0x0002)

    Jump('loc_1D75')

    def _loc_1D68(): pass

    label('loc_1D68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 6, 0x236)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D75',
    )

    OP_2B(0x0002, 0x0001)

    def _loc_1D75(): pass

    label('loc_1D75')

    SetScenaFlags(ScenaFlag(0x0047, 1, 0x239))
    OP_28(0x0002, 0x01, 0x0800)
    OP_28(0x0002, 0x01, 0x1000)
    OP_28(0x0002, 0x04, 0x10)
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene('ED6_DT01/T0411._SN', 1, 0, 0)
    IdleLoop()

    def _loc_1DA3(): pass

    label('loc_1DA3')

    Return()

# id: 0x0016 offset: 0x1DA4
@scena.Code('func_16_1DA4')
def func_16_1DA4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DE7',
    )

    ChrJumpToRelative(0x00FE, 0, 0, 0, 400, 3000)
    Sleep(300)

    ChrJumpToRelative(0x00FE, 0, 0, 0, 400, 3000)
    Sleep(2500)

    Jump('func_16_1DA4')

    def _loc_1DE7(): pass

    label('loc_1DE7')

    Return()

# id: 0x0017 offset: 0x1DE8
@scena.Code('func_17_1DE8')
def func_17_1DE8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E57',
    )

    Sleep(3000)

    ChrMoveTo(0x00FE, 29500, 0, 17300, 300, 0x00)
    Sleep(2000)

    ChrMoveTo(0x00FE, 29300, 0, 17100, 1500, 0x00)
    Sleep(3000)

    ChrMoveTo(0x00FE, 29400, 0, 17200, 300, 0x00)
    Sleep(500)

    ChrMoveTo(0x00FE, 29300, 0, 17100, 700, 0x00)

    Jump('func_17_1DE8')

    def _loc_1E57(): pass

    label('loc_1E57')

    Return()

# id: 0x0018 offset: 0x1E58
@scena.Code('func_18_1E58')
def func_18_1E58():
    ChrWalkTo(0x0009, 34220, 50, 29710, 12000, 0x00)

    Return()

# id: 0x0019 offset: 0x1E6D
@scena.Code('func_19_1E6D')
def func_19_1E6D():
    ChrWalkTo(0x000A, 34220, 50, 29710, 12000, 0x00)

    Return()

# id: 0x001A offset: 0x1E82
@scena.Code('func_1A_1E82')
def func_1A_1E82():
    ChrWalkTo(0x000B, 34220, 50, 29710, 12000, 0x00)

    Return()

# id: 0x001B offset: 0x1E97
@scena.Code('func_1B_1E97')
def func_1B_1E97():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1ED3',
    )

    ChrTurnDirection(0x000F, 0x000A, 0)
    ChrTurnDirection(0x0010, 0x000A, 0)
    ChrTurnDirection(0x0011, 0x000A, 0)
    ChrTurnDirection(0x0012, 0x000A, 0)
    ChrTurnDirection(0x0013, 0x000A, 0)
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x0102, 0x000A, 0)
    Yield()

    Jump('func_1B_1E97')

    def _loc_1ED3(): pass

    label('loc_1ED3')

    Return()

# id: 0x001C offset: 0x1ED4
@scena.Code('func_1C_1ED4')
def func_1C_1ED4():
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001D offset: 0x1EDC
@scena.Code('func_1D_1EDC')
def func_1D_1EDC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F6D',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_69(0x0009, 500)
    CreateThread(0x0101, 0x01, 0x00, 0x0011)
    CreateThread(0x0102, 0x01, 0x00, 0x0011)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, 45500, 0, 45600, 12000, 0x00)
    ChrWalkTo(0x0009, 48000, 0, 51000, 12000, 0x00)
    SetChrPos(0x0009, 22700, 0, 25300, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Call(0, 0x0020)

    def _loc_1F6D(): pass

    label('loc_1F6D')

    Return()

# id: 0x001E offset: 0x1F6E
@scena.Code('func_1E_1F6E')
def func_1E_1F6E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FEB',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_69(0x0009, 500)
    CreateThread(0x0101, 0x01, 0x00, 0x0011)
    CreateThread(0x0102, 0x01, 0x00, 0x0011)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, 33900, 0, 15000, 12000, 0x00)
    SetChrPos(0x0009, 46100, 0, 15200, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Call(0, 0x0020)

    def _loc_1FEB(): pass

    label('loc_1FEB')

    Return()

# id: 0x001F offset: 0x1FEC
@scena.Code('func_1F_1FEC')
def func_1F_1FEC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_207D',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_69(0x0009, 500)
    CreateThread(0x0101, 0x01, 0x00, 0x0011)
    CreateThread(0x0102, 0x01, 0x00, 0x0011)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, 42200, 0, 10900, 12000, 0x00)
    ChrWalkTo(0x0009, 37500, 0, 10200, 12000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetChrPos(0x0009, 39000, 0, 42000, 270)
    Call(0, 0x0020)

    def _loc_207D(): pass

    label('loc_207D')

    Return()

# id: 0x0020 offset: 0x207E
@scena.Code('func_20_207E')
def func_20_207E():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_211F',
    )

    ChrTalk(
        0x0101,
        (
            '#0011350005V#000F啊啊。又逃走了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020990001V#010F这么小的家伙，\n',
            '逃跑起来动作也特别的灵活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好好想一下战斗的方法哦，艾丝蒂尔。（※仮）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_211F(): pass

    label('loc_211F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 6, 0x236)),
            Expr.Return,
        ),
        'loc_21A9',
    )

    SetScenaFlags(ScenaFlag(0x0046, 7, 0x237))
    OP_28(0x0002, 0x01, 0x0400)

    ChrTalk(
        0x0101,
        (
            '#0010001514V#007F啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001515V#012F真可惜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001516V#012F总之当它跳得起劲的时候\n',
            '从背后靠近它，然后再去抓它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_21A9(): pass

    label('loc_21A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 5, 0x235)),
            Expr.Return,
        ),
        'loc_23F1',
    )

    SetScenaFlags(ScenaFlag(0x0046, 6, 0x236))
    OP_28(0x0002, 0x01, 0x0200)

    ChrTalk(
        0x0101,
        (
            '#0010001505V#009F又、又逃走了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001506V#009F这家伙身子圆圆胖胖的，\n',
            '怎么动作还这么灵活啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0001, 0x0000, 0)

    ChrTalk(
        0x0102,
        (
            '#0020001507V#012F动作的确是很灵活，\n',
            '而且反应也相当灵敏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001508V#012F不过，掌握好时机就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0001, 500)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x0017,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Sub,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0017, 800)

    ChrTalk(
        0x0101,
        (
            '#0010001509V#004F掌握时机？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001510V#012F看得出这种魔兽跳起来的时候\n',
            '警戒性会相对减弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001511V#012F瞄准这个空档，然后从背后靠近它，\n',
            '这样就应该可以抓住它了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001512V#006F原来是这样啊……\n',
            '当它跳得起劲的时候从背后靠近它对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001513V#006F嗯，一定要试试看才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2465')

    def _loc_23F1(): pass

    label('loc_23F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Return,
        ),
        'loc_2465',
    )

    SetScenaFlags(ScenaFlag(0x0046, 5, 0x235))
    OP_28(0x0002, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#0010001502V#004F啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001503V#012F真可惜，被它发现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001504V#009F唔～下次一定抓到你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2465(): pass

    label('loc_2465')

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0009, 0xFF)
    EventEnd(0x01)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    Return()

# id: 0x0021 offset: 0x247B
@scena.Code('func_21_247B')
def func_21_247B():
    OP_69(0x0101, 1000)

    Return()

# id: 0x0022 offset: 0x2483
@scena.Code('func_22_2483')
def func_22_2483():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0046, 4, 0x234)),
            Expr.Return,
        ),
        'loc_2543',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24E9',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001463V#012F魔兽一定还在农场里面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001464V我们还是不要去别的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2540')

    def _loc_24E9(): pass

    label('loc_24E9')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001460V#012F魔兽一定还在农场里面某个地方。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001461V我们还是回去巡逻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2540(): pass

    label('loc_2540')

    Jump('loc_25DB')

    def _loc_2543(): pass

    label('loc_2543')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2593',
    )

    ChrTalk(
        0x0102,
        (
            '#0020001465V#012F这里是农场的出口……\n',
            '我们要在农场里面巡逻才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25DB')

    def _loc_2593(): pass

    label('loc_2593')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001462V#012F那里是农场的出口呢。\n',
            '我们要在农场里面巡逻才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25DB(): pass

    label('loc_25DB')

    ChrWalkTo(0x0000, 24100, 20, 53700, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
