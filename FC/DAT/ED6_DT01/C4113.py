import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4113   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特务兵'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '卡露娜'),
    TXT(0x04, '亚妮拉丝'),
    TXT(0x05, '库拉茨'),
    TXT(0x06, '克鲁茨'),
    TXT(0x07, '尤莉亚中尉'),
    TXT(0x08, '亲卫队员'),
    TXT(0x09, '亲卫队员'),
    TXT(0x0A, '亲卫队员'),
    TXT(0x0B, '亲卫队员'),
    TXT(0x0C, '亲卫队员'),
    TXT(0x0D, '亲卫队员'),
    TXT(0x0E, '亲卫队员'),
    TXT(0x0F, '亲卫队员'),
    TXT(0x10, '中队长'),
    TXT(0x11, '特务兵'),
    TXT(0x12, '特务兵'),
    TXT(0x13, '特务兵'),
    TXT(0x14, '特务兵'),
    TXT(0x15, '特务兵'),
    TXT(0x16, '特务兵'),
    TXT(0x17, '特务兵'),
    TXT(0x18, '特务兵'),
    TXT(0x19, '特务兵'),
    TXT(0x1A, '特务兵'),
    TXT(0x1B, '军用犬'),
    TXT(0x1C, '军用犬'),
    TXT(0x1D, '军用犬'),
    TXT(0x1E, '军用犬'),
    TXT(0x1F, '军用犬'),
    TXT(0x20, '修理员佩顿'),
    TXT(0x21, ' '),
    TXT(0x22, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4113.x'
    header.mapIndex       = 1
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x254C
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00400._CH', 'ED6_DT07/CH00400P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT06/CH20115._CH', 'ED6_DT06/CH20115P._CP'),
        ('ED6_DT06/CH20116._CH', 'ED6_DT06/CH20116P._CP'),
        ('ED6_DT06/CH20117._CH', 'ED6_DT06/CH20117P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH01790._CH', 'ED6_DT07/CH01790P._CP'),
        ('ED6_DT07/CH00502._CH', 'ED6_DT07/CH00502P._CP'),
        ('ED6_DT07/CH00510._CH', 'ED6_DT07/CH00510P._CP'),
        ('ED6_DT07/CH00511._CH', 'ED6_DT07/CH00511P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
    ]

# id: 0x10002 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            dword_10            = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 131087,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 131089,
            chipIndex           = 17,
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
            dword_10            = 1,
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
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
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

# id: 0x10003 offset: 0x59A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x59A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 14350,
            y           = -1000,
            z           = -8640,
            range       = 11930,
            dword_10    = 0x000007D0,
            dword_14    = 0x000019F0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 44270,
            y           = 1000,
            z           = 940,
            range       = 48410,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0xFFFFFF10,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 45450,
            y           = 1000,
            z           = 6140,
            range       = 47430,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00001144,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
    )

# id: 0x10005 offset: 0x5FA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x5FA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_611',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_61F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0003)

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_62D',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0014)

    def _loc_62D(): pass

    label('loc_62D')

    Return()

