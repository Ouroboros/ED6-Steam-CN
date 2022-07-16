import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特务兵'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '中队长'),
    TXT(0x06, '莉安妮'),
    TXT(0x07, '基库'),
    TXT(0x08, '奈尔'),
    TXT(0x09, '科洛蒂娅公主'),
    TXT(0x0A, '尤莉亚中尉'),
    TXT(0x0B, '雪拉扎德'),
    TXT(0x0C, '奥利维尔'),
    TXT(0x0D, '卡露娜'),
    TXT(0x0E, '亚妮拉丝'),
    TXT(0x0F, '库拉茨'),
    TXT(0x10, '克鲁茨'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '亲卫队员'),
    TXT(0x16, '亲卫队员'),
    TXT(0x17, '贵族老奶奶'),
    TXT(0x18, '贵族中年男子'),
    TXT(0x19, '贵族女孩'),
    TXT(0x1A, '贵族青年'),
    TXT(0x1B, '贵族中年女子'),
    TXT(0x1C, '贵族老人'),
    TXT(0x1D, '贵族小孩'),
    TXT(0x1E, '男性学者２'),
    TXT(0x1F, '管家'),
    TXT(0x20, '青年市民'),
    TXT(0x21, ' '),
    TXT(0x22, ''),
]

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

# id: 0xFFFF offset: 0x48C2
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

# id: 0x10002 offset: 0x21A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x63A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x63A
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

# id: 0x10005 offset: 0x65A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x65A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_66D',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

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
    Event(0, 0x0008)

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
    Event(0, 0x0006)

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

    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0008, -48300, 0, 18410, 90)
    SetChrPos(0x0009, -48500, 0, 17000, 135)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrChipByIndex(0x0008, 25)
    SetChrChipByIndex(0x0009, 25)

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
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

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
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0108, 190, 0, -7530, 0)
    SetChrPos(0x0101, -1330, 0, -8480, 0)
    SetChrPos(0x0102, 570, 0, -8760, 0)
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
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, 11820, 0, -6220, 250)
    SetChrPos(0x0009, 12550, 0, -5100, 250)
    SetChrPos(0x000B, 14020, 0, -5780, 250)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0108, 100, 400)

    ChrTalk(
        0x0108,
        (
            '#0080130595V#076F好的，冲进去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0910')
    def lambda_0910():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0910)

    @scena.Lambda('lambda_091E')
    def lambda_091E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_091E)

    @scena.Lambda('lambda_092C')
    def lambda_092C():
        CameraMove(6340, 0, -6950, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_092C)

    @scena.Lambda('lambda_0944')
    def lambda_0944():
        OP_67(0, 4710, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0944)

    @scena.Lambda('lambda_095C')
    def lambda_095C():
        OP_6C(68000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_095C)

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
    SetChrDirection(0x0101, 100, 0)

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

    @scena.Lambda('lambda_0A16')
    def lambda_0A16():
        CameraMove(10400, 0, -6130, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A16)

    @scena.Lambda('lambda_0A2E')
    def lambda_0A2E():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A2E)

    Sleep(50)

    @scena.Lambda('lambda_0A48')
    def lambda_0A48():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A48)

    Sleep(50)

    @scena.Lambda('lambda_0A62')
    def lambda_0A62():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0A62)

    SetChrChipByIndex(0x0008, 7)
    SetChrFlags(0x0008, 0x1000)

    @scena.Lambda('lambda_0A81')
    def lambda_0A81():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A81)

    Sleep(50)

    SetChrChipByIndex(0x0009, 38)
    SetChrFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_0AA5')
    def lambda_0AA5():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AA5)

    Sleep(50)

    SetChrChipByIndex(0x000B, 38)
    SetChrFlags(0x000B, 0x1000)

    @scena.Lambda('lambda_0AC9')
    def lambda_0AC9():
        OP_92(0x00FE, 0x0108, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AC9)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x0008, 0x1000)
    ClearChrFlags(0x0009, 0x1000)
    ClearChrFlags(0x000B, 0x1000)
    Battle(0x000003AD, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_B2C'),
        (-1, 'loc_B2F'),
    )

    def _loc_B2C(): pass

    label('loc_B2C')

    OP_B4(0x00)

    Return()

    def _loc_B2F(): pass

    label('loc_B2F')

    EventBegin(0x00)
    SetChrChipByIndex(0x0008, 25)
    SetChrChipByIndex(0x0009, 25)
    SetChrChipByIndex(0x000B, 25)
    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrSubChip(0x000B, 0)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrPos(0x0008, 11700, 0, -9160, 176)
    SetChrPos(0x0009, 12780, 0, -10830, 90)
    SetChrPos(0x000B, 10700, 0, -11180, 296)
    CameraMove(10320, 0, -5900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, 7960, 0, -6540, 90)
    SetChrPos(0x0108, 9450, 0, -5900, 270)
    SetChrPos(0x0102, 8270, 0, -5050, 90)
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

