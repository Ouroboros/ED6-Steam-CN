import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4103   ._SN')

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
    TXT(0x21, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4103.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x241A
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
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10002 offset: 0x11A
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
            dword_10            = 5,
            chipIndex           = 5,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
    )

# id: 0x10003 offset: 0x51A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x51A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 23240,
            y           = -1000,
            z           = 7400,
            range       = 17390,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE0D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 44270,
            y           = 1000,
            z           = 940,
            range       = 48410,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00000000,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 45450,
            y           = 1000,
            z           = 6140,
            range       = 47430,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00001144,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10005 offset: 0x57A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x57A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_588',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_588(): pass

    label('loc_588')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_596',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0004)

    def _loc_596(): pass

    label('loc_596')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_5AD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0015)

    def _loc_5AD(): pass

    label('loc_5AD')

    Return()

# id: 0x0001 offset: 0x5AE
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -90000, -113000, 196710)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            Expr.Return,
        ),
        'loc_5D5',
    )

    OP_71(0x0000, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5D5(): pass

    label('loc_5D5')

    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x5DB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5F0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5F0(): pass

    label('loc_5F0')

    Return()

# id: 0x0003 offset: 0x5F1
@scena.Code('func_03_5F1')
def func_03_5F1():
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

    @scena.Lambda('lambda_066B')
    def lambda_066B():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_066B)

    Sleep(2000)

    @scena.Lambda('lambda_0680')
    def lambda_0680():
        OP_6E(228, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0680)

    CameraMove(26290, 0, 960, 5000)

    ChrTalk(
        0x0008,
        (
            '哈啊……\n',
            '肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0018,
        (
            '还没到换班时间吗？',
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
            '反正在逃中的人\n',
            '连１０个都不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那些家伙，上校只要想的话，\n',
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

    ChrTalk(
        0x000E,
        (
            '……只要你们办得到\n',
            '就尽管来试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0822')
    def lambda_0822():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0822)

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0830)

    @scena.Lambda('lambda_083E')
    def lambda_083E():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_083E)

    @scena.Lambda('lambda_084E')
    def lambda_084E():
        CameraMove(20430, 0, 1370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_084E)

    @scena.Lambda('lambda_0866')
    def lambda_0866():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0866)

    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '亲卫队中队长，\n',
            '尤莉亚·舒华兹！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x8C2
