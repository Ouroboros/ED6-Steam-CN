import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4310.x'
    header.mapIndex       = 1
    header.bgm            = 89
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00510._CH', 'ED6_DT07/CH00510P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20143._CH', 'ED6_DT06/CH20143P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00514._CH', 'ED6_DT07/CH00514P._CP'),
        ('ED6_DT07/CH00513._CH', 'ED6_DT07/CH00513P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT06/CH20113._CH', 'ED6_DT06/CH20113P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH01790._CH', 'ED6_DT07/CH01790P._CP'),
        ('ED6_DT07/CH00500._CH', 'ED6_DT07/CH00500P._CP'),
        ('ED6_DT07/CH00501._CH', 'ED6_DT07/CH00501P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT07/CH00443._CH', 'ED6_DT07/CH00443P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT06/CH20115._CH', 'ED6_DT06/CH20115P._CP'),
    ]

# id: 0x10001 offset: 0x21A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 37,
            chipIndex           = 37,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '中队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉安妮',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛蒂娅公主',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡露娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '库拉茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '贵族老奶奶',
            x                   = 4420,
            z                   = 250,
            y                   = 72560,
            direction           = 201,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族中年男子',
            x                   = 5090,
            z                   = 0,
            y                   = 70990,
            direction           = 254,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族女孩',
            x                   = 3560,
            z                   = 250,
            y                   = 71090,
            direction           = 208,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族青年',
            x                   = -4630,
            z                   = 250,
            y                   = 72900,
            direction           = 165,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族中年女子',
            x                   = -3480,
            z                   = 250,
            y                   = 72300,
            direction           = 150,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族老人',
            x                   = -4870,
            z                   = 0,
            y                   = 70280,
            direction           = 162,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族小孩',
            x                   = 6280,
            z                   = 0,
            y                   = 66790,
            direction           = 237,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '男性学者２',
            x                   = 6740,
            z                   = 0,
            y                   = 65120,
            direction           = 257,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '管家',
            x                   = 8300,
            z                   = 0,
            y                   = 63060,
            direction           = 241,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '青年市民',
            x                   = 6540,
            z                   = 0,
            y                   = 69410,
            direction           = 239,
            word_0E             = 0,
            dword_10            = 35,
            chipIndex           = 35,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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

# id: 0x10002 offset: 0x63A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x63A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -57400,
            y           = 1000,
            z           = 2550,
            range       = -43640,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0xFFFFFCCC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x65A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x65A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_66D',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_72E)

    def _loc_66D(): pass

    label('loc_66D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_67B',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_08_441C)

    def _loc_67B(): pass

    label('loc_67B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_687'),
        (-1, 'loc_69D'),
    )

    def _loc_687(): pass

    label('loc_687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 1, 0x659)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 0, 0x658)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_69A',
    )

    SetScenaFlags(ScenaFlag(0x00CB, 1, 0x659))
    Event(0, func_06_13AC)

    def _loc_69A(): pass

    label('loc_69A')

    Jump('loc_69D')

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 4, 0x654)),
            Expr.Return,
        ),
        'loc_6F8',
    )

    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x0008, -48300, 0, 18410, 90)
    ChrSetPos(0x0009, -48500, 0, 17000, 135)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetChipByIndex(0x0008, 25)
    ChrSetChipByIndex(0x0009, 25)

    def _loc_6F8(): pass

    label('loc_6F8')

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x70A
@scena.Code('func_01_70A')
def func_01_70A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 1, 0x659)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_717',
    )

    OP_1B(0x00, 0x00, 0x0009)

    def _loc_717(): pass

    label('loc_717')

    Return()

# id: 0x0002 offset: 0x718
@scena.Code('func_02_718')
def func_02_718():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_718')

    def _loc_72D(): pass

    label('loc_72D')

    Return()

# id: 0x0003 offset: 0x72E
@scena.Code('func_03_72E')
def func_03_72E():
    EventBegin(0x00)
    CameraMove(19290, 0, 360, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(5020, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0108, 190, 0, -7530, 0)
    ChrSetPos(0x0101, -1330, 0, -8480, 0)
    ChrSetPos(0x0102, 570, 0, -8760, 0)
    FadeIn(1000, 0)
    CameraMove(640, 0, -4630, 4000)
    Fade(1000)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130592V#004F这里就是『艾尔贝离宫』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130593V唔～与城里相比，\n',
            '也是同样那么的典雅豪华啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130594V#010F啊，因为是王家的建筑嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, 11820, 0, -6220, 250)
    ChrSetPos(0x0009, 12550, 0, -5100, 250)
    ChrSetPos(0x000B, 14020, 0, -5780, 250)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0108, 100, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130595V#076F好的，冲进去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0924)

    @scena.Lambda('lambda_0932')
    def lambda_0932():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0932)

    @scena.Lambda('lambda_0940')
    def lambda_0940():
        CameraMove(6340, 0, -6950, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0940)

    @scena.Lambda('lambda_0958')
    def lambda_0958():
        OP_67(0, 4710, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0958)

    @scena.Lambda('lambda_0970')
    def lambda_0970():
        OP_6C(68000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0970)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#2620130596V你、你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -700, 0, -6920, 5000, 0x00)
    ChrWalkTo(0x0101, 790, 0, -6100, 5000, 0x00)
    ChrSetDirection(0x0101, 100, 0)

    ChrTalk(
        0x0101,
        (
            '#0010130597V#005F#5P你们这些坏人不配知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130598V#012F#5P不必多言，我们上！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A39')
    def lambda_0A39():
        CameraMove(10400, 0, -6130, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A39)

    @scena.Lambda('lambda_0A51')
    def lambda_0A51():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A51)

    Sleep(50)

    @scena.Lambda('lambda_0A6B')
    def lambda_0A6B():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A6B)

    Sleep(50)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0A85)

    ChrSetChipByIndex(0x0008, 7)
    ChrSetFlags(0x0008, 0x1000)

    @scena.Lambda('lambda_0AA4')
    def lambda_0AA4():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AA4)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 38)
    ChrSetFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_0AC8')
    def lambda_0AC8():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AC8)

    Sleep(50)

    ChrSetChipByIndex(0x000B, 38)
    ChrSetFlags(0x000B, 0x1000)

    @scena.Lambda('lambda_0AEC')
    def lambda_0AEC():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AEC)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x0008, 0x1000)
    ChrClearFlags(0x0009, 0x1000)
    ChrClearFlags(0x000B, 0x1000)
    Battle(0x000003AD, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_B4F'),
        (-1, 'loc_B52'),
    )

    def _loc_B4F(): pass

    label('loc_B4F')

    OP_B4(0x00)

    Return()

    def _loc_B52(): pass

    label('loc_B52')

    EventBegin(0x00)
    ChrSetChipByIndex(0x0008, 25)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetChipByIndex(0x000B, 25)
    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetSubChip(0x000B, 0)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetPos(0x0008, 11700, 0, -9160, 176)
    ChrSetPos(0x0009, 12780, 0, -10830, 90)
    ChrSetPos(0x000B, 10700, 0, -11180, 296)
    CameraMove(10320, 0, -5900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, 7960, 0, -6540, 90)
    ChrSetPos(0x0108, 9450, 0, -5900, 270)
    ChrSetPos(0x0102, 8270, 0, -5050, 90)
    FadeIn(1000, 0)
    CameraMove(8640, 0, -5700, 1500)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130599V#002F嗯，公主殿下他们被关在哪里呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130600V#012F肯定在这个巨大的建筑里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130601V我们要进行地毯式的调查才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130602V#072F如果再磨磨蹭蹭的话，\n',
            '前庭的那些家伙就会赶来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130603V尽快行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xD4C