# id: 0x0001 offset: 0x62E
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -90000, -113000, 196710)
    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x646
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(45860, 0, 7990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(69000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 26320, 0, 2029, 270)
    SetChrPos(0x0009, 26350, 0, -100, 270)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_06C5')
    def lambda_06C5():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06C5)

    Sleep(2000)

    @scena.Lambda('lambda_06DA')
    def lambda_06DA():
        OP_6E(228, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06DA)

    CameraMove(26290, 0, 960, 5000)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0009, 0x0020)

    ChrTalk(
        0x0008,
        (
            '#2640130558V#5P哈啊……\n',
            '肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#2640130559V#5P还没到换班时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2650130560V喂喂，可别松懈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2650130561V潜伏中的亲卫队\n',
            '随时都有可能出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2640130562V#5P反正在逃中的人\n',
            '连十个都不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2640130563V#5P那些家伙，上校只要想的话，\n',
            '绝对一下就把他们给捉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x000E, 16180, 0, 1410, 90)
    SetChrPos(0x000F, 15420, 0, 630, 90)
    SetChrPos(0x0010, 15520, 0, 2230, 90)
    SetChrPos(0x0011, 14270, 0, 550, 90)
    SetChrPos(0x0012, 14270, 0, 2230, 90)
    SetChrSubChip(0x000E, 1)
    SetChrSubChip(0x000F, 2)
    SetChrSubChip(0x0010, 2)
    SetChrSubChip(0x0011, 2)
    SetChrSubChip(0x0012, 2)
    OP_20(0x000005DC)

    ChrTalk(
        0x000E,
        (
            '#0100130564V#2P……如果你们能办得到的话，\n',
            '就尽管来试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_090F')
    def lambda_090F():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_090F)

    @scena.Lambda('lambda_091D')
    def lambda_091D():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_091D)

    @scena.Lambda('lambda_092B')
    def lambda_092B():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_092B)

    @scena.Lambda('lambda_093B')
    def lambda_093B():
        CameraMove(20430, 0, 1370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_093B)

    @scena.Lambda('lambda_0953')
    def lambda_0953():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0953)

    Sleep(500)

    PlayBGM(89)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2640130565V#2P什……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2650130566V#2P亲卫队中队长……\n',
            '尤莉亚·舒华兹！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 25)
    SetChrChipByIndex(0x0009, 25)
    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrFlags(0x000E, 0x1000)
    SetChrFlags(0x000F, 0x1000)
    SetChrFlags(0x0010, 0x1000)
    SetChrFlags(0x0011, 0x1000)
    SetChrFlags(0x0012, 0x1000)
    SetChrChipByIndex(0x000E, 14)

    @scena.Lambda('lambda_0A19')
    def lambda_0A19():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A19)

    @scena.Lambda('lambda_0A2F')
    def lambda_0A2F():
        CameraMove(24930, 0, 1380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A2F)

    Sleep(200)

    SetChrChipByIndex(0x000F, 16)
    SetChrChipByIndex(0x0010, 16)
    SetChrChipByIndex(0x0011, 16)
    SetChrChipByIndex(0x0012, 16)

    @scena.Lambda('lambda_0A60')
    def lambda_0A60():
        OP_92(0x00FE, 0x0009, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0A60)

    Sleep(50)

    @scena.Lambda('lambda_0A7A')
    def lambda_0A7A():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0A7A)

    Sleep(50)

    @scena.Lambda('lambda_0A94')
    def lambda_0A94():
        OP_92(0x00FE, 0x0009, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0A94)

    Sleep(50)

    @scena.Lambda('lambda_0AAE')
    def lambda_0AAE():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0AAE)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xAD5
