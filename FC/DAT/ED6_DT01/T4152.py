import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4152_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4152   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奈尔'),
    TXT(0x02, '士兵'),
    TXT(0x03, '士兵'),
    TXT(0x04, '士兵'),
    TXT(0x05, '士兵'),
    TXT(0x06, '士兵'),
    TXT(0x07, '士兵'),
    TXT(0x08, '鸽子'),
    TXT(0x09, '鸽子'),
    TXT(0x0A, '鸽子'),
    TXT(0x0B, '鸽子'),
    TXT(0x0C, '鸽子'),
    TXT(0x0D, '鸽子'),
    TXT(0x0E, '鸽子'),
    TXT(0x0F, '鸽子'),
    TXT(0x10, '鸽子'),
    TXT(0x11, '鸽子'),
    TXT(0x12, '王都格兰赛尔·北街区'),
    TXT(0x13, '王都格兰赛尔·西街区'),
    TXT(0x14, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4152.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x15F9
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFEC780,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 4200,
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01730._CH', 'ED6_DT07/CH01730P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
    ]

# id: 0x10002 offset: 0x10A
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
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
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
    )

# id: 0x10003 offset: 0x36A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x36A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -82190,
            y           = 0,
            z           = 13740,
            range       = -75710,
            dword_10    = 0x00000BB8,
            dword_14    = 0x0000292C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -63040,
            y           = -3750,
            z           = -33480,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = -63390,
            y           = -3750,
            z           = -24940,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -78840,
            y           = 1250,
            z           = 12430,
            range       = 2000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000013,
        ),
    )

# id: 0x10005 offset: 0x3EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -76990,
            triggerZ            = -3500,
            triggerY            = -30450,
            triggerRange        = 800,
            actorX              = -76990,
            actorZ              = -2500,
            actorY              = -30450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92000,
            triggerZ            = 800,
            triggerY            = -4000,
            triggerRange        = 800,
            actorX              = -92000,
            actorZ              = 1800,
            actorY              = -4000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
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
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x456
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_464',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0003)

    def _loc_464(): pass

    label('loc_464')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_472',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x000D)

    def _loc_472(): pass

    label('loc_472')

    Return()

# id: 0x0001 offset: 0x473
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -185000, -131000, 196701)
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49A',
    )

    OP_72(0x000A, 0x0010)
    OP_65(0x00, 0x0001)

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AD',
    )

    OP_1B(0x03, 0x00, 0x000E)

    def _loc_4AD(): pass

    label('loc_4AD')

    OP_72(0x000E, 0x0008)
    OP_72(0x000E, 0x0020)
    OP_72(0x000E, 0x0002)
    OP_6F(0x000E, 0)
    OP_72(0x000B, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)
    OP_72(0x000D, 0x0010)
    OP_72(0x0005, 0x0010)
    OP_72(0x0009, 0x0010)
    OP_72(0x000A, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_59F',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    CreateThread(0x0009, 0x01, 0x00, 0x0005)
    CreateThread(0x000A, 0x01, 0x00, 0x0005)
    CreateThread(0x000B, 0x01, 0x00, 0x0005)
    CreateThread(0x000C, 0x01, 0x00, 0x0005)
    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    CreateThread(0x000E, 0x01, 0x00, 0x0005)

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_545',
    )

    def _loc_545(): pass

    label('loc_545')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_550',
    )

    def _loc_550(): pass

    label('loc_550')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_564',
    )

    SetChrFlags(0x000B, 0x0080)
    TerminateThread(0x000B, 0xFF)

    def _loc_564(): pass

    label('loc_564')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_578',
    )

    SetChrFlags(0x000D, 0x0080)
    TerminateThread(0x000D, 0xFF)

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.Eval, "OP_29(0x0048, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_58C',
    )

    SetChrFlags(0x000E, 0x0080)
    TerminateThread(0x000E, 0xFF)

    def _loc_58C(): pass

    label('loc_58C')

    CameraSetDistance(4200, 0)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_59F(): pass

    label('loc_59F')

    Return()