# id: 0x0004 offset: 0xD10
@scena.Code('func_04_D10')
def func_04_D10():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 4, 0x654)),
            Expr.Return,
        ),
        'loc_D18',
    )

    Return()

    def _loc_D18(): pass

    label('loc_D18')

    SetScenaFlags(ScenaFlag(0x00CA, 4, 0x654))
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, -52180, 0, 20500, 180)
    SetChrPos(0x0009, -50170, 0, 20530, 180)
    SetChrChipByIndex(0x0008, 39)
    SetChrChipByIndex(0x0009, 39)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0D70')
    def lambda_0D70():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0D70)

    @scena.Lambda('lambda_0D7E')
    def lambda_0D7E():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D7E)

    @scena.Lambda('lambda_0D8C')
    def lambda_0D8C():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D8C)

    CameraMove(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0108, -50910, 0, 8080, 0)
    SetChrPos(0x0102, -50140, 0, 6930, 0)
    SetChrPos(0x0101, -52160, 0, 7020, 0)

    @scena.Lambda('lambda_0DED')
    def lambda_0DED():
        ChrWalkTo(0x00FE, -51000, 0, 12780, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0DED)

    @scena.Lambda('lambda_0E08')
    def lambda_0E08():
        ChrWalkTo(0x00FE, -51970, 0, 11510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E08)

    @scena.Lambda('lambda_0E23')
    def lambda_0E23():
        ChrWalkTo(0x00FE, -50210, 0, 11920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E23)

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
    SetChrChipByIndex(0x0009, 40)
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
    SetChrChipByIndex(0x0008, 40)
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

    @scena.Lambda('lambda_0FD3')
    def lambda_0FD3():
        CameraMove(-50570, 0, 20000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FD3)

    SetChrChipByIndex(0x0008, 41)

    @scena.Lambda('lambda_0FF0')
    def lambda_0FF0():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FF0)

    Sleep(50)

    SetChrChipByIndex(0x0008, 41)

    @scena.Lambda('lambda_100F')
    def lambda_100F():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_100F)

    @scena.Lambda('lambda_1024')
    def lambda_1024():
        ChrWalkTo(0x00FE, -51080, 0, 39570, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1024)

    Sleep(50)

    @scena.Lambda('lambda_1044')
    def lambda_1044():
        OP_92(0x00FE, 0x0008, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1044)

    Sleep(50)

    @scena.Lambda('lambda_105E')
    def lambda_105E():
        OP_92(0x00FE, 0x0009, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_105E)

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
        (0x00000001, 'loc_109F'),
        (-1, 'loc_10A2'),
    )

    def _loc_109F(): pass

    label('loc_109F')

    OP_B4(0x00)

    Return()

    def _loc_10A2(): pass

    label('loc_10A2')

    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0008, -48300, 0, 18410, 90)
    SetChrPos(0x0009, -48500, 0, 17000, 135)
    ClearChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x0009, 0x0001)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrChipByIndex(0x0008, 25)
    SetChrChipByIndex(0x0009, 25)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, -50450, 0, 17110, 0)
    SetChrPos(0x0108, -50450, 0, 17110, 0)
    SetChrPos(0x0102, -50450, 0, 17110, 0)

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

    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0108, 0)
    CameraMove(-50450, 0, 17110, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x1185
@scena.Code('func_05_1185')
def func_05_1185():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12B3',
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
        'loc_1279',
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

    Jump('loc_12AE')

    def _loc_1279(): pass

    label('loc_1279')

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

    def _loc_12AE(): pass

    label('loc_12AE')

    EventEnd(0x01)

    Jump('loc_133D')

    def _loc_12B3(): pass

    label('loc_12B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_1301',
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

    Jump('loc_133D')

    def _loc_1301(): pass

    label('loc_1301')

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

    def _loc_133D(): pass

    label('loc_133D')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0006 offset: 0x1343
@scena.Code('func_06_1343')
def func_06_1343():
    EventBegin(0x00)
    CameraMove(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(1760, 0)
    OP_6C(57000, 0)
    OP_6E(500, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x0010, 50, 250, 68860, 180)
    SetChrPos(0x000D, 6240, 0, 63940, 11)
    SetChrPos(0x000F, 3070, 0, 58560, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    SetChrPos(0x0101, -110, 0, 50960, 0)
    SetChrPos(0x0102, -110, 0, 50960, 0)
    SetChrPos(0x0108, -110, 0, 50960, 0)
    SetChrPos(0x000E, -110, 0, 50960, 0)
    SetChrPos(0x0013, -110, 0, 50960, 0)
    SetChrPos(0x0011, -110, 0, 50960, 0)
    SetChrPos(0x0012, -110, 0, 50960, 0)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)

    @scena.Lambda('lambda_14A3')
    def lambda_14A3():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14A3')

    DispatchAsync2(0x000D, 0x0001, lambda_14A3)

    @scena.Lambda('lambda_14B4')
    def lambda_14B4():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14B4')

    DispatchAsync2(0x001E, 0x0001, lambda_14B4)

    @scena.Lambda('lambda_14C5')
    def lambda_14C5():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14C5')

    DispatchAsync2(0x001F, 0x0001, lambda_14C5)

    @scena.Lambda('lambda_14D6')
    def lambda_14D6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14D6')

    DispatchAsync2(0x0020, 0x0001, lambda_14D6)

    @scena.Lambda('lambda_14E7')
    def lambda_14E7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14E7')

    DispatchAsync2(0x0021, 0x0001, lambda_14E7)

    @scena.Lambda('lambda_14F8')
    def lambda_14F8():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_14F8')

    DispatchAsync2(0x0022, 0x0001, lambda_14F8)

    @scena.Lambda('lambda_1509')
    def lambda_1509():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_1509')

    DispatchAsync2(0x0023, 0x0001, lambda_1509)

    @scena.Lambda('lambda_151A')
    def lambda_151A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_151A')

    DispatchAsync2(0x0024, 0x0001, lambda_151A)

    @scena.Lambda('lambda_152B')
    def lambda_152B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_152B')

    DispatchAsync2(0x0025, 0x0001, lambda_152B)

    @scena.Lambda('lambda_153C')
    def lambda_153C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_153C')

    DispatchAsync2(0x0026, 0x0001, lambda_153C)

    @scena.Lambda('lambda_154D')
    def lambda_154D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_154D')

    DispatchAsync2(0x0027, 0x0001, lambda_154D)

    OP_1F(0x50, 0x0000012C)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_156D')
    def lambda_156D():
        CameraMove(750, 0, 56890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_156D)

    @scena.Lambda('lambda_1585')
    def lambda_1585():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1585)

    @scena.Lambda('lambda_1597')
    def lambda_1597():
        ChrWalkTo(0x00FE, -60, 0, 57340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1597)

    Sleep(500)

    @scena.Lambda('lambda_15B7')
    def lambda_15B7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_15B7)

    @scena.Lambda('lambda_15C9')
    def lambda_15C9():
        ChrWalkTo(0x00FE, 770, 0, 56300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_15C9)

    Sleep(500)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1600')
    def lambda_1600():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1600)

    @scena.Lambda('lambda_1612')
    def lambda_1612():
        ChrWalkTo(0x00FE, -950, 0, 55860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1612)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_1637')
    def lambda_1637():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1637)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_164F')
    def lambda_164F():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_164F)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_1667')
    def lambda_1667():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1667)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_167A')
    def lambda_167A():
        CameraMove(2460, 0, 58180, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_167A)

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

    @scena.Lambda('lambda_1797')
    def lambda_1797():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1797)

    Sleep(100)

    @scena.Lambda('lambda_17AA')
    def lambda_17AA():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_17AA)

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

    @scena.Lambda('lambda_17DE')
    def lambda_17DE():
        CameraMove(70, 250, 68760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17DE)

    @scena.Lambda('lambda_17F6')
    def lambda_17F6():
        OP_67(0, 4420, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_17F6)

    @scena.Lambda('lambda_180E')
    def lambda_180E():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_180E)

    Sleep(1500)

    @scena.Lambda('lambda_1823')
    def lambda_1823():
        ChrWalkTo(0x00FE, -540, 0, 66590, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1823)

    Sleep(100)

    @scena.Lambda('lambda_1843')
    def lambda_1843():
        ChrWalkTo(0x00FE, 490, 0, 66590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1843)

    Sleep(300)

    @scena.Lambda('lambda_1863')
    def lambda_1863():
        ChrWalkTo(0x00FE, -2330, 0, 66150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1863)

    Sleep(100)

    @scena.Lambda('lambda_1883')
    def lambda_1883():
        ChrWalkTo(0x00FE, 2220, 0, 66920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1883)

    @scena.Lambda('lambda_189E')
    def lambda_189E():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_189E')

    DispatchAsync2(0x0101, 0x0000, lambda_189E)

    @scena.Lambda('lambda_18AF')
    def lambda_18AF():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_18AF')

    DispatchAsync2(0x0102, 0x0000, lambda_18AF)

    @scena.Lambda('lambda_18C0')
    def lambda_18C0():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_18C0')

    DispatchAsync2(0x0108, 0x0001, lambda_18C0)

    @scena.Lambda('lambda_18D1')
    def lambda_18D1():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_18D1')

    DispatchAsync2(0x000F, 0x0001, lambda_18D1)

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

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        OP_67(0, 6000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DB3)

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
    SetChrName('')

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
    SetChrPos(0x000D, -230, 0, 55310, 346)
    SetChrChipByIndex(0x0008, 37)
    SetChrFlags(0x0008, 0x0001)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x000C, 1020, 0, 56140, 0)
    SetChrPos(0x0008, 50, 0, 54770, 0)
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

    @scena.Lambda('lambda_25B7')
    def lambda_25B7():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_25B7)

    @scena.Lambda('lambda_25C5')
    def lambda_25C5():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_25C5)

    @scena.Lambda('lambda_25D3')
    def lambda_25D3():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25D3)

    @scena.Lambda('lambda_25E1')
    def lambda_25E1():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_25E1)

    @scena.Lambda('lambda_25EF')
    def lambda_25EF():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_25EF)

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        CameraMove(680, 0, 60840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25FD)

    @scena.Lambda('lambda_2615')
    def lambda_2615():
        OP_6E(500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2615)

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

    @scena.Lambda('lambda_267E')
    def lambda_267E():
        CameraMove(850, 0, 60760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_267E)

    @scena.Lambda('lambda_2696')
    def lambda_2696():
        OP_6E(450, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2696)

    SetChrChipByIndex(0x0101, 0)

    @scena.Lambda('lambda_26AB')
    def lambda_26AB():
        ChrWalkTo(0x00FE, -530, 0, 61260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_26AB)

    Sleep(200)

    SetChrChipByIndex(0x0102, 2)

    @scena.Lambda('lambda_26D0')
    def lambda_26D0():
        ChrWalkTo(0x00FE, 600, 0, 61850, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_26D0)

    Sleep(100)

    SetChrChipByIndex(0x0108, 4)

    @scena.Lambda('lambda_26F5')
    def lambda_26F5():
        ChrWalkTo(0x00FE, -2220, 0, 61880, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_26F5)

    Sleep(200)

    @scena.Lambda('lambda_2715')
    def lambda_2715():
        ChrWalkTo(0x00FE, 10, 0, 63520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2715)

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

    @scena.Lambda('lambda_2BEC')
    def lambda_2BEC():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2BEC)

    @scena.Lambda('lambda_2BFA')
    def lambda_2BFA():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2BFA)

    @scena.Lambda('lambda_2C08')
    def lambda_2C08():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2C08)

    @scena.Lambda('lambda_2C16')
    def lambda_2C16():
        CameraMove(500, 0, 59390, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2C16)

    OP_6E(500, 800)

    @scena.Lambda('lambda_2C37')
    def lambda_2C37():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2C37')

    DispatchAsync2(0x000C, 0x0001, lambda_2C37)

    @scena.Lambda('lambda_2C48')
    def lambda_2C48():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2C48')

    DispatchAsync2(0x0008, 0x0001, lambda_2C48)

    @scena.Lambda('lambda_2C59')
    def lambda_2C59():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2C59')

    DispatchAsync2(0x000D, 0x0001, lambda_2C59)

    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x000C, 0x0020)
    SetChrFlags(0x0012, 0x0020)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0012, 16)
    ClearChrFlags(0x0012, 0x0080)
    PlayBGM(47)

    @scena.Lambda('lambda_2C90')
    def lambda_2C90():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2C90')

    DispatchAsync2(0x0012, 0x0001, lambda_2C90)

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

    SetChrChipByIndex(0x0008, 43)

    @scena.Lambda('lambda_2D12')
    def lambda_2D12():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000BB8, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D12)

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
    SetChrChipByIndex(0x0008, 42)
    PlaySE(524, 0x00, 0x64)

    @scena.Lambda('lambda_2D5D')
    def lambda_2D5D():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D5D)

    Sleep(500)

    @scena.Lambda('lambda_2D72')
    def lambda_2D72():
        ChrWalkTo(0x00FE, -2850, 0, 55570, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2D72)

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

    @scena.Lambda('lambda_2E52')
    def lambda_2E52():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E52')

    DispatchAsync2(0x0101, 0x0001, lambda_2E52)

    @scena.Lambda('lambda_2E63')
    def lambda_2E63():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E63')

    DispatchAsync2(0x0102, 0x0001, lambda_2E63)

    @scena.Lambda('lambda_2E74')
    def lambda_2E74():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E74')

    DispatchAsync2(0x0108, 0x0001, lambda_2E74)

    @scena.Lambda('lambda_2E85')
    def lambda_2E85():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E85')

    DispatchAsync2(0x000F, 0x0001, lambda_2E85)

    @scena.Lambda('lambda_2E96')
    def lambda_2E96():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2E96')

    DispatchAsync2(0x0010, 0x0001, lambda_2E96)

    ChrTalk(
        0x0012,
        (
            '#0030130799V#021F#5P乖～乖～已经没事了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0012, 0xFF)
    SetChrDirection(0x0012, 45, 400)

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
    SetChrPos(0x0028, 1590, 1000, 54930, 0)
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

    SetChrChipByIndex(0x000C, 18)

    @scena.Lambda('lambda_3062')
    def lambda_3062():
        ChrJumpTo(0x00FE, 3030, 0, 57340, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3062)

    ChrTalk(
        0x000C,
        (
            '#2680130805V#10A呜哦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_309E')
    def lambda_309E():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_309E')

    DispatchAsync2(0x0012, 0x0001, lambda_309E)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrDirection(0x0012, 90, 0)

    @scena.Lambda('lambda_30C1')
    def lambda_30C1():
        ChrJumpTo(0x00FE, 1090, 0, 56780, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_30C1)

    Sleep(200)

    PlaySE(502, 0x00, 0x64)
    OP_99(0x0012, 0x02, 0x04, 4000)
    PlayEffect(0x08, 0xFF, 0x00FF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x000C, 0x0004)

    @scena.Lambda('lambda_312C')
    def lambda_312C():
        CameraMove(6320, 0, 57730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_312C)

    @scena.Lambda('lambda_3144')
    def lambda_3144():
        ChrMoveTo(0x00FE, 9480, 500, 56550, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3144)

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

    SetChrChipByIndex(0x000C, 17)

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

    SetChrChipByIndex(0x0012, 14)
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

    @scena.Lambda('lambda_32E3')
    def lambda_32E3():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_32E3')

    DispatchAsync2(0x0012, 0x0001, lambda_32E3)

    @scena.Lambda('lambda_32F4')
    def lambda_32F4():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_32F4')

    DispatchAsync2(0x000D, 0x0001, lambda_32F4)

    @scena.Lambda('lambda_3305')
    def lambda_3305():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3305')

    DispatchAsync2(0x0101, 0x0001, lambda_3305)

    @scena.Lambda('lambda_3316')
    def lambda_3316():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3316')

    DispatchAsync2(0x0102, 0x0001, lambda_3316)

    @scena.Lambda('lambda_3327')
    def lambda_3327():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3327')

    DispatchAsync2(0x0108, 0x0001, lambda_3327)

    @scena.Lambda('lambda_3338')
    def lambda_3338():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3338')

    DispatchAsync2(0x000F, 0x0001, lambda_3338)

    @scena.Lambda('lambda_3349')
    def lambda_3349():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_3349')

    DispatchAsync2(0x0010, 0x0001, lambda_3349)

    ClearChrFlags(0x0013, 0x0080)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_336A')
    def lambda_336A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_336A)

    @scena.Lambda('lambda_337C')
    def lambda_337C():
        ChrWalkTo(0x00FE, 30, 0, 55280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_337C)

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
    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_33DF')
    def lambda_33DF():
        ChrWalkTo(0x00FE, -1000, 0, 57140, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_33DF)

    Sleep(200)

    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_3404')
    def lambda_3404():
        ChrWalkTo(0x00FE, 240, 0, 58050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3404)

    Sleep(200)

    SetChrChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_3429')
    def lambda_3429():
        ChrWalkTo(0x00FE, -2000, 0, 57950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_3429)

    Sleep(300)

    @scena.Lambda('lambda_3449')
    def lambda_3449():
        ChrWalkTo(0x00FE, 120, 0, 59660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_3449)

    Sleep(200)

    @scena.Lambda('lambda_3469')
    def lambda_3469():
        ChrWalkTo(0x00FE, 2470, 0, 59650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_3469)

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
    SetChrDirection(0x0012, 270, 400)

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

    @scena.Lambda('lambda_381E')
    def lambda_381E():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_381E)

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

    @scena.Lambda('lambda_390B')
    def lambda_390B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_390B)

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

    @scena.Lambda('lambda_3A23')
    def lambda_3A23():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3A23)

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

    @scena.Lambda('lambda_3AC8')
    def lambda_3AC8():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AC8)

    @scena.Lambda('lambda_3AD6')
    def lambda_3AD6():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3AD6)

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
    SetChrPos(0x0011, -110, 0, 50960, 0)
    SetChrPos(0x000E, -110, 0, 50960, 0)
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

    @scena.Lambda('lambda_3C43')
    def lambda_3C43():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3C43)

    @scena.Lambda('lambda_3C51')
    def lambda_3C51():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C51)

    @scena.Lambda('lambda_3C5F')
    def lambda_3C5F():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3C5F)

    @scena.Lambda('lambda_3C6D')
    def lambda_3C6D():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3C6D)

    @scena.Lambda('lambda_3C7B')
    def lambda_3C7B():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_3C7B)

    @scena.Lambda('lambda_3C89')
    def lambda_3C89():
        ChrMoveTo(0x00FE, 1190, 0, 55790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_3C89)

    @scena.Lambda('lambda_3CA4')
    def lambda_3CA4():
        ChrMoveTo(0x00FE, -1720, 0, 57080, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3CA4)

    Sleep(500)

    @scena.Lambda('lambda_3CC4')
    def lambda_3CC4():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3CC4')

    DispatchAsync2(0x0101, 0x0001, lambda_3CC4)

    @scena.Lambda('lambda_3CD5')
    def lambda_3CD5():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3CD5')

    DispatchAsync2(0x0102, 0x0001, lambda_3CD5)

    @scena.Lambda('lambda_3CE6')
    def lambda_3CE6():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3CE6')

    DispatchAsync2(0x0108, 0x0001, lambda_3CE6)

    @scena.Lambda('lambda_3CF7')
    def lambda_3CF7():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3CF7')

    DispatchAsync2(0x0013, 0x0001, lambda_3CF7)

    @scena.Lambda('lambda_3D08')
    def lambda_3D08():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3D08')

    DispatchAsync2(0x0012, 0x0001, lambda_3D08)

    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x1000)
    SetChrChipByIndex(0x0011, 44)

    @scena.Lambda('lambda_3D28')
    def lambda_3D28():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3D28)

    @scena.Lambda('lambda_3D3A')
    def lambda_3D3A():
        ChrWalkTo(0x00FE, -350, 0, 57210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3D3A)

    Sleep(500)

    PlaySE(140, 0x00, 0x64)
    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000E, 0x0004)

    @scena.Lambda('lambda_3D6E')
    def lambda_3D6E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3D6E)

    @scena.Lambda('lambda_3D80')
    def lambda_3D80():
        ChrWalkTo(0x00FE, 830, 0, 59590, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3D80)

    WaitForThreadExit(0x0011, 0x0001)
    SetChrChipByIndex(0x0011, 45)
    SetChrSubChip(0x0011, 2)
    WaitForThreadExit(0x000E, 0x0001)
    CreateThread(0x000E, 0x01, 0x00, 0x0007)
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
    SetChrFlags(0x000E, 0x0020)

    @scena.Lambda('lambda_3E2C')
    def lambda_3E2C():
        OP_99(0x00FE, 0x00, 0x07, 5000)
        Yield()

        Jump('lambda_3E2C')

    DispatchAsync2(0x000E, 0x0002, lambda_3E2C)

    @scena.Lambda('lambda_3E3F')
    def lambda_3E3F():
        ChrMoveTo(0x00FE, -730, 600, 57540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3E3F)

    SetChrDirection(0x000E, 45, 100)
    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_3E66')
    def lambda_3E66():
        ChrMoveTo(0x00FE, -730, 0, 57540, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3E66)

    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x000E, 0x02)
    Fade(500)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 36)
    SetChrSubChip(0x0011, 1)
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
    SetChrName('')

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