@scena.Code('func_03_AD5')
def func_03_AD5():
    EventBegin(0x00)
    CameraMove(30000, 0, 630, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(233000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x000E, 28310, 0, 210, 90)
    SetChrPos(0x000F, 29950, 0, -1020, 47)
    SetChrPos(0x0010, 29140, 0, 2290, 127)
    SetChrPos(0x0011, 31010, 0, 1560, 131)
    SetChrPos(0x0012, 31530, 0, -1200, 11)
    SetChrChipByIndex(0x0008, 12)
    SetChrChipByIndex(0x0009, 12)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 33200, 0, 2800, 26)
    SetChrPos(0x0009, 32790, 0, 420, 142)
    SetChrFlags(0x0017, 0x0040)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x001B, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x001D, 0x0040)
    SetChrFlags(0x001E, 0x0040)
    SetChrFlags(0x001F, 0x0040)
    SetChrFlags(0x0020, 0x0040)
    SetChrFlags(0x0021, 0x0040)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x0017, 11630, 0, -2640, 90)
    SetChrPos(0x0018, 9800, 0, -3930, 90)
    SetChrPos(0x0019, 9800, 0, -3930, 90)
    SetChrPos(0x001A, 9800, 0, -3930, 90)
    SetChrPos(0x001B, 9800, 0, -3930, 90)
    SetChrPos(0x001C, 9800, 0, -3930, 90)
    SetChrPos(0x001D, 9890, 0, -2180, 90)
    SetChrPos(0x001E, 9890, 0, -2180, 90)
    SetChrPos(0x001F, 9890, 0, -2180, 90)
    SetChrPos(0x0020, 9890, 0, -2180, 90)
    SetChrPos(0x0021, 9890, 0, -2180, 90)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    SetChrFlags(0x0022, 0x0040)
    SetChrFlags(0x0023, 0x0040)
    SetChrFlags(0x0024, 0x0040)
    SetChrFlags(0x0025, 0x0040)
    SetChrFlags(0x0026, 0x0040)
    SetChrPos(0x0022, 12030, 0, -4240, 90)
    SetChrPos(0x0023, 13140, 0, -2490, 72)
    SetChrPos(0x0024, 11810, 0, -930, 90)
    SetChrPos(0x0025, 8510, 0, -4850, 90)
    SetChrPos(0x0026, 8510, 0, -1080, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0100130571V#176F#5P总算收拾掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130572V#173F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 1)
    SetChrSubChip(0x000F, 1)
    SetChrSubChip(0x0010, 1)
    SetChrSubChip(0x0011, 1)
    SetChrSubChip(0x0012, 1)
    SetChrFlags(0x000E, 0x0020)
    SetChrFlags(0x000F, 0x0020)
    SetChrFlags(0x0010, 0x0020)
    SetChrFlags(0x0011, 0x0020)
    SetChrFlags(0x0012, 0x0020)

    @scena.Lambda('lambda_0DFC')
    def lambda_0DFC():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0DFC)

    @scena.Lambda('lambda_0E0A')
    def lambda_0E0A():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0E0A)

    @scena.Lambda('lambda_0E18')
    def lambda_0E18():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0E18)

    @scena.Lambda('lambda_0E26')
    def lambda_0E26():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0E26)

    @scena.Lambda('lambda_0E34')
    def lambda_0E34():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E34)

    Sleep(100)

    @scena.Lambda('lambda_0E47')
    def lambda_0E47():
        CameraMove(19050, 0, 1190, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E47)

    @scena.Lambda('lambda_0E5F')
    def lambda_0E5F():
        OP_6C(315000, 2300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E5F)

    Sleep(400)

    CreateThread(0x0022, 0x01, 0x00, 0x0005)
    CreateThread(0x0023, 0x01, 0x00, 0x0006)
    CreateThread(0x0024, 0x01, 0x00, 0x0007)
    CreateThread(0x0017, 0x01, 0x00, 0x0004)
    CreateThread(0x0018, 0x01, 0x00, 0x000A)
    CreateThread(0x001D, 0x01, 0x00, 0x000F)
    Sleep(600)

    @scena.Lambda('lambda_0EA3')
    def lambda_0EA3():
        CameraMove(25500, 0, 390, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EA3)

    @scena.Lambda('lambda_0EBB')
    def lambda_0EBB():
        OP_67(0, 6710, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0EBB)

    CreateThread(0x0019, 0x01, 0x00, 0x000B)
    CreateThread(0x001E, 0x01, 0x00, 0x0010)
    Sleep(400)

    CreateThread(0x001A, 0x01, 0x00, 0x000C)
    CreateThread(0x001F, 0x01, 0x00, 0x0011)
    Sleep(400)

    CreateThread(0x001B, 0x01, 0x00, 0x000D)
    CreateThread(0x0020, 0x01, 0x00, 0x0012)
    Sleep(400)

    CreateThread(0x001C, 0x01, 0x00, 0x000E)
    CreateThread(0x0021, 0x01, 0x00, 0x0013)
    Sleep(400)

    CreateThread(0x0025, 0x01, 0x00, 0x0008)
    CreateThread(0x0026, 0x01, 0x00, 0x0009)
    Sleep(2500)

    ChrTalk(
        0x0017,
        (
            '#2680130573V愚蠢的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130574V飞艇是上了锁的，\n',
            '不会那么容易被你们抢走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0100130575V#178F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130576V如果不乖乖服从上校，\n',
            '那么就只有用你们的性命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130577V顽固不化的家伙们，\n',
            '受死吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130578V进攻！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, 12560, 0, -2110, 70)
    SetChrPos(0x000D, 13660, 0, -70, 90)
    SetChrPos(0x000C, 13730, 0, -1250, 75)
    SetChrPos(0x000B, 12340, 0, 1110, 95)

    @scena.Lambda('lambda_106B')
    def lambda_106B():
        CameraMove(28050, 0, 980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_106B)

    LoadEffect(0x02, 'map\\\\mp019_00.eff')
    LoadEffect(0x00, 'craft\\\\cr201_02.eff')
    SetChrPos(0x0028, 19080, 0, 510, 0)
    PlayEffect(0x02, 0xFF, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x0028, 0, 0, 0, 0)
    Sleep(200)

    SetChrChipByIndex(0x0022, 11)
    SetChrChipByIndex(0x0023, 11)
    SetChrChipByIndex(0x0024, 11)

    @scena.Lambda('lambda_1107')
    def lambda_1107():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_1107)

    @scena.Lambda('lambda_1122')
    def lambda_1122():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_1122)

    @scena.Lambda('lambda_113D')
    def lambda_113D():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_113D)

    Sleep(100)

    SetChrChipByIndex(0x0018, 20)
    SetChrChipByIndex(0x001C, 9)

    @scena.Lambda('lambda_1167')
    def lambda_1167():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1167)

    @scena.Lambda('lambda_1182')
    def lambda_1182():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_1182)

    Sleep(100)

    SetChrChipByIndex(0x0019, 9)
    SetChrChipByIndex(0x001D, 9)

    @scena.Lambda('lambda_11AC')
    def lambda_11AC():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_11AC)

    @scena.Lambda('lambda_11C7')
    def lambda_11C7():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_11C7)

    PlaySE(506, 0x00, 0x64)
    Sleep(100)

    Sleep(200)

    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)
    Sleep(100)

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    TerminateThread(0x0024, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    SetChrChipByIndex(0x0017, 23)
    SetChrChipByIndex(0x0018, 19)
    SetChrChipByIndex(0x0019, 8)
    SetChrChipByIndex(0x001A, 19)
    SetChrChipByIndex(0x001C, 19)
    SetChrChipByIndex(0x001D, 8)
    SetChrChipByIndex(0x001E, 19)
    SetChrChipByIndex(0x001F, 8)
    SetChrChipByIndex(0x0020, 19)
    SetChrChipByIndex(0x0021, 8)
    SetChrChipByIndex(0x0022, 10)
    SetChrChipByIndex(0x0023, 10)
    SetChrChipByIndex(0x0024, 10)
    SetChrChipByIndex(0x0025, 10)
    SetChrChipByIndex(0x0026, 10)

    @scena.Lambda('lambda_1281')
    def lambda_1281():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1281)

    @scena.Lambda('lambda_128F')
    def lambda_128F():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_128F)

    @scena.Lambda('lambda_129D')
    def lambda_129D():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_129D)

    @scena.Lambda('lambda_12AB')
    def lambda_12AB():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_12AB)

    @scena.Lambda('lambda_12B9')
    def lambda_12B9():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_12B9)

    @scena.Lambda('lambda_12C7')
    def lambda_12C7():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_12C7)

    @scena.Lambda('lambda_12D5')
    def lambda_12D5():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_12D5)

    @scena.Lambda('lambda_12E3')
    def lambda_12E3():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_12E3)

    @scena.Lambda('lambda_12F1')
    def lambda_12F1():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_12F1)

    @scena.Lambda('lambda_12FF')
    def lambda_12FF():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_12FF)

    @scena.Lambda('lambda_130D')
    def lambda_130D():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_130D)

    @scena.Lambda('lambda_131B')
    def lambda_131B():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_131B)

    @scena.Lambda('lambda_1329')
    def lambda_1329():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_1329)

    @scena.Lambda('lambda_1337')
    def lambda_1337():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_1337)

    @scena.Lambda('lambda_1345')
    def lambda_1345():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_1345)

    @scena.Lambda('lambda_1353')
    def lambda_1353():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_1353)

    @scena.Lambda('lambda_1361')
    def lambda_1361():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1361')

    DispatchAsync2(0x0022, 0x0000, lambda_1361)

    @scena.Lambda('lambda_1374')
    def lambda_1374():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1374')

    DispatchAsync2(0x0023, 0x0000, lambda_1374)

    @scena.Lambda('lambda_1387')
    def lambda_1387():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1387')

    DispatchAsync2(0x0024, 0x0000, lambda_1387)

    @scena.Lambda('lambda_139A')
    def lambda_139A():
        OP_67(0, 4650, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_139A)

    @scena.Lambda('lambda_13B2')
    def lambda_13B2():
        OP_6C(291000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13B2)

    @scena.Lambda('lambda_13C2')
    def lambda_13C2():
        CameraMove(16070, 0, 1210, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13C2)

    Sleep(350)

    PlayEffect(0x00, 0xFF, 0x001B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001F, 0xFF)
    TerminateThread(0x0020, 0xFF)

    @scena.Lambda('lambda_148A')
    def lambda_148A():
        ChrMoveTo(0x001B, 19380, 0, -1920, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_148A)

    @scena.Lambda('lambda_14A5')
    def lambda_14A5():
        ChrMoveTo(0x001F, 20690, 0, 1130, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_14A5)

    @scena.Lambda('lambda_14C0')
    def lambda_14C0():
        ChrMoveTo(0x0020, 18740, 0, 2600, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_14C0)

    ChrTurnDirection(0x001B, 0x0028, 0)
    ChrTurnDirection(0x001F, 0x0028, 0)
    ChrTurnDirection(0x0020, 0x0028, 0)
    SetChrChipByIndex(0x001B, 18)
    SetChrChipByIndex(0x001F, 18)
    SetChrChipByIndex(0x0020, 18)
    SetChrFlags(0x001B, 0x0020)
    SetChrFlags(0x001F, 0x0020)
    SetChrFlags(0x0020, 0x0020)

    @scena.Lambda('lambda_150E')
    def lambda_150E():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_150E)

    @scena.Lambda('lambda_151E')
    def lambda_151E():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_151E)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_152E)

    Sleep(30)

    @scena.Lambda('lambda_1543')
    def lambda_1543():
        ChrMoveTo(0x001B, 19380, 0, -1920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_1543)

    @scena.Lambda('lambda_155E')
    def lambda_155E():
        ChrMoveTo(0x001F, 20690, 0, 1130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_155E)

    @scena.Lambda('lambda_1579')
    def lambda_1579():
        ChrMoveTo(0x0020, 18740, 0, 2600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_1579)

    Sleep(30)

    @scena.Lambda('lambda_1599')
    def lambda_1599():
        ChrMoveTo(0x001B, 19380, 0, -1920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_1599)

    @scena.Lambda('lambda_15B4')
    def lambda_15B4():
        ChrMoveTo(0x001F, 20690, 0, 1130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_15B4)

    @scena.Lambda('lambda_15CF')
    def lambda_15CF():
        ChrMoveTo(0x0020, 18740, 0, 2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0002, lambda_15CF)

    Sleep(30)

    TerminateThread(0x001B, 0x02)
    TerminateThread(0x001F, 0x02)
    TerminateThread(0x0020, 0x02)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0017,
        (
            '#2680130579V#2P游、游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2680130580V#2P你们打算与军队为敌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0330130581V#5P很抱歉……\n',
            '你们的所作所为是违法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0320130582V奉陛下的口谕，\n',
            '前来消灭你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x16A8
@scena.Code('func_04_16A8')
def func_04_16A8():
    SetChrChipByIndex(0x00FE, 24)
    ChrWalkTo(0x00FE, 17640, 0, -360, 6000, 0x00)
    ChrWalkTo(0x00FE, 21560, 0, 0, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 23)

    Return()

# id: 0x0005 offset: 0x16DB
@scena.Code('func_05_16DB')
def func_05_16DB():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 18430, 10, -2280, 6000, 0x00)
    ChrWalkTo(0x00FE, 22420, 0, -2220, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1713')
    def lambda_1713():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1713')

    DispatchAsync2(0x00FE, 0x0000, lambda_1713)

    Return()

# id: 0x0006 offset: 0x1721
@scena.Code('func_06_1721')
def func_06_1721():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 19470, 0, -110, 6000, 0x00)
    ChrWalkTo(0x00FE, 23240, 0, -50, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1759')
    def lambda_1759():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1759')

    DispatchAsync2(0x00FE, 0x0000, lambda_1759)

    Return()

# id: 0x0007 offset: 0x1767
@scena.Code('func_07_1767')
def func_07_1767():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17780, 0, 1050, 6000, 0x00)
    ChrWalkTo(0x00FE, 22340, 0, 1920, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_179F')
    def lambda_179F():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_179F')

    DispatchAsync2(0x00FE, 0x0000, lambda_179F)

    Return()

# id: 0x0008 offset: 0x17AD
@scena.Code('func_08_17AD')
def func_08_17AD():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17510, 0, -2090, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_17D1')
    def lambda_17D1():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_17D1')

    DispatchAsync2(0x00FE, 0x0000, lambda_17D1)

    Return()

# id: 0x0009 offset: 0x17DF
@scena.Code('func_09_17DF')
def func_09_17DF():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17230, 0, 2360, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1803')
    def lambda_1803():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1803')

    DispatchAsync2(0x00FE, 0x0000, lambda_1803)

    Return()

# id: 0x000A offset: 0x1811
@scena.Code('func_0A_1811')
def func_0A_1811():
    SetChrChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 21940, 100, -3370, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x000B offset: 0x1844
@scena.Code('func_0B_1844')
def func_0B_1844():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20370, 20, -2280, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000C offset: 0x1877
@scena.Code('func_0C_1877')
def func_0C_1877():
    SetChrChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20460, 0, -750, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x000D offset: 0x18AA
@scena.Code('func_0D_18AA')
def func_0D_18AA():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 18470, 0, -690, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000E offset: 0x18C9
@scena.Code('func_0E_18C9')
def func_0E_18C9():
    SetChrChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 19200, 30, -3090, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x000F offset: 0x18FC
@scena.Code('func_0F_18FC')
def func_0F_18FC():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 21670, 0, 3110, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0010 offset: 0x192F
@scena.Code('func_10_192F')
def func_10_192F():
    SetChrChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 20410, 0, 1810, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x0011 offset: 0x1962
@scena.Code('func_11_1962')
def func_11_1962():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19710, 0, 540, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0012 offset: 0x1995
@scena.Code('func_12_1995')
def func_12_1995():
    SetChrChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 18220, 0, 1520, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 19)

    Return()