# id: 0x0002 offset: 0x5A0
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5B5(): pass

    label('loc_5B5')

    Return()

# id: 0x0003 offset: 0x5B6
@scena.Code('func_03_5B6')
def func_03_5B6():
    EventBegin(0x00)
    CameraMove(-63290, -3220, -25240, 0)
    OP_67(0, 12660, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(442, 0)

    @scena.Lambda('lambda_05FB')
    def lambda_05FB():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05FB)

    @scena.Lambda('lambda_0613')
    def lambda_0613():
        CameraSetDistance(2800, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0613)

    @scena.Lambda('lambda_0623')
    def lambda_0623():
        OP_6C(270000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0623)

    @scena.Lambda('lambda_0633')
    def lambda_0633():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0633)

    SetChrPos(0x0101, -61850, -3500, -25070, 270)
    SetChrPos(0x0102, -62010, -3500, -26170, 270)
    SetChrPos(0x0008, -63080, -3500, -25100, 270)
    ClearChrFlags(0x0008, 0x0080)
    Sleep(6000)

    ChrTalk(
        0x0101,
        (
            '#0010110505V#000F哎～这家店的气氛真不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110506V与其说是酒馆，\n',
            '还不如称为咖啡店更好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110507V#010F这种香气，就是咖啡的味道吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0270110508V#141F#5P这可是老板按照自己的兴趣布置的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110509V用玻璃器具煮出来的咖啡，\n',
            '不能不说是精品中的精品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110510V另外，用本地产的调料做的咖喱饭\n',
            '也是很值得你们一试试的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110511V不过，吃饭和喝咖啡的事一会儿再说，\n',
            '现在我们还是先……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110512V#005F#3S等一下！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010110513V#007F我们比赛已经很累了，\n',
            '肚子都快饿扁啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110514V#019F就是这样，\n',
            '我们能不能先吃晚饭呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110515V#142F#5P呼呼……\n',
            '你们这些孩子真是不讨人喜欢啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110516V#144F哼，算了，\n',
            '你们想吃多少就吃多少吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110517V待会儿取材的时候，\n',
            '可要给我把你们知道的通通说出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110518V#006F果然是为了这个来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110519V#014F话说回来，\n',
            '朵洛希小姐今天没有一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110520V#140F#5P嗯，她去做别的工作去了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110521V不说这个了，我们还是赶快进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4137._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xA13
@scena.Code('func_04_A13')
def func_04_A13():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A6E',
    )

    EventBegin(0x01)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

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
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x01)

    Jump('loc_BD3')

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B61',
    )

    EventBegin(0x01)
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

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
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110430V#010F看起来这里就是『渡鸦帮』那些家伙\n',
            '所说的地下水路的入口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_BD3')

    def _loc_B61(): pass

    label('loc_B61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 2, 0x622)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD3',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '使用了',
            (TxtCtl.SetColor, 0x2),
            '地下水路的钥匙Ａ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x00C4, 2, 0x622))
    OP_70(0x000A, 60)
    OP_73(0x000A)
    OP_64(0x00, 0x0001)
    OP_71(0x000A, 0x0010)
    EventEnd(0x00)

    def _loc_BD3(): pass

    label('loc_BD3')

    Return()

# id: 0x0005 offset: 0xBD4
@scena.Code('func_05_BD4')
def func_05_BD4():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E3B',
    )

    Yield()

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x151),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C07',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_C07(): pass

    label('loc_C07')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x125),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C2D',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_C2D(): pass

    label('loc_C2D')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xF8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C53',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_C53(): pass

    label('loc_C53')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xCA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C7A',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_C7A(): pass

    label('loc_C7A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x9E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CA0',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_CA0(): pass

    label('loc_CA0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x70),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CC6',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_CC6(): pass

    label('loc_CC6')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x44),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CEB',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_CEB(): pass

    label('loc_CEB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x16),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D10',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D24')

    def _loc_D10(): pass

    label('loc_D10')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D24(): pass

    label('loc_D24')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.PushReg, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E38',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x00FE, 0x00)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 400)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 5, 0x62D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E29',
    )

    ChrTalk(
        0x00FE,
        (
            '#4190111258V你们是干什么的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111259V#580F（糟糕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111260V#017F（被发现了吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E29(): pass

    label('loc_E29')

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4133._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x01)

    Return()

    def _loc_E38(): pass

    label('loc_E38')

    Jump('func_05_BD4')

    def _loc_E3B(): pass

    label('loc_E3B')

    Return()

# id: 0x0006 offset: 0xE3C
@scena.Code('func_06_E3C')
def func_06_E3C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E62',
    )

    SetChrPos(0x00FE, -42250, 0, -8170, 180)
    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_06_E3C')

    def _loc_E62(): pass

    label('loc_E62')

    Return()

# id: 0x0007 offset: 0xE63
@scena.Code('func_07_E63')
def func_07_E63():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E89',
    )

    SetChrPos(0x00FE, -38960, 0, -8109, 180)
    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_07_E63')

    def _loc_E89(): pass

    label('loc_E89')

    Return()