# id: 0x0007 offset: 0x4098
@scena.Code('func_07_4098')
def func_07_4098():
    OP_A6(0x0000)
    def _loc_409B(): pass

    label('loc_409B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40BC',
    )

    OP_97(0x00FE, 130, 59590, -360000, 5000, 0x0001)
    Yield()

    Jump('loc_409B')

    def _loc_40BC(): pass

    label('loc_40BC')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0008 offset: 0x40C0
@scena.Code('func_08_40C0')
def func_08_40C0():
    EventBegin(0x00)
    CameraMove(1040, 130, 67720, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x0011, -40, 250, 70880, 180)
    SetChrPos(0x0102, -2410, 0, 67020, 45)
    SetChrPos(0x0013, -3610, 0, 67070, 61)
    SetChrPos(0x0108, -3890, 0, 68290, 80)
    SetChrPos(0x0101, 2540, 0, 67490, 320)
    SetChrPos(0x0010, 1280, 0, 67070, 2)
    SetChrPos(0x0012, 2980, 0, 66110, 297)
    SetChrPos(0x0014, -730, 0, 65269, 0)
    SetChrPos(0x0016, 180, 0, 64510, 0)
    SetChrPos(0x0015, -950, 0, 63940, 0)
    SetChrPos(0x0017, -2170, 0, 64410, 0)
    SetChrPos(0x0018, -1770, 0, 61620, 0)
    SetChrPos(0x0018, 70, 0, 61620, 0)
    SetChrPos(0x0018, 1840, 0, 61620, 0)
    SetChrPos(0x0018, -1770, 0, 59790, 0)
    SetChrPos(0x0018, 70, 0, 59790, 0)
    SetChrPos(0x0018, 1840, 0, 59790, 0)
    SetChrChipByIndex(0x0010, 24)

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
    SetChrDirection(0x0011, 180, 400)

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
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x4764
@scena.Code('func_09_4764')
def func_09_4764():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47C7',
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

    Jump('loc_4892')

    def _loc_47C7(): pass

    label('loc_47C7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4831',
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

    Jump('loc_4892')

    def _loc_4831(): pass

    label('loc_4831')

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

    def _loc_4892(): pass

    label('loc_4892')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