# id: 0x0013 offset: 0x19C8
@scena.Code('func_13_19C8')
def func_13_19C8():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19540, 0, 3570, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0014 offset: 0x19FB
@scena.Code('func_14_19FB')
def func_14_19FB():
    EventBegin(0x00)
    CameraMove(46220, -50, 11920, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x02, 0xFF)
    FormationAddMember(0x04, 0xFF)
    OP_B5(0x0002, 0x00)
    OP_B5(0x0002, 0x01)
    OP_B5(0x0002, 0x02)
    OP_B5(0x0002, 0x03)
    OP_B5(0x0002, 0x04)
    OP_B5(0x0002, 0x05)
    EquipCmd(0x02, 0x0040)
    EquipCmd(0x02, 0x00F5)
    EquipCmd(0x02, 0x0113)
    EquipCmd(0x02, 0x026E, 0x00)
    EquipCmd(0x02, 0x026B, 0x01)
    EquipCmd(0x02, 0x025F, 0x02)
    EquipCmd(0x02, 0x0262, 0x03)
    EquipCmd(0x02, 0x0268, 0x04)
    EquipCmd(0x02, 0x0271, 0x05)
    AddCraft(0x0002, 0x00AA)
    AddCraft(0x0002, 0x00AB)
    AddSCraft(0x0002, 0x00F0)
    OP_B5(0x0004, 0x00)
    OP_B5(0x0004, 0x05)
    OP_B5(0x0004, 0x04)
    OP_B5(0x0004, 0x03)
    OP_B5(0x0004, 0x02)
    OP_B5(0x0004, 0x01)
    EquipCmd(0x04, 0x007C)
    EquipCmd(0x04, 0x00F5)
    EquipCmd(0x04, 0x0113)
    EquipCmd(0x04, 0x0259, 0x00)
    EquipCmd(0x04, 0x0261, 0x05)
    EquipCmd(0x04, 0x02C8, 0x04)
    EquipCmd(0x04, 0x0264, 0x03)
    EquipCmd(0x04, 0x025F, 0x02)
    EquipCmd(0x04, 0x027E, 0x01)
    AddCraft(0x0004, 0x00BE)
    AddCraft(0x0004, 0x00BF)
    AddSCraft(0x0004, 0x00FA)
    SetChrPos(0x0101, 46320, -10, -1800, 0)
    SetChrPos(0x0103, 47360, 0, -2280, 0)
    SetChrPos(0x0105, 45230, 0, -2280, 0)

    @scena.Lambda('lambda_1B21')
    def lambda_1B21():
        CameraMove(46300, -40, -1440, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B21)

    @scena.Lambda('lambda_1B39')
    def lambda_1B39():
        OP_6E(262, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B39)

    Sleep(7000)

    ChrTalk(
        0x0101,
        (
            '#000F情报部的特务艇……\n',
            '没想到要在这种情况下乘坐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F怎么说好呢……\n',
            '真是造型随便、低俗的飞艇啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '和空贼艇真是棋逢对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940001V#040F不过，拥有很强大的性能\n',
            '这一点是没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060940002V这样的一艘飞船，\n',
            '情报部是怎么得到的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F确实有很多谜团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0027, 46370, 200, 5440, 180)
    ClearChrFlags(0x0027, 0x0080)

    @scena.Lambda('lambda_1C76')
    def lambda_1C76():
        ChrWalkTo(0x00FE, 46370, 200, 1090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_1C76)

    Sleep(500)

    @scena.Lambda('lambda_1C96')
    def lambda_1C96():
        CameraMove(46270, 200, 430, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C96)

    WaitForThreadExit(0x0027, 0x0001)

    ChrTalk(
        0x0027,
        (
            '呀，是殿下啊。\n',
            '让您久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F佩顿师傅。。\n',
            '你好，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F咦……这个人是?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940003V#040F他是佩顿师傅，\n',
            '『埃尔赛尤号』飞船\n',
            '的维修人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '我是由中央工房\n',
            '外派的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '『埃尔赛尤号』\n',
            '现在还处于测试阶段，\n',
            '不能用于实战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131068V在卢安看到它的时候\n',
            '可是飞的好好的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '一般的飞行当然是可以的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '因为新型的导力引擎开发进度\n',
            '推迟而搭载了旧型的引擎，\n',
            '这样就不能发挥其应有的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '而且现在『埃尔赛尤号』又被\n',
            '情报部给夺走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '我在王都走投无路的时候，\n',
            '尤莉亚中尉就让我到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131073V#000F原来是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵……\n',
            '请多多指教哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '好、好的，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '只要解开锁定，\n',
            '就可以启动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0027, 44540, 200, 1020, 2000, 0x00)
    ChrTurnDirection(0x0027, 0x0105, 400)

    @scena.Lambda('lambda_1F7C')
    def lambda_1F7C():
        ChrTurnDirection(0x00FE, 0x0105, 0)
        Yield()

        Jump('lambda_1F7C')

    DispatchAsync2(0x0027, 0x0003, lambda_1F7C)

    ChrTalk(
        0x0027,
        (
            '因为飞艇的机动性很高，\n',
            '所以驾驶时要小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那么，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x1FE5
@scena.Code('func_15_1FE5')
def func_15_1FE5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 7, 0x65F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1FF2',
    )

    Return()

    def _loc_1FF2(): pass

    label('loc_1FF2')

    EventBegin(0x00)

    ChrTalk(
        0x0027,
        (
            '#2350131080V……哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131081V我带了一些可以调整\n',
            '大家的导力器的工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131082V还有，虽然种类不多，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，还是挺会办事的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F真是帮了我们大忙了。\n',
            '真是非常感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '东、东西不多，希望能派上用场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131087V有需要的话请说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CB, 7, 0x65F))
    EventEnd(0x01)

    Return()

# id: 0x0016 offset: 0x211D
@scena.Code('func_16_211D')
def func_16_211D():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0105, 46310, 200, 4320, 176)
    SetChrPos(0x0103, 46840, 200, 3150, 0)
    SetChrPos(0x0101, 45710, 200, 3160, 0)
    ChrTurnDirection(0x0027, 0x0105, 0)
    CameraMove(46390, 250, 4580, 1000)

    ChrTalk(
        0x0105,
        (
            '#040F距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131092V要乘坐飞艇\n',
            '并启动引擎吗？',
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
            TXT(0x00, '乘坐飞艇\n'),
            TXT(0x01, ' \n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2215'),
        (0x00000001, 'loc_222D'),
        (-1, 'loc_2282'),
    )

    def _loc_2215(): pass

    label('loc_2215')

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2282')

    def _loc_222D(): pass

    label('loc_222D')

    ChrTalk(
        0x0105,
        (
            '#040F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131095V#020F如果想整理装备的话\n',
            '就和修理员师傅说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2282(): pass

    label('loc_2282')

    SetScenaFlags(ScenaFlag(0x00CC, 0, 0x660))
    OP_28(0x004D, 0x01, 0x0020)
    ChrTurnDirection(0x0105, 0x0027, 400)

    ChrTalk(
        0x0105,
        (
            '#040F……佩顿师傅，\n',
            '请您在后面协助我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '引擎的调整就交给我吧，\n',
            '请殿下专心的驾驶飞艇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#000F雪拉姐，终于要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030131100V#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '任务虽然很艰巨，\n',
            '不过原则是相通的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131102V迅速果敢……以及沉着冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x239F
@scena.Code('func_17_239F')
def func_17_239F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_251B',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2435',
    )

    ChrTurnDirection(0x0105, 0x0000, 400)

    ChrTalk(
        0x0105,
        (
            '#0060940004V#042F嗯，距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#002F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2500')

    def _loc_2435(): pass

    label('loc_2435')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24A9',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030840005V#026F距离作战开始\n',
            '已经没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840006V#027F确认完装备\n',
            '就赶快上飞艇去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2500')

    def _loc_24A9(): pass

    label('loc_24A9')

    ChrTurnDirection(0x0105, 0x0001, 400)

    ChrTalk(
        0x0105,
        (
            '#0060131108V#042F距离正午已经\n',
            '没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2500(): pass

    label('loc_2500')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_251B(): pass

    label('loc_251B')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