# id: 0x0008 offset: 0xE8A
@scena.Code('func_08_E8A')
def func_08_E8A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EF7',
    )

    SetChrPos(0x00FE, -54990, -3750, -18870, 180)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)

    Jump('func_08_E8A')

    def _loc_EF7(): pass

    label('loc_EF7')

    Return()

# id: 0x0009 offset: 0xEF8
@scena.Code('func_09_EF8')
def func_09_EF8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F65',
    )

    SetChrPos(0x00FE, -74820, -3500, -19000, 180)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)

    Jump('func_09_EF8')

    def _loc_F65(): pass

    label('loc_F65')

    Return()

# id: 0x000A offset: 0xF66
@scena.Code('func_0A_F66')
def func_0A_F66():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FD3',
    )

    SetChrPos(0x00FE, -74820, -3500, -30850, 180)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)

    Jump('func_0A_F66')

    def _loc_FD3(): pass

    label('loc_FD3')

    Return()

# id: 0x000B offset: 0xFD4
@scena.Code('func_0B_FD4')
def func_0B_FD4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1041',
    )

    SetChrPos(0x00FE, -54990, -3750, -30850, 180)
    ChrWalkTo(0x00FE, -74820, -3500, -30850, 3000, 0x00)
    ChrWalkTo(0x00FE, -74820, -3500, -19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -18870, 3000, 0x00)
    ChrWalkTo(0x00FE, -54990, -3750, -30850, 3000, 0x00)

    Jump('func_0B_FD4')

    def _loc_1041(): pass

    label('loc_1041')

    Return()

# id: 0x000C offset: 0x1042
@scena.Code('func_0C_1042')
def func_0C_1042():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 3, 0x62B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 6, 0x62E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11FB',
    )

    SetScenaFlags(ScenaFlag(0x00C5, 6, 0x62E))
    OP_28(0x0048, 0x01, 0x0200)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -78280, 1760, 11580, 0)
    SetChrPos(0x0102, -79290, 1760, 11770, 45)

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        OP_6C(350000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1086)

    CameraMove(-79030, 1760, 13490, 2000)
    Fade(1000)
    CameraSetDistance(2800, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111306V#001F（太好了，终于到了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111307V#012F（不要丧失警惕，艾丝蒂尔……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111308V（我先进去，你跟在我后面。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111309V#002F（嗯，好的……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, -79100, 1760, 12480, 2000, 0x00)
    SetChrDirection(0x0102, 0, 400)
    OP_70(0x000C, 60)
    OP_73(0x000C)

    @scena.Lambda('lambda_117F')
    def lambda_117F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_117F)

    @scena.Lambda('lambda_1191')
    def lambda_1191():
        ChrWalkTo(0x00FE, -78920, 1760, 13980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1191)

    Sleep(300)

    FadeOut(2000, 0, -1)
    ChrWalkTo(0x0101, -78630, 1760, 12450, 2000, 0x00)

    @scena.Lambda('lambda_11CF')
    def lambda_11CF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11CF)

    ChrWalkTo(0x0101, -78920, 1760, 13980, 2000, 0x00)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4134._SN', 100, 0, 0)
    IdleLoop()

    def _loc_11FB(): pass

    label('loc_11FB')

    Return()