@scena.Code('func_04_D4C')
def func_04_D4C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 4, 0x654)),
            Expr.Return,
        ),
        'loc_D54',
    )

    Return()

    def _loc_D54(): pass

    label('loc_D54')

    SetScenaFlags(ScenaFlag(0x00CA, 4, 0x654))
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, -52180, 0, 20500, 180)
    ChrSetPos(0x0009, -50170, 0, 20530, 180)
    ChrSetChipByIndex(0x0008, 39)
    ChrSetChipByIndex(0x0009, 39)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0DAC')
    def lambda_0DAC():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0DAC)

    @scena.Lambda('lambda_0DBA')
    def lambda_0DBA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DBA)

    @scena.Lambda('lambda_0DC8')
    def lambda_0DC8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DC8)

    CameraMove(-50570, 0, 17760, 2000)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0108, -50910, 0, 8080, 0)
    ChrSetPos(0x0102, -50140, 0, 6930, 0)
    ChrSetPos(0x0101, -52160, 0, 7020, 0)

    @scena.Lambda('lambda_0E29')
    def lambda_0E29():
        ChrWalkTo(0x00FE, -51000, 0, 12780, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0E29)

    @scena.Lambda('lambda_0E44')
    def lambda_0E44():
        ChrWalkTo(0x00FE, -51970, 0, 11510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E44)

    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        ChrWalkTo(0x00FE, -50210, 0, 11920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E5F)

    ChrTalk(
        0x0008,
        (
            '#2620130691V#5P你们是什么人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630130692V#5P好像在哪儿见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 40)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#2630130693V#5P是他们！\n',
            '武术大会取得优胜的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 40)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2620130694V#5P游击士那些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130695V#070F#2P啊，知道就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130696V#006F#2P老老实实让我们过去的话，\n',
            '或许还可以饶你们一命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620130697V#5P不、不要小看了我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630130698V#5P我们的防守坚如铁壁，\n',
            '能破得了就过来试试看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1037')
    def lambda_1037():
        CameraMove(-50570, 0, 20000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1037)

    ChrSetChipByIndex(0x0008, 41)

    @scena.Lambda('lambda_1054')
    def lambda_1054():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1054)

    Sleep(50)

    ChrSetChipByIndex(0x0008, 41)

    @scena.Lambda('lambda_1073')
    def lambda_1073():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1073)

    @scena.Lambda('lambda_1088')
    def lambda_1088():
        ChrWalkTo(0x00FE, -51080, 0, 39570, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1088)

    Sleep(50)

    @scena.Lambda('lambda_10A8')
    def lambda_10A8():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10A8)

    Sleep(50)

    @scena.Lambda('lambda_10C2')
    def lambda_10C2():
        OP_92(0x00FE, 0x0009, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10C2)

    Sleep(300)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x000003AE, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1103'),
        (-1, 'loc_1106'),
    )

    def _loc_1103(): pass

    label('loc_1103')

    OP_B4(0x00)

    Return()

    def _loc_1106(): pass

    label('loc_1106')

    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x0008, -48300, 0, 18410, 90)
    ChrSetPos(0x0009, -48500, 0, 17000, 135)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetChipByIndex(0x0008, 25)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, -50450, 0, 17110, 0)
    ChrSetPos(0x0108, -50450, 0, 17110, 0)
    ChrSetPos(0x0102, -50450, 0, 17110, 0)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0108,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0108, 0)
    CameraMove(-50450, 0, 17110, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x11E9
@scena.Code('func_05_11E9')
def func_05_11E9():
    MapSetFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_131C',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 5, 0x655))
    EventBegin(0x00)
    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    ChrTurnDirectionByPos(0x0001, -50950, 22020, 400)
    ChrTurnDirectionByPos(0x0002, -50950, 22020, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F唉～怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F真是相当坚固的锁呢……\n',
            '得先找到钥匙才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12DD',
    )

    ChrTalk(
        0x0108,
        (
            '#070F唔，\n',
            '那就只能暂时先到别的地方看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1317')

    def _loc_12DD(): pass

    label('loc_12DD')

    ChrTalk(
        0x0108,
        (
            '#0080130619V#070F唔，\n',
            '去问问那个年轻的管家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0008)

    def _loc_1317(): pass

    label('loc_1317')

    EventEnd(0x01)

    Jump('loc_13A6')

    def _loc_131C(): pass

    label('loc_131C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_136A',
    )

    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    SetScenaFlags(ScenaFlag(0x00CB, 0, 0x658))
    OP_71(0x0001, 0x0010)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用了备用钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_64(0x00, 0x0001)

    Jump('loc_13A6')

    def _loc_136A(): pass

    label('loc_136A')

    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_13A6(): pass

    label('loc_13A6')

    MapClearFlags(0x00000080)

    Return()

# id: 0x0006 offset: 0x13AC
@scena.Code('func_06_13AC')
def func_06_13AC():
    EventBegin(0x00)
    CameraMove(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(1760, 0)
    OP_6C(57000, 0)
    OP_6E(500, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0010, 50, 250, 68860, 180)
    ChrSetPos(0x000D, 6240, 0, 63940, 11)
    ChrSetPos(0x000F, 3070, 0, 58560, 0)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    ChrSetPos(0x0101, -110, 0, 50960, 0)
    ChrSetPos(0x0102, -110, 0, 50960, 0)
    ChrSetPos(0x0108, -110, 0, 50960, 0)
    ChrSetPos(0x000E, -110, 0, 50960, 0)
    ChrSetPos(0x0013, -110, 0, 50960, 0)
    ChrSetPos(0x0011, -110, 0, 50960, 0)
    ChrSetPos(0x0012, -110, 0, 50960, 0)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x0027, 0x0080)

    @scena.Lambda('lambda_150C')
    def lambda_150C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_150C')

    DispatchAsync2(0x000D, 0x0001, lambda_150C)

    @scena.Lambda('lambda_151D')
    def lambda_151D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_151D')

    DispatchAsync2(0x001E, 0x0001, lambda_151D)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_152E')

    DispatchAsync2(0x001F, 0x0001, lambda_152E)

    @scena.Lambda('lambda_153F')
    def lambda_153F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_153F')

    DispatchAsync2(0x0020, 0x0001, lambda_153F)

    @scena.Lambda('lambda_1550')
    def lambda_1550():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1550')

    DispatchAsync2(0x0021, 0x0001, lambda_1550)

    @scena.Lambda('lambda_1561')
    def lambda_1561():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1561')

    DispatchAsync2(0x0022, 0x0001, lambda_1561)

    @scena.Lambda('lambda_1572')
    def lambda_1572():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1572')

    DispatchAsync2(0x0023, 0x0001, lambda_1572)

    @scena.Lambda('lambda_1583')
    def lambda_1583():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1583')

    DispatchAsync2(0x0024, 0x0001, lambda_1583)

    @scena.Lambda('lambda_1594')
    def lambda_1594():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1594')

    DispatchAsync2(0x0025, 0x0001, lambda_1594)

    @scena.Lambda('lambda_15A5')
    def lambda_15A5():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_15A5')

    DispatchAsync2(0x0026, 0x0001, lambda_15A5)

    @scena.Lambda('lambda_15B6')
    def lambda_15B6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_15B6')

    DispatchAsync2(0x0027, 0x0001, lambda_15B6)

    OP_1F(0x50, 0x0000012C)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_15D6')
    def lambda_15D6():
        CameraMove(750, 0, 56890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_15D6)

    @scena.Lambda('lambda_15EE')
    def lambda_15EE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_15EE)

    @scena.Lambda('lambda_1600')
    def lambda_1600():
        ChrWalkTo(0x00FE, -60, 0, 57340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1600)

    Sleep(500)

    @scena.Lambda('lambda_1620')
    def lambda_1620():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1620)

    @scena.Lambda('lambda_1632')
    def lambda_1632():
        ChrWalkTo(0x00FE, 770, 0, 56300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1632)

    Sleep(500)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1669')
    def lambda_1669():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1669)

    @scena.Lambda('lambda_167B')
    def lambda_167B():
        ChrWalkTo(0x00FE, -950, 0, 55860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_167B)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_16A0')
    def lambda_16A0():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16A0)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_16B8')
    def lambda_16B8():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16B8)

    WaitForThreadExit(0x0108, 0x0001)
    ChrSetChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_16D0')
    def lambda_16D0():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_16D0)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_16E3')
    def lambda_16E3():
        CameraMove(2460, 0, 58180, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16E3)

    ChrTurnDirection(0x000F, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#0270130705V#143F你、你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130706V#006F呀呵～我们来救你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130707V#010F奈尔先生，\n',
            '看起来您安然无恙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0270130708V#144F来救我们的，真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '女孩的声音',
        (
            '#0060130709V艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '女孩的声音',
        (
            '#0060130710V没想到能在这里相会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_181E')
    def lambda_181E():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_181E)

    Sleep(100)

    @scena.Lambda('lambda_1831')
    def lambda_1831():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1831)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130711V#004F……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_186A')
    def lambda_186A():
        CameraMove(70, 250, 68760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_186A)

    @scena.Lambda('lambda_1882')
    def lambda_1882():
        OP_67(0, 4420, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1882)

    @scena.Lambda('lambda_189A')
    def lambda_189A():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_189A)

    Sleep(1500)

    @scena.Lambda('lambda_18AF')
    def lambda_18AF():
        ChrWalkTo(0x00FE, -540, 0, 66590, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18AF)

    Sleep(100)

    @scena.Lambda('lambda_18CF')
    def lambda_18CF():
        ChrWalkTo(0x00FE, 490, 0, 66590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_18CF)

    Sleep(300)

    @scena.Lambda('lambda_18EF')
    def lambda_18EF():
        ChrWalkTo(0x00FE, -2330, 0, 66150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_18EF)

    Sleep(100)

    @scena.Lambda('lambda_190F')
    def lambda_190F():
        ChrWalkTo(0x00FE, 2220, 0, 66920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_190F)

    @scena.Lambda('lambda_192A')
    def lambda_192A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_192A')

    DispatchAsync2(0x0101, 0x0000, lambda_192A)

    @scena.Lambda('lambda_193B')
    def lambda_193B():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_193B')

    DispatchAsync2(0x0102, 0x0000, lambda_193B)

    @scena.Lambda('lambda_194C')
    def lambda_194C():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_194C')

    DispatchAsync2(0x0108, 0x0001, lambda_194C)

    @scena.Lambda('lambda_195D')
    def lambda_195D():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_195D')

    DispatchAsync2(0x000F, 0x0001, lambda_195D)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010130712V#501F您、您就是公主殿下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130713V#001F初次见面。\n',
            '我们是游击士协会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '身着礼服的女孩',
        (
            '#0060130714V#406F不是初次见面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130715V#401F艾丝蒂尔、约修亚。\n',
            '终于按照约定再会了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130716V#505F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130717V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010130718V#004F#3S啊啊，你不是科洛丝吗！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛丝',
        (
            '#0060130719V#405F艾丝蒂尔你真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130720V虽然没有立刻察觉，\n',
            '但也不至于那么惊讶嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130721V#506F话、话虽这么说，\n',
            '可是身着礼服、长发披肩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130722V#501F究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130723V#017F……对不起呢，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130724V艾丝蒂尔这个人思想比较单纯。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130725V#509F我说！\n',
            '你那是什～么意思！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛丝',
        (
            '#0060130726V#466F呵呵……\n',
            '我认为那是艾丝蒂尔的一个优点哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130727V#401F对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130728V你还称呼我……那个名字啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130729V#010F嗯，我觉得你也是这么希望的吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130730V如果你介意的话，我还是称呼本名吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛丝',
        (
            '#0060130731V#408F怎么会呢……\n',
            '谢谢呢，我真的好开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130732V#505F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130733V话说回来……\n',
            '为什么科洛丝会在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130734V还有，公主殿下不是应该在这的吗？\n',
            '为什么到处都没有看见呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0270130735V#145F我说啊，不就在你的面前吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270130736V这位就是女王陛下的孙女，\n',
            '科洛蒂娅公主殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130737V#501F…………哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_20(0x000007D0)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x000D, 0x00)

    @scena.Lambda('lambda_1EC1')
    def lambda_1EC1():
        OP_67(0, 6000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EC1)

    OP_6C(45000, 1500)
    Sleep(500)

    OP_63(0x0101)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010130738V#005F#5S#2P啊啊啊啊啊啊？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    OP_6E(480, 0)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x000F, 0xFF)
    CloseMessageWindow()
    PlayBGM(17)

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130739V#466F对不起呢，我一直没说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130740V#405F我本来打算和艾丝蒂尔你们\n',
            '在王都再会的时候告诉你们的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130741V结果被理查德上校掳走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130742V#580F可、可是，为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130743V为什么公主殿下会隐藏身份\n',
            '在王立学院念书呢……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130744V而、而且我们称呼你科洛丝，\n',
            '这样可以吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130745V#406F以后也请一如既往地叫我科洛丝。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130746V科洛蒂娅·冯·奥赛雷丝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130747V#401F其实，我的全名的开始和末尾相结合\n',
            '就是我的爱称了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130748V#008F是这样的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130749V嗯，那么头发呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130750V#400F啊，这是假发。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130751V如果真的是这种发型，\n',
            '在学院里面读书就不太方便了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0270130752V#141F我也有够粗心的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270130753V虽然以前看过您的照片，\n',
            '但在市长官邸事件中见到您时\n',
            '竟然完全没有注意到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130754V#466F呵呵，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130755V杜南王叔和戴尔蒙市长都没有察觉，\n',
            '真是有些意外的效果呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130756V#007F哦，说起来，\n',
            '那个公爵还是你的亲戚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130757V#004F嗯，对了。\n',
            '最重要的事情反而忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们把至今为止的事情经过一一道来，\n',
            '也说明了接受女王的委托前来营救的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130758V#404F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130759V#403F艾丝蒂尔、约修亚，\n',
            '还有那位金先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130760V#406F你们能来营救我们，\n',
            '我发自内心地感谢你们的恩德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130761V#001F啊哈哈，怎么又客气起来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130762V如果知道被掳走的是科洛丝的话，\n',
            '就算不委托我们也会来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130763V#405F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130764V#019F的确如此呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130765V#010F不过，相比之下，\n',
            '我觉得你要感谢的应该是陛下才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130766V她不顾自己所处的不利境况，\n',
            '也要委托我们来营救你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130767V#074F的确，公主殿下既然已经平安无事，\n',
            '那么陛下就可以拒绝上校的要求了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130768V#072F也许陛下已经视死如归了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0108, 400)

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130769V#403F是的……\n',
            '祖母大人就是那样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130770V无论如何也不会妥协，\n',
            '可是这样祖母大人她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, -230, 0, 55310, 346)
    ChrSetChipByIndex(0x0008, 37)
    ChrSetFlags(0x0008, 0x0001)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000C, 1020, 0, 56140, 0)
    ChrSetPos(0x0008, 50, 0, 54770, 0)
    OP_20(0x000005DC)

    NpcTalk(
        0x000C,
        '男人的声音',
        (
            '#2680130771V#1P所谓闹剧，\n',
            '就是这个样子的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()

    @scena.Lambda('lambda_276F')
    def lambda_276F():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_276F)

    @scena.Lambda('lambda_277D')
    def lambda_277D():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_277D)

    @scena.Lambda('lambda_278B')
    def lambda_278B():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_278B)

    @scena.Lambda('lambda_2799')
    def lambda_2799():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2799)

    @scena.Lambda('lambda_27A7')
    def lambda_27A7():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_27A7)

    @scena.Lambda('lambda_27B5')
    def lambda_27B5():
        CameraMove(680, 0, 60840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_27B5)

    @scena.Lambda('lambda_27CD')
    def lambda_27CD():
        OP_6E(500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_27CD)

    Sleep(500)

    PlayBGM(86)
    Sleep(1500)

    ChrTalk(
        0x000D,
        (
            '#2340130772V#6P公、公主殿下～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130773V#407F小莉安妮！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2840')
    def lambda_2840():
        CameraMove(850, 0, 60760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2840)

    @scena.Lambda('lambda_2858')
    def lambda_2858():
        OP_6E(450, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2858)

    ChrSetChipByIndex(0x0101, 0)

    @scena.Lambda('lambda_286D')
    def lambda_286D():
        ChrWalkTo(0x00FE, -530, 0, 61260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_286D)

    Sleep(200)

    ChrSetChipByIndex(0x0102, 2)

    @scena.Lambda('lambda_2892')
    def lambda_2892():
        ChrWalkTo(0x00FE, 600, 0, 61850, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2892)

    Sleep(100)

    ChrSetChipByIndex(0x0108, 4)

    @scena.Lambda('lambda_28B7')
    def lambda_28B7():
        ChrWalkTo(0x00FE, -2220, 0, 61880, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_28B7)

    Sleep(200)

    @scena.Lambda('lambda_28D7')
    def lambda_28D7():
        ChrWalkTo(0x00FE, 10, 0, 63520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_28D7)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010130774V#580F那、那个小女孩是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0010, 0x0001)

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130775V#403F是摩尔根将军的孙女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130776V为了威逼被软禁在哈肯大门的将军就范，\n',
            '小莉安妮也被带到这里来了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130777V#012F为了要挟陛下而将公主殿下带到这里，\n',
            '你们对付所有掌权者都是用同一种手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130778V#2P你说得完全没错……\n',
            '不过，别以为这是单纯的威胁哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130779V#2P我们情报部的队员，为了理想，\n',
            '就算化成鬼、化成修罗也在所不惜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130780V#005F这、这种事还有脸自吹自擂！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130781V#402F中队长，我想和你做个交易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130782V请让我代替那个孩子，作为人质。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130783V#2P哦……\n',
            '我才不会上当呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130784V#2P对于我们这些人而言，\n',
            '是没有亲手杀死王族成员的勇气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130785V#2P与之相比，\n',
            '摩尔根将军的孙女就要好办得多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130786V#2P既有作为人质的价值，\n',
            '要打伤她又不会很难下手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130787V#407F……你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130788V#509F……无耻～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130789V#075F哎呀呀，无可救药的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130790V#2P哼，随便你们怎么胡说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130791V#2P到王都执勤的巡回部队\n',
            '很快就要从空中庭园归来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130792V#2P到时候会把亲卫队还有游击士\n',
            '在这儿一网打尽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '女性的声音',
        (
            '#0030130793V#1P啊～那已经不可能了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '女性的声音',
        (
            '#0030130794V#1P他们在来这里的途中\n',
            '就已经被我们全部消灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2E17')
    def lambda_2E17():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2E17)

    @scena.Lambda('lambda_2E25')
    def lambda_2E25():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E25)

    @scena.Lambda('lambda_2E33')
    def lambda_2E33():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2E33)

    @scena.Lambda('lambda_2E41')
    def lambda_2E41():
        CameraMove(500, 0, 59390, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E41)

    OP_6E(500, 800)

    @scena.Lambda('lambda_2E62')
    def lambda_2E62():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E62')

    DispatchAsync2(0x000C, 0x0001, lambda_2E62)

    @scena.Lambda('lambda_2E73')
    def lambda_2E73():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E73')

    DispatchAsync2(0x0008, 0x0001, lambda_2E73)

    @scena.Lambda('lambda_2E84')
    def lambda_2E84():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E84')

    DispatchAsync2(0x000D, 0x0001, lambda_2E84)

    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x000C, 0x0020)
    ChrSetFlags(0x0012, 0x0020)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0012, 16)
    ChrClearFlags(0x0012, 0x0080)
    PlayBGM(47)

    @scena.Lambda('lambda_2EBB')
    def lambda_2EBB():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2EBB')

    DispatchAsync2(0x0012, 0x0001, lambda_2EBB)

    ChrJumpTo(0x0012, -2140, 0, 54720, 1000, 8000)
    PlaySE(502, 0x00, 0x64)
    OP_99(0x0012, 0x02, 0x04, 3000)
    PlayEffect(0x08, 0xFF, 0x00FF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    ChrTurnDirection(0x0008, 0x0012, 0)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 43)

    @scena.Lambda('lambda_2F3D')
    def lambda_2F3D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000BB8, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2F3D)

    OP_99(0x0012, 0x04, 0x09, 3000)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#2620130795V#10A啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 42)
    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_2F8D')
    def lambda_2F8D():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2F8D)

    Sleep(500)

    @scena.Lambda('lambda_2FA2')
    def lambda_2FA2():
        ChrWalkTo(0x00FE, -2850, 0, 55570, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2FA2)

    Sleep(100)

    ChrMoveTo(0x000C, 1740, 0, 56010, 5000, 0x00)
    WaitForThreadExit(0x000D, 0x0001)
    ChrJumpTo(0x0012, -1960, 0, 55830, 500, 8000)
    ChrTurnDirection(0x000D, 0x0012, 400)
    Sleep(200)

    ChrTalk(
        0x000C,
        (
            '#2680130796V#2P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2340130797V#3P呜……呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000D,
        (
            '#2340130798V#3S#3P呜哇哇啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_3091')
    def lambda_3091():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_3091')

    DispatchAsync2(0x0101, 0x0001, lambda_3091)

    @scena.Lambda('lambda_30A2')
    def lambda_30A2():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_30A2')

    DispatchAsync2(0x0102, 0x0001, lambda_30A2)

    @scena.Lambda('lambda_30B3')
    def lambda_30B3():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_30B3')

    DispatchAsync2(0x0108, 0x0001, lambda_30B3)

    @scena.Lambda('lambda_30C4')
    def lambda_30C4():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_30C4')

    DispatchAsync2(0x000F, 0x0001, lambda_30C4)

    @scena.Lambda('lambda_30D5')
    def lambda_30D5():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_30D5')

    DispatchAsync2(0x0010, 0x0001, lambda_30D5)

    ChrTalk(
        0x0012,
        (
            '#0030130799V#021F#5P乖～乖～已经没事了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0012, 0xFF)
    ChrSetDirection(0x0012, 45, 400)

    ChrTalk(
        0x0012,
        (
            '#0030130800V#020F艾丝蒂尔、约修亚。\n',
            '真是好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130801V#004F雪、雪拉姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130802V#014F终于来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2680130803V#2P哪、哪里有这么\n',
            '慢条斯理的打招呼的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0013,
        '青年的声音',
        (
            '#0040130804V#1P哈·哈·哈。简直不解风情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp008_00.eff')
    ChrSetPos(0x0028, 1590, 1000, 54930, 0)
    PlayEffect(0x00, 0xFF, 0x0013, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x0028, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x08, 0xFF, 0x00FF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000C, 18)

    @scena.Lambda('lambda_32BF')
    def lambda_32BF():
        ChrJumpTo(0x00FE, 3030, 0, 57340, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_32BF)

    ChrTalk(
        0x000C,
        (
            '#2680130805V#10A呜哦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_3300')
    def lambda_3300():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_3300')

    DispatchAsync2(0x0012, 0x0001, lambda_3300)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0012, 90, 0)

    @scena.Lambda('lambda_3323')
    def lambda_3323():
        ChrJumpTo(0x00FE, 1090, 0, 56780, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3323)

    Sleep(200)

    PlaySE(502, 0x00, 0x64)
    OP_99(0x0012, 0x02, 0x04, 4000)
    PlayEffect(0x08, 0xFF, 0x00FF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x000C, 0x0004)

    @scena.Lambda('lambda_338E')
    def lambda_338E():
        CameraMove(6320, 0, 57730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_338E)

    @scena.Lambda('lambda_33A6')
    def lambda_33A6():
        ChrMoveTo(0x00FE, 9480, 500, 56550, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_33A6)

    OP_99(0x0012, 0x04, 0x09, 2000)
    WaitForThreadExit(0x000C, 0x0001)
    PlaySE(142, 0x00, 0x64)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000C, 17)

    ChrTalk(
        0x000C,
        (
            '#2680130806V#10A呜啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    PlayEffect(0x12, 0xFF, 0x000C, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    CameraSetDistance(1800, 0)
    CameraSetDistance(1760, 80)
    Sleep(500)

    ChrMoveTo(0x000C, 9490, 0, 56550, 1000, 0x00)
    PlaySE(524, 0x00, 0x64)
    OP_99(0x000C, 0x00, 0x03, 2000)

    ChrTalk(
        0x0012,
        (
            '#0030130807V#027F#5P刚才那是附赠品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(280, 0, 59100, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010130808V#509F好、好狠啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130809V#004F咦，刚才发起攻击的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130810V#014F……奥利维尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0012, 14)
    ChrTurnDirection(0x0012, 0x0013, 400)
    PlaySE(166, 0x00, 0x64)

    NpcTalk(
        0x0013,
        '青年的声音',
        (
            '#0040130811V#1PBingo⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3563')
    def lambda_3563():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3563')

    DispatchAsync2(0x0012, 0x0001, lambda_3563)

    @scena.Lambda('lambda_3574')
    def lambda_3574():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3574')

    DispatchAsync2(0x000D, 0x0001, lambda_3574)

    @scena.Lambda('lambda_3585')
    def lambda_3585():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3585')

    DispatchAsync2(0x0101, 0x0001, lambda_3585)

    @scena.Lambda('lambda_3596')
    def lambda_3596():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3596')

    DispatchAsync2(0x0102, 0x0001, lambda_3596)

    @scena.Lambda('lambda_35A7')
    def lambda_35A7():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_35A7')

    DispatchAsync2(0x0108, 0x0001, lambda_35A7)

    @scena.Lambda('lambda_35B8')
    def lambda_35B8():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_35B8')

    DispatchAsync2(0x000F, 0x0001, lambda_35B8)

    @scena.Lambda('lambda_35C9')
    def lambda_35C9():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_35C9')

    DispatchAsync2(0x0010, 0x0001, lambda_35C9)

    ChrClearFlags(0x0013, 0x0080)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_35EA')
    def lambda_35EA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_35EA)

    @scena.Lambda('lambda_35FC')
    def lambda_35FC():
        ChrWalkTo(0x00FE, 30, 0, 55280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_35FC)

    Sleep(100)

    CameraMove(550, 0, 58110, 2000)

    ChrTalk(
        0x0013,
        (
            '#0040130812V#031F哎呀呀。主角华丽登场了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_3664')
    def lambda_3664():
        ChrWalkTo(0x00FE, -1000, 0, 57140, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3664)

    Sleep(200)

    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_3689')
    def lambda_3689():
        ChrWalkTo(0x00FE, 240, 0, 58050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3689)

    Sleep(200)

    ChrSetChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_36AE')
    def lambda_36AE():
        ChrWalkTo(0x00FE, -2000, 0, 57950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_36AE)

    Sleep(300)

    @scena.Lambda('lambda_36CE')
    def lambda_36CE():
        ChrWalkTo(0x00FE, 120, 0, 59660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_36CE)

    Sleep(200)

    @scena.Lambda('lambda_36EE')
    def lambda_36EE():
        ChrWalkTo(0x00FE, 2470, 0, 59650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_36EE)

    TerminateThread(0x0012, 0xFF)
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(17)

    ChrTalk(
        0x0108,
        (
            '#0080130813V#071F哈哈哈……\n',
            '这不是那位怪腔怪调的兄弟吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130814V#070F对了，雪拉扎德，\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0012, 270, 400)

    ChrTalk(
        0x0012,
        (
            '#0030130815V#021F#2P你好，久疏问候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130816V#020F没想到金先生你也到利贝尔来了呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130817V听说你和艾丝蒂尔他们在一起时，\n',
            '我就没有那么担心了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130818V#070F哈哈，你真是太抬举我了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130819V#071F不过我说你啊……\n',
            '没见一段日子，越来越有魅力了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130820V说实话，我都有些认不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0030130821V#520F#2P哎、哎呀，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0012, 400)
    Sleep(200)

    ChrTurnDirection(0x0013, 0x0108, 400)
    Sleep(200)

    ChrTurnDirection(0x0013, 0x0012, 400)

    ChrTalk(
        0x0013,
        (
            '#0040130822V#032F哼·哼·哼，我好生嫉妒。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130823V#034F在把我尽情地享用完之后，\n',
            '又像垃圾一样抛弃了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0013, 400)

    ChrTalk(
        0x0012,
        (
            '#0030130824V#027F#2P哎哟，我说奥利维尔，\n',
            '你不是已经和爱娜她搭上了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130825V还想一脚踏两只船啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0102, 400)

    ChrTalk(
        0x0013,
        (
            '#0040130826V#034F哈·哈·哈，对不起～啦。\n',
            '人家～开玩笑的～啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130827V#506F还真是的……\n',
            '大家都还是老样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130828V#014F可是雪拉姐姐怎么来到王都的呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130829V王国军不是把关所全部封锁了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_3AF8')
    def lambda_3AF8():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AF8)

    ChrTurnDirection(0x0012, 0x0102, 400)

    ChrTalk(
        0x0012,
        (
            '#0030130830V#021F#2P嗯，所以我们是乘着小船\n',
            '从瓦雷利亚湖渡过来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130831V然后在王都的码头上岸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130832V#010F原来如此，真是深思熟虑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130833V#505F可是可是，你为什么又会\n',
            '和这个骗吃骗喝的大赖皮蛋在一起呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3BF9')
    def lambda_3BF9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3BF9)

    ChrTalk(
        0x0012,
        (
            '#0030130834V#025F#2P我刚踏出王都的协会就撞见他了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130835V他死皮赖脸地跟着我，甩都甩不掉，\n',
            '没办法之下，我就只有带他来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0040130836V#031F哈·哈·哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130837V如此有趣好玩的事情，\n',
            '怎能缺少了我这位天才演奏家的参与呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130838V#030F对了，那位小姐是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_3D2A')
    def lambda_3D2A():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3D2A)

    ChrWalkTo(0x0102, 940, 0, 58220, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0010, 400)
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130839V#006F啊，我给大家介绍一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130840V她是女王陛下的孙女科洛蒂娅公主殿下。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130841V是我和约修亚的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3DDE')
    def lambda_3DDE():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DDE)

    @scena.Lambda('lambda_3DEC')
    def lambda_3DEC():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3DEC)

    TerminateThread(0x0010, 0xFF)

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130842V#401F两位，初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130843V非常感谢你们两位刚才的协助。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0030130844V#021F#2P别客气，这也是游击士的义务嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0040130845V#035F哈·哈·哈。\n',
            '拯救美丽的公主是绅士的无上荣誉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130846V#030F能见到公主您，是我的光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0011, -110, 0, 50960, 0)
    ChrSetPos(0x000E, -110, 0, 50960, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)

    NpcTalk(
        0x0011,
        '女性的声音',
        (
            '#0100130847V#1P科洛丝，你没事吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3F77')
    def lambda_3F77():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3F77)

    @scena.Lambda('lambda_3F85')
    def lambda_3F85():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F85)

    @scena.Lambda('lambda_3F93')
    def lambda_3F93():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3F93)

    @scena.Lambda('lambda_3FA1')
    def lambda_3FA1():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3FA1)

    @scena.Lambda('lambda_3FAF')
    def lambda_3FAF():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3FAF)

    @scena.Lambda('lambda_3FBD')
    def lambda_3FBD():
        ChrMoveTo(0x00FE, 1190, 0, 55790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_3FBD)

    @scena.Lambda('lambda_3FD8')
    def lambda_3FD8():
        ChrMoveTo(0x00FE, -1720, 0, 57080, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3FD8)

    Sleep(500)

    @scena.Lambda('lambda_3FF8')
    def lambda_3FF8():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3FF8')

    DispatchAsync2(0x0101, 0x0001, lambda_3FF8)

    @scena.Lambda('lambda_4009')
    def lambda_4009():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_4009')

    DispatchAsync2(0x0102, 0x0001, lambda_4009)

    @scena.Lambda('lambda_401A')
    def lambda_401A():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_401A')

    DispatchAsync2(0x0108, 0x0001, lambda_401A)

    @scena.Lambda('lambda_402B')
    def lambda_402B():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_402B')

    DispatchAsync2(0x0013, 0x0001, lambda_402B)

    @scena.Lambda('lambda_403C')
    def lambda_403C():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_403C')

    DispatchAsync2(0x0012, 0x0001, lambda_403C)

    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x1000)
    ChrSetChipByIndex(0x0011, 44)

    @scena.Lambda('lambda_405C')
    def lambda_405C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_405C)

    @scena.Lambda('lambda_406E')
    def lambda_406E():
        ChrWalkTo(0x00FE, -350, 0, 57210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_406E)

    Sleep(500)

    PlaySE(140, 0x00, 0x64)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000E, 0x0004)

    @scena.Lambda('lambda_40A2')
    def lambda_40A2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_40A2)

    @scena.Lambda('lambda_40B4')
    def lambda_40B4():
        ChrWalkTo(0x00FE, 830, 0, 59590, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_40B4)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetChipByIndex(0x0011, 45)
    ChrSetSubChip(0x0011, 2)
    WaitForThreadExit(0x000E, 0x0001)
    CreateThread(0x000E, 0x01, 0x00, func_07_43F4)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130848V#409F尤莉亚，基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0440130849V啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A5(0x0000)
    OP_97(0x000E, 130, 59590, -90000, 5000, 0x0001)
    OP_97(0x000E, 130, 59590, -90000, 3000, 0x0001)
    ChrSetFlags(0x000E, 0x0020)

    @scena.Lambda('lambda_416A')
    def lambda_416A():
        OP_99(0x00FE, 0x00, 0x07, 5000)
        Yield()

        Jump('lambda_416A')

    DispatchAsync2(0x000E, 0x0002, lambda_416A)

    @scena.Lambda('lambda_417D')
    def lambda_417D():
        ChrMoveTo(0x00FE, -730, 600, 57540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_417D)

    ChrSetDirection(0x000E, 45, 100)
    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_41A4')
    def lambda_41A4():
        ChrMoveTo(0x00FE, -730, 0, 57540, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_41A4)

    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x000E, 0x02)
    Fade(500)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0011, 0x0020)
    ChrSetChipByIndex(0x0011, 36)
    ChrSetSubChip(0x0011, 1)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0440130850V#311F#5P啾啾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440130851V啾——啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130852V#408F呵呵，太好了。\n',
            '你们也平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130853V#171F#2P殿下，您平安无事就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130854V真的……真的太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '科洛蒂娅公主',
        (
            '#0060130855V#401F尤莉亚你也是……\n',
            '还是那么精神焕发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，艾丝蒂尔他们带着科洛丝\n',
            '和伪装行动的游击士还有亲卫队队员汇合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '安顿好其他的人质之后，\n',
            '众人决定一起商讨对策以确认当前的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1B(0x00, 0x00, 0xFFFF)
    OP_28(0x004B, 0x04, 0x10)
    OP_28(0x004C, 0x04, 0x10)
    OP_28(0x004C, 0x01, 0x0040)
    OP_28(0x004C, 0x01, 0x0080)
    OP_28(0x004C, 0x01, 0x0100)
    OP_28(0x004D, 0x04, 0x02)
    OP_28(0x004D, 0x04, 0x04)
    OP_28(0x004D, 0x01, 0x0001)
    OP_28(0x004D, 0x01, 0x0002)
    OP_20(0x000005DC)
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x43F4
@scena.Code('func_07_43F4')
def func_07_43F4():
    OP_A6(0x0000)
    def _loc_43F7(): pass

    label('loc_43F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4418',
    )

    OP_97(0x00FE, 130, 59590, -360000, 5000, 0x0001)
    Yield()

    Jump('loc_43F7')

    def _loc_4418(): pass

    label('loc_4418')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0008 offset: 0x441C
@scena.Code('func_08_441C')
def func_08_441C():
    EventBegin(0x00)
    CameraMove(1040, 130, 67720, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x0011, -40, 250, 70880, 180)
    ChrSetPos(0x0102, -2410, 0, 67020, 45)
    ChrSetPos(0x0013, -3610, 0, 67070, 61)
    ChrSetPos(0x0108, -3890, 0, 68290, 80)
    ChrSetPos(0x0101, 2540, 0, 67490, 320)
    ChrSetPos(0x0010, 1280, 0, 67070, 2)
    ChrSetPos(0x0012, 2980, 0, 66110, 297)
    ChrSetPos(0x0014, -730, 0, 65269, 0)
    ChrSetPos(0x0016, 180, 0, 64510, 0)
    ChrSetPos(0x0015, -950, 0, 63940, 0)
    ChrSetPos(0x0017, -2170, 0, 64410, 0)
    ChrSetPos(0x0018, -1770, 0, 61620, 0)
    ChrSetPos(0x0018, 70, 0, 61620, 0)
    ChrSetPos(0x0018, 1840, 0, 61620, 0)
    ChrSetPos(0x0018, -1770, 0, 59790, 0)
    ChrSetPos(0x0018, 70, 0, 59790, 0)
    ChrSetPos(0x0018, 1840, 0, 59790, 0)
    ChrSetChipByIndex(0x0010, 24)

    ChrTalk(
        0x0011,
        (
            '#0101060016V#170F现在我就对解放格兰赛尔城\n',
            '和营救女王陛下的作战进行说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '首先，由约修亚君等\n',
            '三人为一组从地下水路\n',
            '攻入格兰赛尔城的地下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060017V然后迅速赶往亲卫队值勤室\n',
            '将城门的开关装置启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130946V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130947V#070F嗯，巨大的烟花\n',
            '就要开始燃放了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#030F哼哼……不管怎样，\n',
            '最后一幕终于开演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0101060018V#170F在城门打开的同时，\n',
            '全体亲卫队员以及四名\n',
            '游击士就从市街区冲进城内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060019V尽量制造草木皆兵的效果，\n',
            '将敌人全部引入城内集中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '好的，交给我们去办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '太好了，我已经跃跃欲试了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#170F最后还要说的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……殿下，您真的\n',
            '下决心要参战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#040F抱歉……\n',
            '我一定要救出祖母大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，\n',
            '我还会操纵飞行艇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060940016V没有不让我\n',
            '参战的道理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F唉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130959V如果早知道会发生这样的事情，\n',
            '当初就不会教你操纵飞艇的方法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不用担心啦，尤莉亚中尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130961V科洛丝就交给\n',
            '我们来照顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#020F我以『银闪』之名作为赌注，\n',
            '发誓一定会保护公主的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F我知道了……拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060020V在将敌人的兵力集中于城内之后，\n',
            '艾丝蒂尔等三人为一组就乘坐\n',
            '特务飞行艇在空中庭园强行着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130965V然后就冲入女王宫\n',
            '救出艾莉茜雅女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 180, 400)

    ChrTalk(
        0x0011,
        (
            '#170F正午钟响的同时开始作战——\n',
            '在此之前请在各自的地点等候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060021V……全体听命，行动开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x4AFC
@scena.Code('func_09_4AFC')
def func_09_4AFC():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B69',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130699V#002F还没有完成女王陛下的委托呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130700V快点把公主殿下找出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C48')

    def _loc_4B69(): pass

    label('loc_4B69')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BDD',
    )

    ChrTalk(
        0x0102,
        (
            '#0020130701V#012F等把人质都解放了，\n',
            '再离开这里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130702V总之要先把里面彻底调查一番。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C48')

    def _loc_4BDD(): pass

    label('loc_4BDD')

    ChrTalk(
        0x0108,
        (
            '#0080130703V#072F还没有找到公主殿下和其他人质呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130704V先把那些坏家伙们\n',
            '一个不留地干掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C48(): pass

    label('loc_4C48')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