@scena.Code('func_04_8C2')
def func_04_8C2():
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

    ChrTalk(
        0x000E,
        (
            '#170F总算收拾掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B83')
    def lambda_0B83():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0B83)

    @scena.Lambda('lambda_0B91')
    def lambda_0B91():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0B91)

    @scena.Lambda('lambda_0B9F')
    def lambda_0B9F():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0B9F)

    @scena.Lambda('lambda_0BAD')
    def lambda_0BAD():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0BAD)

    @scena.Lambda('lambda_0BBB')
    def lambda_0BBB():
        ChrTurnDirection(0x00FE, 0x0017, 800)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0BBB)

    Sleep(100)

    @scena.Lambda('lambda_0BCE')
    def lambda_0BCE():
        CameraMove(19050, 0, 1190, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BCE)

    @scena.Lambda('lambda_0BE6')
    def lambda_0BE6():
        OP_6C(315000, 2300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0BE6)

    Sleep(400)

    CreateThread(0x0022, 0x01, 0x00, 0x0006)
    CreateThread(0x0023, 0x01, 0x00, 0x0007)
    CreateThread(0x0024, 0x01, 0x00, 0x0008)
    CreateThread(0x0017, 0x01, 0x00, 0x0005)
    CreateThread(0x0018, 0x01, 0x00, 0x000B)
    CreateThread(0x001D, 0x01, 0x00, 0x0010)
    Sleep(600)

    @scena.Lambda('lambda_0C2A')
    def lambda_0C2A():
        CameraMove(25500, 0, 390, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C2A)

    @scena.Lambda('lambda_0C42')
    def lambda_0C42():
        OP_67(0, 6710, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C42)

    CreateThread(0x0019, 0x01, 0x00, 0x000C)
    CreateThread(0x001E, 0x01, 0x00, 0x0011)
    Sleep(400)

    CreateThread(0x001A, 0x01, 0x00, 0x000D)
    CreateThread(0x001F, 0x01, 0x00, 0x0012)
    Sleep(400)

    CreateThread(0x001B, 0x01, 0x00, 0x000E)
    CreateThread(0x0020, 0x01, 0x00, 0x0013)
    Sleep(400)

    CreateThread(0x001C, 0x01, 0x00, 0x000F)
    CreateThread(0x0021, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x0025, 0x01, 0x00, 0x0009)
    CreateThread(0x0026, 0x01, 0x00, 0x000A)
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
            '#2680130574V飞行艇是严密封锁了的，\n',
            '不会那么容易被你们抢走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#170F…………………………',
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
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000A, 13660, 0, -70, 90)
    SetChrPos(0x000B, 12560, 0, -2110, 75)
    SetChrPos(0x000C, 13730, 0, -1250, 68)
    SetChrPos(0x000D, 12340, 0, 1110, 97)

    @scena.Lambda('lambda_0E00')
    def lambda_0E00():
        CameraMove(28050, 0, 980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E00)

    SetChrChipByIndex(0x0022, 11)
    SetChrChipByIndex(0x0023, 11)
    SetChrChipByIndex(0x0024, 11)

    @scena.Lambda('lambda_0E27')
    def lambda_0E27():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_0E27)

    @scena.Lambda('lambda_0E42')
    def lambda_0E42():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_0E42)

    @scena.Lambda('lambda_0E5D')
    def lambda_0E5D():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_0E5D)

    Sleep(100)

    SetChrChipByIndex(0x0018, 9)
    SetChrChipByIndex(0x001C, 9)

    @scena.Lambda('lambda_0E87')
    def lambda_0E87():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0E87)

    @scena.Lambda('lambda_0EA2')
    def lambda_0EA2():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_0EA2)

    Sleep(100)

    SetChrChipByIndex(0x0019, 9)
    SetChrChipByIndex(0x001D, 9)

    @scena.Lambda('lambda_0ECC')
    def lambda_0ECC():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0ECC)

    @scena.Lambda('lambda_0EE7')
    def lambda_0EE7():
        ChrWalkTo(0x00FE, 37290, 0, 320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_0EE7)

    Sleep(100)

    PlayEffect(0x08, 0xFF, 0x00FF, 21350, 3000, 30, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    TerminateThread(0x001B, 0xFF)
    PlayEffect(0x08, 0xFF, 0x00FF, 17730, 1000, -580, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x001B, 12)
    SetChrDirection(0x001B, 244, 0)

    @scena.Lambda('lambda_0F86')
    def lambda_0F86():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0F86)

    Sleep(100)

    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    TerminateThread(0x0024, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    TerminateThread(0x0019, 0xFF)
    TerminateThread(0x001D, 0xFF)
    TerminateThread(0x001E, 0xFF)
    SetChrChipByIndex(0x0017, 8)
    SetChrChipByIndex(0x0018, 8)
    SetChrChipByIndex(0x0019, 8)
    SetChrChipByIndex(0x001A, 8)
    SetChrChipByIndex(0x001C, 8)
    SetChrChipByIndex(0x001D, 8)
    SetChrChipByIndex(0x001E, 8)
    SetChrChipByIndex(0x001F, 8)
    SetChrChipByIndex(0x0020, 8)
    SetChrChipByIndex(0x0021, 8)
    SetChrChipByIndex(0x0022, 10)
    SetChrChipByIndex(0x0023, 10)
    SetChrChipByIndex(0x0024, 10)
    SetChrChipByIndex(0x0025, 10)
    SetChrChipByIndex(0x0026, 10)

    @scena.Lambda('lambda_1006')
    def lambda_1006():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_1006)

    @scena.Lambda('lambda_1014')
    def lambda_1014():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1014)

    @scena.Lambda('lambda_1022')
    def lambda_1022():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1022)

    @scena.Lambda('lambda_1030')
    def lambda_1030():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_1030)

    @scena.Lambda('lambda_103E')
    def lambda_103E():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_103E)

    @scena.Lambda('lambda_104C')
    def lambda_104C():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_104C)

    @scena.Lambda('lambda_105A')
    def lambda_105A():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_105A)

    @scena.Lambda('lambda_1068')
    def lambda_1068():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1068)

    @scena.Lambda('lambda_1076')
    def lambda_1076():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_1076)

    @scena.Lambda('lambda_1084')
    def lambda_1084():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_1084)

    @scena.Lambda('lambda_1092')
    def lambda_1092():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_1092)

    @scena.Lambda('lambda_10A0')
    def lambda_10A0():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_10A0)

    @scena.Lambda('lambda_10AE')
    def lambda_10AE():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_10AE)

    @scena.Lambda('lambda_10BC')
    def lambda_10BC():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_10BC)

    @scena.Lambda('lambda_10CA')
    def lambda_10CA():
        ChrTurnDirection(0x00FE, 0x000A, 800)

        ExitThread()

    DispatchAsync(0x0026, 0x0001, lambda_10CA)

    @scena.Lambda('lambda_10D8')
    def lambda_10D8():
        OP_67(0, 4650, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_10D8)

    @scena.Lambda('lambda_10F0')
    def lambda_10F0():
        OP_6C(291000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_10F0)

    CameraMove(18070, 0, 1210, 1500)

    ChrTalk(
        0x0017,
        (
            '呀……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '游、游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '你们打算\n',
            '与军队为敌吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '很抱歉……\n',
            '你们的所作所为是违法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '奉陛下的口谕，\n',
            '前来消灭你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x11A3
@scena.Code('func_05_11A3')
def func_05_11A3():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 17640, 0, -360, 6000, 0x00)
    ChrWalkTo(0x00FE, 21560, 0, 0, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    @scena.Lambda('lambda_11DB')
    def lambda_11DB():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_11DB')

    DispatchAsync2(0x00FE, 0x0000, lambda_11DB)

    Return()

# id: 0x0006 offset: 0x11E9
@scena.Code('func_06_11E9')
def func_06_11E9():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 18430, 10, -2280, 6000, 0x00)
    ChrWalkTo(0x00FE, 22420, 0, -2220, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1221')
    def lambda_1221():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1221')

    DispatchAsync2(0x00FE, 0x0000, lambda_1221)

    Return()

# id: 0x0007 offset: 0x122F
@scena.Code('func_07_122F')
def func_07_122F():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 19470, 0, -110, 6000, 0x00)
    ChrWalkTo(0x00FE, 23240, 0, -50, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1267')
    def lambda_1267():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1267')

    DispatchAsync2(0x00FE, 0x0000, lambda_1267)

    Return()

# id: 0x0008 offset: 0x1275
@scena.Code('func_08_1275')
def func_08_1275():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17780, 0, 1050, 6000, 0x00)
    ChrWalkTo(0x00FE, 22340, 0, 1920, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_12AD')
    def lambda_12AD():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_12AD')

    DispatchAsync2(0x00FE, 0x0000, lambda_12AD)

    Return()

# id: 0x0009 offset: 0x12BB
@scena.Code('func_09_12BB')
def func_09_12BB():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17510, 0, -2090, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_12DF')
    def lambda_12DF():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_12DF')

    DispatchAsync2(0x00FE, 0x0000, lambda_12DF)

    Return()

# id: 0x000A offset: 0x12ED
@scena.Code('func_0A_12ED')
def func_0A_12ED():
    SetChrChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 17230, 0, 2360, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 10)

    @scena.Lambda('lambda_1311')
    def lambda_1311():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1311')

    DispatchAsync2(0x00FE, 0x0000, lambda_1311)

    Return()

# id: 0x000B offset: 0x131F
@scena.Code('func_0B_131F')
def func_0B_131F():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 21940, 100, -3370, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000C offset: 0x1352
@scena.Code('func_0C_1352')
def func_0C_1352():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20370, 20, -2280, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000D offset: 0x1385
@scena.Code('func_0D_1385')
def func_0D_1385():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 20460, 0, -750, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000E offset: 0x13B8
@scena.Code('func_0E_13B8')
def func_0E_13B8():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 18470, 0, -690, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x000F offset: 0x13D7
@scena.Code('func_0F_13D7')
def func_0F_13D7():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16680, 0, -1480, 6000, 0x00)
    ChrWalkTo(0x00FE, 19200, 30, -3090, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0010 offset: 0x140A
@scena.Code('func_10_140A')
def func_10_140A():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 21670, 0, 3110, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0011 offset: 0x143D
@scena.Code('func_11_143D')
def func_11_143D():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 20410, 0, 1810, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0012 offset: 0x1470
@scena.Code('func_12_1470')
def func_12_1470():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19710, 0, 540, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0013 offset: 0x14A3
@scena.Code('func_13_14A3')
def func_13_14A3():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 18220, 0, 1520, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0014 offset: 0x14D6
@scena.Code('func_14_14D6')
def func_14_14D6():
    SetChrChipByIndex(0x00FE, 9)
    ChrWalkTo(0x00FE, 16250, 0, 670, 6000, 0x00)
    ChrWalkTo(0x00FE, 19540, 0, 3570, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 8)

    Return()

# id: 0x0015 offset: 0x1509
@scena.Code('func_15_1509')
def func_15_1509():
    ClearMapFlags(0x02000000)
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
    FormationAddMember(0x04, 0xFF)
    FormationAddMember(0x02, 0xFF)
    SetChrStatus(0x0002, 0x00, 34)
    OP_B5(0x0002, 0x00)
    OP_B5(0x0002, 0x01)
    OP_B5(0x0002, 0x05)
    OP_B5(0x0002, 0x04)
    OP_B5(0x0002, 0x03)
    OP_B5(0x0002, 0x02)
    EquipCmd(0x02, 0x0040)
    EquipCmd(0x02, 0x00F6)
    EquipCmd(0x02, 0x0114)
    EquipCmd(0x02, 0x026F, 0x00)
    EquipCmd(0x02, 0x026C, 0x01)
    EquipCmd(0x02, 0x0260, 0x05)
    EquipCmd(0x02, 0x0269, 0x04)
    EquipCmd(0x02, 0x0271, 0x03)
    EquipCmd(0x02, 0x0280, 0x02)
    AddCraft(0x0002, 0x00AA)
    AddCraft(0x0002, 0x00AB)
    AddCraft(0x0002, 0x00AC)
    AddSCraft(0x0002, 0x00F0)
    SetChrStatus(0x0004, 0x00, 32)
    OP_B5(0x0004, 0x00)
    OP_B5(0x0004, 0x05)
    OP_B5(0x0004, 0x04)
    OP_B5(0x0004, 0x03)
    OP_B5(0x0004, 0x02)
    OP_B5(0x0004, 0x01)
    EquipCmd(0x04, 0x007C)
    EquipCmd(0x04, 0x00F6)
    EquipCmd(0x04, 0x0114)
    EquipCmd(0x04, 0x025A, 0x00)
    EquipCmd(0x04, 0x0262, 0x05)
    EquipCmd(0x04, 0x02C9, 0x04)
    EquipCmd(0x04, 0x0265, 0x03)
    EquipCmd(0x04, 0x025D, 0x02)
    EquipCmd(0x04, 0x02D4, 0x01)
    AddCraft(0x0004, 0x00BE)
    AddCraft(0x0004, 0x00BF)
    AddSCraft(0x0004, 0x00FA)
    SetChrPos(0x0101, 46320, -10, -1800, 0)
    SetChrPos(0x0103, 47360, 0, -2280, 0)
    SetChrPos(0x0105, 45230, 0, -2280, 0)

    @scena.Lambda('lambda_1642')
    def lambda_1642():
        CameraMove(46300, -40, -1440, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1642)

    @scena.Lambda('lambda_165A')
    def lambda_165A():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_165A)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010131054V#002F情报部的特务飞艇……\n',
            '没想到会是在这种情况下乘坐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131055V#025F怎么说好呢……\n',
            '真是造型随便、低俗的飞艇啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131056V#027F和空贼飞艇真是棋逢对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131057V#043F不过话说回来，\n',
            '拥有很强大的性能这一点是没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131058V这样的一艘飞艇，\n',
            '情报部是怎么得到的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131059V#505F嗯，说到这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131060V#007F那个叫『福音』的导力器\n',
            '也隐藏了不少秘密呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0027, 46370, 200, 6000, 180)
    ClearChrFlags(0x0027, 0x0080)
    OP_4A(0x0027, 255)

    NpcTalk(
        0x0027,
        '青年的声音',
        (
            '#2350131061V#4P呀，是公主殿下啊。\n',
            '让您久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_183B')
    def lambda_183B():
        CameraMove(46270, 200, 430, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_183B)

    @scena.Lambda('lambda_1853')
    def lambda_1853():
        ChrWalkTo(0x00FE, 46370, 200, 1090, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0027, 0x0001, lambda_1853)

    WaitForThreadExit(0x0027, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060131062V#041F是佩顿师傅啊。\n',
            '你好，真是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131063V#501F咦……这个人是?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131064V#040F他是佩顿师傅，\n',
            '『埃尔赛尤号』巡洋舰的维修员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131065V#5P我是由中央工房\n',
            '外派的技术人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131066V#5P因为『埃尔赛尤号』处于试飞阶段，\n',
            '所以需要测试并处理各种数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131067V#004F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131068V可是，在卢安看到那飞艇的时候，\n',
            '还是飞得好好的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131069V#5P一般的飞行当然是可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131070V#5P因为新型的导力引擎开发进度推迟，\n',
            '所以暂时只能用旧型的引擎，\n',
            '这样就不能发挥其应有的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131071V#5P而且现在飞艇又被情报部给夺走了，\n',
            '试飞只有无限延期了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131072V#5P我在王都走投无路的时候，\n',
            '尤莉亚中尉就让我到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131073V#000F原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131074V#021F呵呵……\n',
            '请多多指教哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131075V#5P好、好的，交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B77')
    def lambda_1B77():
        ChrTurnDirection(0x00FE, 0x0027, 400)
        Yield()

        Jump('lambda_1B77')

    DispatchAsync2(0x0101, 0x0001, lambda_1B77)

    @scena.Lambda('lambda_1B88')
    def lambda_1B88():
        ChrTurnDirection(0x00FE, 0x0027, 400)
        Yield()

        Jump('lambda_1B88')

    DispatchAsync2(0x0105, 0x0001, lambda_1B88)

    @scena.Lambda('lambda_1B99')
    def lambda_1B99():
        ChrTurnDirection(0x00FE, 0x0027, 400)
        Yield()

        Jump('lambda_1B99')

    DispatchAsync2(0x0103, 0x0001, lambda_1B99)

    ChrWalkTo(0x0027, 48030, 200, 730, 2000, 0x00)
    ChrTurnDirection(0x0027, 0x0105, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)

    ChrTalk(
        0x0027,
        (
            '#2350131076V#5P只要解开锁定，\n',
            '就可以开动飞艇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131077V#5P因为飞艇的机动性很高，\n',
            '所以驾驶时要小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131078V#042F#6P我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131079V#006F那么，\n',
            '我们赶快上飞艇去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0027, 270, 0)
    OP_4B(0x0027, 255)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x1C93
@scena.Code('func_16_1C93')
def func_16_1C93():
    TalkBegin(0x0027)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 7, 0x65F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D31',
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
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '购买道具\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D0A',
    )

    OP_0D()
    OP_A9(0x6C)
    OP_56(0x00)
    TalkEnd(0x0027)

    Return()

    def _loc_1D0A(): pass

    label('loc_1D0A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D20',
    )

    OP_0D()
    OP_A9(0x6D)
    OP_56(0x00)
    TalkEnd(0x0027)

    Return()

    def _loc_1D20(): pass

    label('loc_1D20')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D31',
    )

    TalkEnd(0x0027)

    Return()

    def _loc_1D31(): pass

    label('loc_1D31')

    ChrTalk(
        0x0027,
        (
            '我带了一些可以调整大家的\n',
            '导力器的工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '还有，我也准备了一些装备和道具，\n',
            '虽然种类不算很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '有需要的话请说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0027)

    Return()

# id: 0x0017 offset: 0x1DB5
@scena.Code('func_17_1DB5')
def func_17_1DB5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 7, 0x65F)),
            Expr.Return,
        ),
        'loc_1DBD',
    )

    Return()

    def _loc_1DBD(): pass

    label('loc_1DBD')

    EventBegin(0x00)
    OP_4A(0x0027, 255)
    SetChrDirection(0x0027, 225, 400)

    ChrTalk(
        0x0027,
        (
            '#2350131080V……哦，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0027, 0)
    ChrTurnDirection(0x0105, 0x0027, 0)
    ChrTurnDirection(0x0103, 0x0027, 0)

    ChrTalk(
        0x0027,
        (
            '#2350131081V我带了一些可以调整大家的\n',
            '导力器的工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131082V还有，我也准备了一些装备和道具，\n',
            '虽然种类不算很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131083V#001F啊，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131084V#027F哎呀，还是挺会办事的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131085V#041F您真是帮了我们大忙了，\n',
            '真是非常感谢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131086V东、东西不多，希望能派上用场。',
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
    SetChrDirection(0x0027, 270, 0)
    OP_4B(0x0027, 255)
    EventEnd(0x01)

    Return()

# id: 0x0018 offset: 0x1F4E
@scena.Code('func_18_1F4E')
def func_18_1F4E():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0105, 46310, 200, 4320, 176)
    SetChrPos(0x0103, 46840, 200, 3150, 0)
    SetChrPos(0x0101, 45710, 200, 3160, 0)
    CameraMove(46390, 250, 4580, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060131091V#042F#5P距离正午已经没有多少时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131092V这就乘坐飞艇并启动引擎吗？\n',
            '　',
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
            TXT(0x00, '【乘坐飞艇】\n'),
            TXT(0x01, '【整理装备】\n'),
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
        (0x00000000, 'loc_205F'),
        (0x00000001, 'loc_207D'),
        (-1, 'loc_20D8'),
    )

    def _loc_205F(): pass

    label('loc_205F')

    ChrTalk(
        0x0105,
        (
            '#0060131093V#047F#5P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D8')

    def _loc_207D(): pass

    label('loc_207D')

    ChrTalk(
        0x0105,
        (
            '#0060131094V#040F#5P好的。',
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

    def _loc_20D8(): pass

    label('loc_20D8')

    OP_28(0x004D, 0x01, 0x0020)
    OP_4A(0x0027, 255)
    ChrTurnDirection(0x0027, 0x0105, 400)
    CameraMove(47340, 250, 3680, 1000)

    ChrTalk(
        0x0105,
        (
            '#0060131096V#040F#5P……佩顿师傅，请你在后面协助我。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131097V#2P遵命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0027,
        (
            '#2350131098V#2P引擎的调整就交给我吧，\n',
            '殿下专心驾驶飞艇就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010131099V#002F#6P雪拉姐，终于要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030131100V#026F#2P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131101V#020F任务虽然很艰巨，不过原则是相通的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131102V迅速果敢……以及沉着冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x2253
@scena.Code('func_19_2253')
def func_19_2253():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 6, 0x65E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_23E5',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22F7',
    )

    ChrTurnDirection(0x0105, 0x0000, 400)

    ChrTalk(
        0x0105,
        (
            '#0060131103V#043F嗯，\n',
            '距离正午已经没有多少时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131104V准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010131105V#006F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_22F7(): pass

    label('loc_22F7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_236A',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    ChrTalk(
        0x0103,
        (
            '#0030131106V#022F距离作战开始已经没有多少时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131107V确认完装备就赶快上飞艇去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23CA')

    def _loc_236A(): pass

    label('loc_236A')

    ChrTurnDirection(0x0105, 0x0001, 400)

    ChrTalk(
        0x0105,
        (
            '#0060131108V#042F距离正午已经没有多少时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131104V准备好了的话，\n',
            '我们就上飞艇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23CA(): pass

    label('loc_23CA')

    ChrMoveToRelative(0x0000, 2000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_23E5(): pass

    label('loc_23E5')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