# id: 0x000D offset: 0x11FC
@scena.Code('func_0D_11FC')
def func_0D_11FC():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    CameraMove(-79450, 4770, 11320, 0)
    OP_67(0, 6680, -10000, 0)
    CameraSetDistance(2460, 0)
    OP_6C(39000, 0)
    OP_6E(478, 0)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0014, 0x0004)
    SetChrFlags(0x0015, 0x0004)
    SetChrFlags(0x0016, 0x0004)
    SetChrPos(0x000F, -80280, 1520, 11070, 218)
    SetChrPos(0x0010, -77730, 1490, 10600, 146)
    SetChrPos(0x0011, -81930, 1250, 9130, 327)
    SetChrPos(0x0012, -79450, 1250, 9450, 44)
    SetChrPos(0x0013, -76040, 1250, 8290, 156)
    SetChrPos(0x0014, -81880, 750, 6280, 145)
    SetChrPos(0x0015, -79420, 250, 5000, 190)
    SetChrPos(0x0016, -77590, 750, 6270, 7)

    @scena.Lambda('lambda_1328')
    def lambda_1328():
        OP_67(0, 11700, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1328)

    @scena.Lambda('lambda_1340')
    def lambda_1340():
        OP_6C(351000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1340)

    @scena.Lambda('lambda_1350')
    def lambda_1350():
        OP_6E(544, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1350)

    @scena.Lambda('lambda_1360')
    def lambda_1360():
        ChrMoveToRelative(0x00FE, -5000, 10160, -20000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1360)

    Sleep(500)

    @scena.Lambda('lambda_1380')
    def lambda_1380():
        ChrMoveToRelative(0x00FE, -2500, 26160, -21000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1380)

    @scena.Lambda('lambda_139B')
    def lambda_139B():
        ChrMoveToRelative(0x00FE, 10000, 20160, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_139B)

    Sleep(200)

    @scena.Lambda('lambda_13BB')
    def lambda_13BB():
        ChrMoveToRelative(0x00FE, 15000, 15160, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_13BB)

    Sleep(200)

    @scena.Lambda('lambda_13DB')
    def lambda_13DB():
        ChrMoveToRelative(0x00FE, 15000, 20160, -15000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_13DB)

    @scena.Lambda('lambda_13F6')
    def lambda_13F6():
        ChrMoveToRelative(0x00FE, -5000, 15160, -10000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_13F6)

    Sleep(500)

    @scena.Lambda('lambda_1416')
    def lambda_1416():
        ChrMoveToRelative(0x00FE, 15000, 15160, -5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1416)

    Sleep(300)

    @scena.Lambda('lambda_1436')
    def lambda_1436():
        ChrMoveToRelative(0x00FE, -10000, 15160, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_1436)

    Sleep(100)

    Sleep(200)

    Sleep(7000)

    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4130._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x1467
@scena.Code('func_0E_1467')
def func_0E_1467():
    EventBegin(0x01)

    ChrTalk(
        0x0102,
        (
            '#0020110430V#010F看起来这里就是『渡鸦帮』那些家伙\n',
            '所说的地下水路的入口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110431V今天已经很晚了，\n',
            '明天再和金先生他们一起进去看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000F offset: 0x1510
@scena.Code('func_0F_1510')
def func_0F_1510():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　前面是港湾区　　　　\n',
            '※为强化警备体制，禁止通行',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0x1578
@scena.Code('func_10_1578')
def func_10_1578():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　 房屋出租\n',
            '※可以经营饭店',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0011 offset: 0x15C5
@scena.Code('func_11_15C5')
def func_11_15C5():
    OP_13(0x00B8)

    Return()

# id: 0x0012 offset: 0x15C9
@scena.Code('func_12_15C9')
def func_12_15C9():
    OP_13(0x00B7)

    Return()

# id: 0x0013 offset: 0x15CD
@scena.Code('func_13_15CD')
def func_13_15CD():
    OP_13(0x00AF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
