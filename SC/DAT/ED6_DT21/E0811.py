import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0811_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0811   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0811.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT27/CH03010._CH', 'ED6_DT27/CH03010P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT26/CH20370._CH', 'ED6_DT26/CH20370P._CP'),
        ('ED6_DT26/CH20400._CH', 'ED6_DT26/CH20400P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP'),
        ('ED6_DT26/CH20401._CH', 'ED6_DT26/CH20401P._CP'),
        ('ED6_DT27/CH03101._CH', 'ED6_DT27/CH03101P._CP'),
        ('ED6_DT26/CH20398._CH', 'ED6_DT26/CH20398P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT07/CH00051._CH', 'ED6_DT07/CH00051P._CP'),
        ('ED6_DT07/CH00021._CH', 'ED6_DT07/CH00021P._CP'),
        ('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP'),
        ('ED6_DT27/CH03081._CH', 'ED6_DT27/CH03081P._CP'),
        ('ED6_DT27/CH03001._CH', 'ED6_DT27/CH03001P._CP'),
        ('ED6_DT27/CH03011._CH', 'ED6_DT27/CH03011P._CP'),
        ('ED6_DT26/CH20327._CH', 'ED6_DT26/CH20327P._CP'),
        ('ED6_DT26/CH20398._CH', 'ED6_DT26/CH20398P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
    ]

# id: 0x10001 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '约修亚',
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
            name                = '乔丝特',
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
            name                = '吉尔',
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
            name                = '多伦',
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
            name                = '结社艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '结社艇右',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼艇右',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '尤莉亚上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01CC,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01CC,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x3EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -100290,
            y           = 5150,
            z           = -94850,
            range       = -98290,
            dword_10    = 0x00001BEE,
            dword_14    = 0xFFFE954E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x40A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x40A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_41B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_03_632)

    Jump('loc_57A')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_435',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x50),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_09_1AE2)

    Jump('loc_57A')

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_44F',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0E_239C)

    Jump('loc_57A')

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_469',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_1F_40D4)

    Jump('loc_57A')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_47A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    Event(0, func_25_464E)

    Jump('loc_57A')

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_494',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    Event(0, func_08_1870)

    Jump('loc_57A')

    def _loc_494(): pass

    label('loc_494')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_4AE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x50),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    Event(0, func_02_581)

    Jump('loc_57A')

    def _loc_4AE(): pass

    label('loc_4AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_4C8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    Event(0, func_27_4A4E)

    Jump('loc_57A')

    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Return,
        ),
        'loc_51E',
    )

    OP_76(0x00FF, 0x00000000, 0x0001, -1, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -2, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -5, -2, 0, 0x00, 0x00)
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    Event(0, func_29_4E9B)

    Jump('loc_57A')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            Expr.Return,
        ),
        'loc_57A',
    )

    OP_76(0x00FF, 0x00000000, 0x0001, -1, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -2, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -5, -2, 0, 0x00, 0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    Event(0, func_2A_4FC8)

    def _loc_57A(): pass

    label('loc_57A')

    Return()

# id: 0x0001 offset: 0x57B
@scena.Code('func_01_57B')
def func_01_57B():
    OP_71(0x0005, 0x0004)

    Return()

# id: 0x0002 offset: 0x581
@scena.Code('func_02_581')
def func_02_581():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    CameraMove(-213310, -10000, -14980, 0)
    OP_67(0, -2490, -10000, 0)
    CameraSetDistance(43240, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_05EE')
    def lambda_05EE():
        OP_67(0, -3300, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_05EE)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1500, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1211._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x632
@scena.Code('func_03_632')
def func_03_632():
    EventBegin(0x00)
    OP_DB()
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    ChrSetFlags(0x0102, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000F, 0x0003)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    ChrSetPos(0x000F, -99500, 0, -91500, 270)
    Yield()
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 400)
    OP_70(0x0003, 450)
    CameraMove(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    CameraSetDistance(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    OP_EB(0xD5, 0x00)
    OP_BB(0x01, 0x01, 0x00000001)
    OP_BD()
    FadeIn(2000, 0)

    @scena.Lambda('lambda_06EA')
    def lambda_06EA():
        CameraMove(-99550, 5550, -94010, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06EA)

    @scena.Lambda('lambda_0702')
    def lambda_0702():
        CameraSetDistance(2800, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0702)

    @scena.Lambda('lambda_0712')
    def lambda_0712():
        OP_6E(334, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0712)

    Sleep(6000)

    OP_72(0x0003, 0x0020)

    @scena.Lambda('lambda_072C')
    def lambda_072C():
        OP_6C(35000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_072C)

    OP_67(0, 7540, -10000, 4000)
    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    OP_73(0x0003)
    Sleep(1000)

    ChrSetFlags(0x000A, 0x0004)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetPos(0x000A, -99440, 5550, -91440, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrWalkTo(0x000A, -99470, 5540, -93960, 2000, 0x00)
    Sleep(500)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)
    OP_DC()

    ChrTalk(
        0x000A,
        (
            '#213F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 400)
    Sleep(500)

    ChrSetDirection(0x000A, 180, 400)
    ChrSetDirection(0x000A, 270, 400)
    Sleep(500)

    ChrSetDirection(0x000A, 180, 400)
    Sleep(500)

    ChrSetDirection(0x000A, 90, 400)
    Sleep(200)

    ChrSetPos(0x0102, -100000, 5550, -89650, 0)
    ChrSetFlags(0x0102, 0x0004)
    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetSubChip(0x0102, 2)
    CreateThread(0x000A, 0x01, 0x00, func_05_1647)

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        CameraMove(-98020, 5550, -89450, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0830)

    OP_6C(300000, 5000)
    OP_6C(212000, 5000)

    ChrTalk(
        0x000A,
        (
            '#0090320002V#210F怎么，原来在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 1)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)

    ChrTalk(
        0x0102,
        (
            '#1030F……这边可以\n',
            '比较清楚地看到月亮呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320004V肌肤也能感到风的流动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F哈哈，又～开始\n',
            '装模作样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_092B')
    def lambda_092B():
        CameraMove(-99380, 5550, -89630, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_092B)

    @scena.Lambda('lambda_0943')
    def lambda_0943():
        CameraSetDistance(2350, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0943)

    @scena.Lambda('lambda_0953')
    def lambda_0953():
        ChrWalkTo(0x000A, -99020, 5550, -89450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0953)

    Sleep(300)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    WaitForThreadExit(0x000A, 0x0000)
    ChrSetDirection(0x000A, 0, 400)
    WaitForThreadExit(0x0102, 0x0001)
    Fade(250)
    ChrSetChipByIndex(0x000A, 3)
    ChrSetSubChip(0x000A, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0090320006V#210F……哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '其实你这并不是在\n',
            '装模作样的吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这也是必要的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F因为月光、云的位置、风的流向\n',
            '都变得相当重要了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我希望把失败的可能性\n',
            '尽量降到最低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F尽、尽量？……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 4)
    Sleep(100)

    ChrTalk(
        0x000A,
        (
            '#210F我说你啊……\n',
            '可别说什么能尽力而为的话哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320013V失败了就是死路一条哦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F没关系，失败的可能性很小。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320015V这种程度的任务，\n',
            '以前每天都在做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '倒不如说更大的危险……\n',
            '是在任务成功之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……我说，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320019V你真的\n',
            '有必要做到这一步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#1030F嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F你也和我们一样\n',
            '是埃雷波尼亚出身的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然说彼此或许各有隐情\n',
            '而不能返回故乡……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但就算是这样，你也没必要\n',
            '为这个国家尽什么义务不是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320024V『结社』要做什么，\n',
            '放着不管不就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090320026V#210F好不好，现在还来得及。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320027V就这样，与我们一起\n',
            '离开利贝尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320028V去找个自治州\n',
            '揭竿而起怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320029V如果不想做空贼\n',
            '也可以找其他的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我和哥哥们也说过了，\n',
            '利用这艘船的速度\n',
            '来做运输业应该不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 5)
    Sleep(100)

    ChrSetSubChip(0x0102, 6)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#1030F用飞船做运输业吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320032V今后的需求也会陆续增加，\n',
            '或许是相当有前途的行业呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320033V至少应该能赚得\n',
            '比当空贼还多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090320034V#210F那、那就！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 5)
    Sleep(100)

    ChrSetSubChip(0x0102, 4)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#1030F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320036V粉碎了『结社』的阴谋之后\n',
            '如果我还活着\n',
            '就考虑考虑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F嗯，你不必担心\n',
            '我们的契约到此就结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只要配合这个作战计划，\n',
            '之前欠我的人情就一笔勾销了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320040V你们随时都可以出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#210F……够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(250)

    Fade(500)
    ChrSetDirection(0x000A, 270, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000A, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x000A,
        (
            '#210F笨蛋！\n',
            '谁在说什么欠人情的事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不用说了！\n',
            '谁知道你是谁啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320045V爱跳火坑就跳\n',
            '你愿意见鬼就见鬼去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    ChrSetChipByIndex(0x000A, 7)
    ChrWalkTo(0x000A, -94660, 5550, -90000, 5000, 0x00)
    ChrWalkTo(0x000A, -94810, 5550, -92930, 5000, 0x00)
    ChrWalkTo(0x000A, -99390, 5550, -93940, 5000, 0x00)
    PlaySE(106, 0x00, 0x64)
    ChrSetFlags(0x000A, 0x0080)
    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    Sleep(300)

    ChrSetSubChip(0x0102, 3)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 1)
    Sleep(100)

    ChrSetSubChip(0x0102, 2)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#1030F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……对不起，乔丝特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetPos(0x000B, -103120, 13050, -91360, 10)
    Sleep(300)

    NpcTalk(
        0x000B,
        '青年的声音',
        (
            '#3P真是的……\n',
            '假装迟钝可真没意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    ChrSetSubChip(0x0102, 1)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(100)

    OP_6F(0x0003, 90)
    ChrSetPos(0x000B, -103120, 9050, -91360, 10)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0020)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000B, 0x0080)
    Fade(500)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    OP_0D()
    ChrSetDirection(0x0102, 270, 400)

    @scena.Lambda('lambda_11CD')
    def lambda_11CD():
        CameraMove(-100330, 5550, -92350, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11CD)

    @scena.Lambda('lambda_11E5')
    def lambda_11E5():
        OP_67(0, 9500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_11E5)

    OP_6C(144000, 4000)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#1030F……吉尔先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0290320049V#200F那家伙也是一样，\n',
            '脱离不了小孩子个性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320050V不过，刚才毕竟是\n',
            '你的说话方式不对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然并不打算道歉，\n',
            '但还是觉得对不起她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#200F真是的……\n',
            '虽然知道这就是你\n',
            '关心别人的方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，刚才的话\n',
            '还是认真考虑一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290320055V等一切都了结之后，\n',
            '要是你不打算回那个\n',
            '游击士小姑娘身边的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F哈哈……不会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320057V毕竟，我和她\n',
            '生存的世界差距太大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320058V不可能再有交集了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0290320059V#200F嗯……\n',
            '嗯，那也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '既然这样就\n',
            '更好说话了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F是啊……\n',
            '我会积极考虑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(171, 0x01, 0x64)
    Sleep(500)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(2200)

    OP_23(0x00AB)

    ChrTalk(
        0x000B,
        (
            '#200F……出现了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 400)
    ChrSetPos(0x000B, -103120, 8900, -91360, 270)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#200F大哥，来了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, -103120, 6550, -91360, 270)

    NpcTalk(
        0x000C,
        '多伦的声音',
        (
            '哟！\n',
            '正如小子预料的一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300320065V从东北方向\n',
            '不断接近中呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000B, -103120, 9050, -91360, 270)
    ChrSetDirection(0x000B, 10, 400)

    ChrTalk(
        0x000B,
        (
            '#200F你听到了吧。\n',
            '马上过来舰桥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 400)
    CreateThread(0x000B, 0x01, 0x00, func_04_162D)
    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0003, 90)
    OP_70(0x0003, 160)
    SetScenaFlags(ScenaFlag(0x0380, 0, 0x1C00))
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '◆这个剧情使用的临时地图。\n',
            '　进入船内的时候请按DEBUG键『J』来接触入口附近。\n',
            '　接触临时入口就能进入里面。',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x162D
@scena.Code('func_04_162D')
def func_04_162D():
    ChrMoveTo(0x00FE, -103120, 6050, -91360, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0005 offset: 0x1647
@scena.Code('func_05_1647')
def func_05_1647():
    ChrWalkTo(0x00FE, -94380, 5550, -92900, 1500, 0x00)
    ChrWalkTo(0x00FE, -94520, 5550, -90170, 1500, 0x00)
    ChrWalkTo(0x00FE, -95150, 5550, -89860, 1500, 0x00)
    ChrSetDirection(0x00FE, 305, 400)

    Return()

# id: 0x0006 offset: 0x168B
@scena.Code('func_06_168B')
def func_06_168B():
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '◆临时入口【≡ 空贼艇内部夜用（E0110）】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F2',
    )

    NewScene('ED6_DT21/E0111._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1707')

    def _loc_16F2(): pass

    label('loc_16F2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1707',
    )

    NewScene('ED6_DT21/E0110._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1707(): pass

    label('loc_1707')

    Return()

# id: 0x0007 offset: 0x1708
@scena.Code('func_07_1708')
def func_07_1708():
    EventBegin(0x00)
    OP_DB()
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    ChrSetFlags(0x0102, 0x0080)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000F, 0x0003)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    ChrSetPos(0x000F, -99500, 0, -91500, 270)
    CameraMove(43700, -10000, 9730, 0)
    OP_67(0, 640, -10000, 0)
    CameraSetDistance(43830, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x14)
    OP_6F(0x0002, 700)
    OP_70(0x0002, 780)
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x01, 'C_VIS227._CH')
    OP_C6(0x00, 0x03, -1, 0, 0)

    @scena.Lambda('lambda_17E4')
    def lambda_17E4():
        CameraSetDistance(32830, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17E4)

    FadeIn(500, 0)
    OP_0D()
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(124, 0x00, 0x64)
    CameraMove(116270, -10000, 41470, 0)
    OP_67(0, 1020, -10000, 0)
    CameraSetDistance(18860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    MapSetFlags(0x02000000)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_AE(0x00001388)
    OP_DC()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x1870
@scena.Code('func_08_1870')
def func_08_1870():
    EventBegin(0x00)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x0005, 0x0004)
    ChrSetFlags(0x0102, 0x0080)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000D, 100000, 4000, 0, 270)
    ChrSetPos(0x000E, 100000, 4000, 0, 90)
    OP_76(0x0006, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_11(0x38, 0x44, 0x58, 20000, 1000000, 0)
    CameraMove(1000, 2700, 2800, 0)
    OP_67(0, 680, -10000, 0)
    CameraSetDistance(36240, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x1E)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0005, 0x0020)
    OP_B0(0x0005, 0x1E)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x01, 'C_VIS227._CH')
    OP_C6(0x00, 0x03, -1, 0, 0)
    FadeIn(500, 0)

    @scena.Lambda('lambda_198E')
    def lambda_198E():
        CameraSetDistance(22830, 6000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_198E)

    @scena.Lambda('lambda_199E')
    def lambda_199E():
        ChrMoveTo(0x00FE, 0, 4000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_199E)

    @scena.Lambda('lambda_19B9')
    def lambda_19B9():
        ChrMoveTo(0x00FE, 0, 4000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_19B9)

    Sleep(6400)

    FadeOut(100, 0, -1)
    OP_0D()
    Sleep(200)

    PlaySE(124, 0x00, 0x64)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000E, 0x00)
    ChrSetPos(0x000D, 10000, 4000, 0, 270)
    ChrSetPos(0x000E, 10000, 4000, 0, 270)
    CameraMove(116270, -10000, 41470, 0)
    OP_67(0, 1320, -10000, 0)
    CameraSetDistance(19860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    MapSetFlags(0x02000000)
    OP_11(0x38, 0x44, 0x58, 100000, 500000, 0)
    Sleep(400)

    @scena.Lambda('lambda_1A86')
    def lambda_1A86():
        ChrMoveTo(0x00FE, -10000, 4000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_1A86)

    @scena.Lambda('lambda_1AA1')
    def lambda_1AA1():
        ChrMoveTo(0x00FE, -10000, 4000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_1AA1)

    FadeIn(100, 0)
    OP_0D()
    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_AE(0x00001388)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x1AE2
@scena.Code('func_09_1AE2')
def func_09_1AE2():
    EventBegin(0x00)
    CameraMove(-105420, 5550, -91410, 0)
    OP_67(0, 6080, -10000, 0)
    CameraSetDistance(3470, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)
    PlaySE(451, 0x00, 0x64)
    PlaySE(121, 0x01, 0x3C)
    OP_71(0x0001, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    OP_A1(0x000F, 0x0003)
    OP_A1(0x0010, 0x0004)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    ChrSetPos(0x000F, -99500, 0, -91500, 270)
    ChrSetPos(0x0010, -99500, 0, -91500, 270)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1BA1')
    def lambda_1BA1():
        CameraMove(-95530, 5550, -92450, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1BA1)

    @scena.Lambda('lambda_1BB9')
    def lambda_1BB9():
        OP_67(0, 6080, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1BB9)

    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    OP_73(0x0001)
    CreateThread(0x0102, 0x01, 0x00, func_0A_21CA)
    Sleep(1700)

    ChrSetFlags(0x000A, 0x0004)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetPos(0x000A, -99420, 5550, -90790, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetChipByIndex(0x000A, 7)
    ChrWalkTo(0x000A, -99360, 5550, -93870, 4000, 0x00)
    ChrWalkTo(0x000A, -96560, 5550, -93310, 4000, 0x00)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 6)
    ChrSetSubChip(0x000A, 1)
    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0102, 0x0003)

    ChrTalk(
        0x0102,
        (
            '#0020320100V#1034F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C84')
    def lambda_1C84():
        CameraSetDistance(2900, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1C84)

    ChrTalk(
        0x000A,
        (
            '#0090320101V#214F到了最后的最后，\n',
            '还是个一点都不可爱的家伙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320102V还一本正经地说什么\n',
            '『这段期间谢谢你们了』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320103V#215F听到这种话，\n',
            '我一点也高兴不起来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320104V我不想听你说这种话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320105V#1033F#5P……乔丝特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0090320106V#413F……答应我啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320107V绝对不能勉强自己……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090320108V你一定要活着回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320109V#1033F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320110V#1035F我不能够\n',
            '轻易承诺你的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090320111V#417F……！………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020320112V#1031F#5P不过……有一点我可以答应你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320113V即使我的目的\n',
            '没能达成……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020320114V#1053F我也一定会活着回来，\n',
            '找个时间再次向你们道谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090320115V#414F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0003)
    Fade(250)
    ChrSetSubChip(0x000A, 1)
    OP_0D()

    @scena.Lambda('lambda_1F56')
    def lambda_1F56():
        CameraMove(-95030, 5550, -92450, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1F56)

    ChrWalkTo(0x0102, -95820, 5550, -93180, 500, 0x00)
    Sleep(500)

    ChrSetDirection(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020320116V#1031F#2P……这样可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090320117V#416F#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetSubChip(0x000A, 0)
    ChrTurnDirection(0x000A, 0x0102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0090320118V#415F#6P别忘记啦！\n',
            '这是我们约定好的哦！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_DB()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    PlaySE(121, 0x01, 0x5A)
    CameraMove(-1880, 5550, -1900, 0)
    OP_67(0, 1380, -10000, 0)
    CameraSetDistance(2680, 0)
    OP_6C(66000, 0)
    OP_6E(861, 0)
    OP_11(0x38, 0x44, 0x58, 100000, 500000, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000D, 150000, 6000, 150000, 270)
    ChrSetPos(0x000E, 150000, 6000, 150000, 270)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x1E)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0005, 0x0020)
    OP_B0(0x0005, 0x1E)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    ChrClearFlags(0x000D, 0x0100)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000D, 0, 180000, 0, 0)
    OP_D1(0x000E, 0, 180000, 0, 0)
    CreateThread(0x000D, 0x00, 0x00, func_0B_2209)
    Sleep(3800)

    PlayBGM(81)
    FadeIn(2000, 0)
    Sleep(6000)

    @scena.Lambda('lambda_2185')
    def lambda_2185():
        CameraMove(-19030, 5550, -4550, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2185)

    @scena.Lambda('lambda_219D')
    def lambda_219D():
        OP_6C(310000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_219D)

    Sleep(3200)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x21CA
@scena.Code('func_0A_21CA')
def func_0A_21CA():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -99420, 5550, -90790, 180)
    ChrWalkTo(0x00FE, -99360, 5550, -93870, 2000, 0x00)
    ChrWalkTo(0x00FE, -96090, 5550, -93260, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x2209
@scena.Code('func_0B_2209')
def func_0B_2209():
    @scena.Lambda('lambda_220F')
    def lambda_220F():
        OP_D1(0x00FE, 0, 230000, -30000, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_220F)

    @scena.Lambda('lambda_2229')
    def lambda_2229():
        OP_D1(0x00FE, 0, 230000, -30000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_2229)

    @scena.Lambda('lambda_2243')
    def lambda_2243():
        ChrMoveTo(0x00FE, 150000, 4000, 50000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2243)

    @scena.Lambda('lambda_225E')
    def lambda_225E():
        ChrMoveTo(0x00FE, 150000, 4000, 50000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_225E)

    WaitForThreadExit(0x000D, 0x0002)
    WaitForThreadExit(0x000E, 0x0002)
    CreateThread(0x000D, 0x01, 0x00, func_0C_2342)
    CreateThread(0x000E, 0x01, 0x00, func_0D_236F)

    @scena.Lambda('lambda_2291')
    def lambda_2291():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_2291)

    @scena.Lambda('lambda_22AB')
    def lambda_22AB():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_22AB)

    @scena.Lambda('lambda_22C5')
    def lambda_22C5():
        OP_97(0x00FE, 100000, 50000, 90000, 24000, 0x0000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_22C5)

    @scena.Lambda('lambda_22E1')
    def lambda_22E1():
        OP_97(0x00FE, 100000, 50000, 90000, 24000, 0x0000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_22E1)

    WaitForThreadExit(0x000D, 0x0002)
    WaitForThreadExit(0x000E, 0x0002)

    @scena.Lambda('lambda_2307')
    def lambda_2307():
        ChrMoveTo(0x00FE, -100000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2307)

    @scena.Lambda('lambda_2322')
    def lambda_2322():
        ChrMoveTo(0x00FE, -100000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2322)

    WaitForThreadExit(0x000D, 0x0002)
    WaitForThreadExit(0x000E, 0x0002)

    Return()

# id: 0x000C offset: 0x2342
@scena.Code('func_0C_2342')
def func_0C_2342():
    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2363',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x5),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_0C_2342')

    def _loc_2363(): pass

    label('loc_2363')

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x236F
@scena.Code('func_0D_236F')
def func_0D_236F():
    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2390',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x5),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_0D_236F')

    def _loc_2390(): pass

    label('loc_2390')

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0x239C
@scena.Code('func_0E_239C')
def func_0E_239C():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\mp091_00.eff')
    OP_11(0x38, 0x44, 0x58, 100000, 500000, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -20, 0, 0, 0x00, 0x00)
    ChrSetFlags(0x0102, 0x0080)
    OP_71(0x0001, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    OP_A1(0x000F, 0x0003)
    OP_A1(0x0010, 0x0004)
    ChrSetPos(0x000D, 50000, 0, 0, 270)
    ChrSetPos(0x000E, 50000, 0, 0, 270)
    ChrClearFlags(0x000D, 0x0100)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000D, 0, 270000, 0, 0)
    OP_D1(0x000E, 0, 270000, 0, 0)
    ChrSetPos(0x000F, 20000, 0, 50000, 270)
    ChrSetPos(0x0010, 20000, 0, 50000, 270)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    PlaySE(451, 0x00, 0x64)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    OP_6F(0x0003, 360)
    OP_6F(0x0004, 360)
    CameraMove(-36160, -10000, -5660, 0)
    OP_67(0, 4150, -10000, 0)
    CameraSetDistance(4740, 0)
    OP_6C(252000, 0)
    OP_6E(1357, 0)
    OP_D0(10000, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_2538')
    def lambda_2538():
        ChrMoveTo(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_2538)

    @scena.Lambda('lambda_2553')
    def lambda_2553():
        ChrMoveTo(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_2553)

    Sleep(4000)

    CreateThread(0x000F, 0x00, 0x00, func_19_38FC)
    CreateThread(0x0010, 0x00, 0x00, func_1A_3993)
    Sleep(9000)

    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(31120, -9250, -10030, 0)
    OP_67(0, 3530, -10000, 0)
    CameraSetDistance(4740, 0)
    OP_6C(96000, 0)
    OP_6E(1357, 0)
    OP_D0(340000, 0)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x0010, 0x00)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    ChrSetPos(0x000F, 60000, 7000, -30000, 270)
    ChrSetPos(0x0010, 60000, 7000, -30000, 270)
    OP_D1(0x000F, 0, 290000, -25000, 0)
    OP_D1(0x0010, 0, 290000, -25000, 0)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 360)
    OP_70(0x0003, 460)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 360)
    OP_70(0x0004, 460)
    CreateThread(0x000F, 0x00, 0x00, func_1B_3A2A)
    CreateThread(0x0010, 0x00, 0x00, func_1C_3B60)
    FadeIn(1000, 0)
    Sleep(4500)

    @scena.Lambda('lambda_2693')
    def lambda_2693():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2693)

    @scena.Lambda('lambda_26AE')
    def lambda_26AE():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_26AE)

    Sleep(100)

    @scena.Lambda('lambda_26CE')
    def lambda_26CE():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_26CE)

    @scena.Lambda('lambda_26E9')
    def lambda_26E9():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_26E9)

    Sleep(100)

    @scena.Lambda('lambda_2709')
    def lambda_2709():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2709)

    @scena.Lambda('lambda_2724')
    def lambda_2724():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2724)

    Sleep(100)

    @scena.Lambda('lambda_2744')
    def lambda_2744():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2744)

    @scena.Lambda('lambda_275F')
    def lambda_275F():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_275F)

    Sleep(100)

    @scena.Lambda('lambda_277F')
    def lambda_277F():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_277F)

    @scena.Lambda('lambda_279A')
    def lambda_279A():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_279A)

    Sleep(100)

    @scena.Lambda('lambda_27BA')
    def lambda_27BA():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_27BA)

    @scena.Lambda('lambda_27D5')
    def lambda_27D5():
        ChrMoveTo(0x00FE, -100000, 1000, -34000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_27D5)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0102, 0xFF)
    CameraMove(-49540, -6000, 10420, 0)
    OP_6C(337000, 0)
    OP_67(0, 2080, -10000, 0)
    OP_6E(1357, 0)
    CameraSetDistance(4740, 0)
    OP_D0(370000, 0)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0010, 0x01)
    ChrSetPos(0x000D, 0, -1000, 0, 270)
    ChrSetPos(0x000E, 0, -1000, 0, 270)
    OP_D1(0x000D, 0, 270000, 0, 0)
    OP_D1(0x000E, 0, 270000, 0, 0)
    ChrSetPos(0x000F, 40000, 4000, 30000, 270)
    ChrSetPos(0x0010, 40000, 4000, 30000, 270)
    OP_D1(0x000F, 0, 260000, 0, 0)
    OP_D1(0x0010, 0, 260000, 0, 0)
    CreateThread(0x000D, 0x00, 0x00, func_15_358C)
    CreateThread(0x000E, 0x00, 0x00, func_16_36CB)
    CreateThread(0x000F, 0x00, 0x00, func_1D_3C6E)
    CreateThread(0x0010, 0x00, 0x00, func_1E_3EA1)
    Sleep(300)

    FadeIn(1000, 0)
    Sleep(4700)

    @scena.Lambda('lambda_2929')
    def lambda_2929():
        CameraMove(-76150, -4350, -6420, 4400)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2929)

    @scena.Lambda('lambda_2941')
    def lambda_2941():
        OP_6C(224000, 4400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2941)

    @scena.Lambda('lambda_2951')
    def lambda_2951():
        OP_D0(350000, 4400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2951)

    @scena.Lambda('lambda_2961')
    def lambda_2961():
        OP_D1(0x00FE, 0, 270000, -15000, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_2961)

    @scena.Lambda('lambda_297B')
    def lambda_297B():
        OP_D1(0x00FE, 0, 270000, -15000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_297B)

    @scena.Lambda('lambda_2995')
    def lambda_2995():
        OP_D1(0x00FE, 0, 270000, -45000, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_2995)

    @scena.Lambda('lambda_29AF')
    def lambda_29AF():
        OP_D1(0x00FE, 0, 270000, -45000, 6000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_29AF)

    WaitForThreadExit(0x0102, 0x0000)
    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x000E, 0x01)

    @scena.Lambda('lambda_29DE')
    def lambda_29DE():
        OP_D1(0x00FE, 0, 270000, -45000, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_29DE)

    @scena.Lambda('lambda_29F8')
    def lambda_29F8():
        OP_D1(0x00FE, 0, 270000, -45000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_29F8)

    Sleep(100)

    @scena.Lambda('lambda_2A17')
    def lambda_2A17():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A17)

    @scena.Lambda('lambda_2A32')
    def lambda_2A32():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2A32)

    Sleep(100)

    @scena.Lambda('lambda_2A52')
    def lambda_2A52():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A52)

    @scena.Lambda('lambda_2A6D')
    def lambda_2A6D():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2A6D)

    Sleep(100)

    @scena.Lambda('lambda_2A8D')
    def lambda_2A8D():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A8D)

    @scena.Lambda('lambda_2AA8')
    def lambda_2AA8():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2AA8)

    Sleep(100)

    @scena.Lambda('lambda_2AC8')
    def lambda_2AC8():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2AC8)

    @scena.Lambda('lambda_2AE3')
    def lambda_2AE3():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2AE3)

    Sleep(100)

    @scena.Lambda('lambda_2B03')
    def lambda_2B03():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2B03)

    @scena.Lambda('lambda_2B1E')
    def lambda_2B1E():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2B1E)

    Sleep(100)

    @scena.Lambda('lambda_2B3E')
    def lambda_2B3E():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2B3E)

    @scena.Lambda('lambda_2B59')
    def lambda_2B59():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2B59)

    Sleep(100)

    @scena.Lambda('lambda_2B79')
    def lambda_2B79():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2B79)

    @scena.Lambda('lambda_2B94')
    def lambda_2B94():
        ChrMoveTo(0x00FE, -190000, 4000, 80000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2B94)

    Sleep(2000)

    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000D, 0x03)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000E, 0x03)
    ChrSetPos(0x000D, -200000, -2000, 110000, 270)
    ChrSetPos(0x000E, -200000, -2000, 110000, 270)
    OP_D1(0x000D, 0, 270000, 10000, 0)
    OP_D1(0x000E, 0, 270000, 10000, 0)
    Sleep(2000)

    Fade(1000)
    CameraMove(-223070, -10000, 89110, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6C(273000, 0)
    OP_D0(370000, 0)
    OP_0D()
    CreateThread(0x0102, 0x00, 0x00, func_0F_32B3)
    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x000F, 0x0001)
    TerminateThread(0x0102, 0x00)
    OP_89(0x0102, -187360, 5630, 81990, 316)
    Fade(1000)
    CameraMove(-187360, 5630, 81990, 0)
    OP_67(0, 3240, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(174000, 0)
    OP_6E(429, 0)
    OP_D0(360000, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0102,
        (
            '#0020320134V#1035F#6P#40W…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraSetDistance(2000, 500)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020320135V#1032F#6P好……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_DB()

    @scena.Lambda('lambda_2D5C')
    def lambda_2D5C():
        CameraMove(-192600, 5630, 84510, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2D5C)

    @scena.Lambda('lambda_2D74')
    def lambda_2D74():
        OP_67(0, 2960, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2D74)

    @scena.Lambda('lambda_2D8C')
    def lambda_2D8C():
        OP_6C(248000, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2D8C)

    @scena.Lambda('lambda_2D9C')
    def lambda_2D9C():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2D9C)

    WaitForThreadExit(0x000A, 0x0000)
    ChrSetChipByIndex(0x0102, 26)
    ChrSetSubChip(0x0102, 0)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0102, 0x0002)

    @scena.Lambda('lambda_2DC5')
    def lambda_2DC5():
        OP_99(0x00FE, 0x00, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2DC5)

    ChrWalkTo(0x0102, -190310, 5630, 82480, 10000, 0x00)
    TerminateThread(0x0102, 0x01)
    ChrSetChipByIndex(0x0102, 26)
    ChrSetSubChip(0x0102, 8)
    Sleep(200)

    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x01F4)
    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_2E0E')
    def lambda_2E0E():
        OP_99(0x00FE, 0x08, 0x0A, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E0E)

    @scena.Lambda('lambda_2E1E')
    def lambda_2E1E():
        ChrJumpTo(0x00FE, -192520, 5330, 86470, 1250, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2E1E)

    PlaySE(163, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_2E46')
    def lambda_2E46():
        OP_99(0x00FE, 0x10, 0x12, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E46)

    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0102, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_2E65')
    def lambda_2E65():
        OP_D1(0x00FE, 0, 270000, -4000, 100)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_2E65)

    @scena.Lambda('lambda_2E7F')
    def lambda_2E7F():
        OP_D1(0x00FE, 0, 270000, -4000, 100)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_2E7F)

    ChrSetPos(0x0102, -193320, 5330, 86470, 316)
    ChrSetChipByIndex(0x0102, 26)
    ChrSetSubChip(0x0102, 8)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2EBE')
    def lambda_2EBE():
        OP_D1(0x00FE, 0, 270000, 2000, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_2EBE)

    @scena.Lambda('lambda_2ED8')
    def lambda_2ED8():
        OP_D1(0x00FE, 0, 270000, 2000, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_2ED8)

    @scena.Lambda('lambda_2EF2')
    def lambda_2EF2():
        OP_99(0x00FE, 0x09, 0x0A, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2EF2)

    @scena.Lambda('lambda_2F02')
    def lambda_2F02():
        ChrJumpTo(0x00FE, -206490, 3530, 109410, 3000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2F02)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x00000010)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x0102, 0x03)
    ChrClearBattleFlags(0x0102, 0x0020)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    ChrSetPos(0x000D, 136000, 1000, 50000, 270)
    ChrSetPos(0x000E, 136000, 1000, 50000, 270)
    OP_D1(0x000D, 0, 260000, 10000, 0)
    OP_D1(0x000E, 0, 260000, 10000, 0)
    ChrSetPos(0x0102, 0, 5000, 0, 270)
    ChrSetPos(0x0019, -350, 5900, 0, 270)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x001A, -24650, 5900, 0, 270)
    ChrClearFlags(0x001A, 0x0080)
    CameraMove(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    CameraSetDistance(1500, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)
    FadeIn(1000, 0)
    CreateThread(0x0102, 0x00, 0x00, func_12_33F9)

    @scena.Lambda('lambda_3031')
    def lambda_3031():
        OP_9E(0x00FE, 10, 10, 5000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3031)

    @scena.Lambda('lambda_304B')
    def lambda_304B():
        CameraSetDistance(3260, 3750)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_304B)

    @scena.Lambda('lambda_305B')
    def lambda_305B():
        CameraMove(-10900, 5000, -1600, 3750)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_305B)

    @scena.Lambda('lambda_3073')
    def lambda_3073():
        OP_67(0, 2040, -10000, 3750)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3073)

    @scena.Lambda('lambda_308B')
    def lambda_308B():
        OP_6C(246000, 3750)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_308B)

    @scena.Lambda('lambda_309B')
    def lambda_309B():
        ChrMoveTo(0x00FE, -364000, 1000, -100000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_309B)

    @scena.Lambda('lambda_30B6')
    def lambda_30B6():
        ChrMoveTo(0x00FE, -364000, 1000, -100000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_30B6)

    Sleep(2500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    StopEffect(0x01, 0x00)
    Fade(500)
    PlaySE(214, 0x00, 0x64)
    TerminateThread(0x0102, 0xFF)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetFlags(0x0102, 0x8000)
    ChrSetChipByIndex(0x0102, 25)
    ChrSetSubChip(0x0102, 0)
    ChrSetDirection(0x0102, 270, 0)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)
    ChrSetPos(0x0019, 100000, 0, 0, 270)
    ChrSetPos(0x001A, 101000, 0, 0, 270)
    CreateThread(0x0102, 0x00, 0x00, func_11_3357)
    PlayEffect(0x01, 0x01, 0x0019, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    OP_D1(0x000D, 0, 270000, 10000, 0)
    OP_D1(0x000E, 0, 270000, 10000, 0)
    ChrSetPos(0x000D, 40000, 1000, 0, 270)
    ChrSetPos(0x000E, 40000, 1000, 0, 270)
    CameraMove(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    CameraSetDistance(2100, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)

    @scena.Lambda('lambda_31FB')
    def lambda_31FB():
        ChrMoveTo(0x00FE, -400000, 1000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_31FB)

    @scena.Lambda('lambda_3216')
    def lambda_3216():
        ChrMoveTo(0x00FE, -400000, 1000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3216)

    @scena.Lambda('lambda_3231')
    def lambda_3231():
        CameraMove(2880, 10000, 6720, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_3231)

    @scena.Lambda('lambda_3249')
    def lambda_3249():
        OP_67(0, 1320, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3249)

    @scena.Lambda('lambda_3261')
    def lambda_3261():
        OP_6C(268000, 4500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3261)

    Sleep(15)

    WaitForThreadExit(0x000A, 0x0002)
    FadeOut(2000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0102, 0x8000)
    StopEffect(0x01, 0x00)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    OP_DC()
    MapSetFlags(0x02000000)
    MapSetFlags(0x00000010)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0110._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x32B3
@scena.Code('func_0F_32B3')
def func_0F_32B3():
    ChrSetChipByIndex(0x0102, 5)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0102, 0x0001)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetBattleFlags(0x0102, 0x0020)
    ChrSetDirection(0x0102, 316, 0)
    def _loc_32D3(): pass

    label('loc_32D3')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3314',
    )

    ExecExpressionWithValue(
        0x0102,
        0x01,
        (
            (Expr.GetChrWork, 0xF, 0x1),
            (Expr.PushLong, 0xA50),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x02,
        (
            (Expr.GetChrWork, 0xF, 0x2),
            (Expr.PushLong, 0x15FE),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x03,
        (
            (Expr.GetChrWork, 0xF, 0x3),
            (Expr.PushLong, 0x7C6),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('loc_32D3')

    def _loc_3314(): pass

    label('loc_3314')

    Return()

# id: 0x0010 offset: 0x3315
@scena.Code('func_10_3315')
def func_10_3315():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3356',
    )

    ExecExpressionWithValue(
        0x0102,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.PushLong, 0xC1C),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.PushLong, 0x988),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.PushLong, 0xBCC),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_10_3315')

    def _loc_3356(): pass

    label('loc_3356')

    Return()

# id: 0x0011 offset: 0x3357
@scena.Code('func_11_3357')
def func_11_3357():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33F8',
    )

    ExecExpressionWithValue(
        0x0102,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.PushLong, 0x9C4),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.PushLong, 0x5DC),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.PushLong, 0x5DC),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x01,
        (
            (Expr.GetChrWork, 0xD, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x02,
        (
            (Expr.GetChrWork, 0xD, 0x2),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x03,
        (
            (Expr.GetChrWork, 0xD, 0x3),
            (Expr.PushLong, 0x5DC),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_11_3357')

    def _loc_33F8(): pass

    label('loc_33F8')

    Return()

# id: 0x0012 offset: 0x33F9
@scena.Code('func_12_33F9')
def func_12_33F9():
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    OP_99(0x0102, 0x14, 0x17, 2000)
    ChrSetSubChip(0x0102, 12)
    Sleep(200)

    PlaySE(132, 0x00, 0x64)
    ChrSetSubChip(0x0102, 13)
    PlayEffect(0x01, 0x01, 0x0019, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    Sleep(80)

    ChrSetSubChip(0x0102, 14)
    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x00C8)

    Return()

# id: 0x0013 offset: 0x34B8
@scena.Code('func_13_34B8')
def func_13_34B8():
    Sleep(500)

    ChrMoveTo(0x00FE, -44160, 0, 21930, 20000, 0x00)
    ChrMoveTo(0x00FE, -80160, -5000, 1680, 20000, 0x00)
    ChrMoveTo(0x00FE, -120160, -10000, 33480, 18000, 0x00)
    ChrMoveTo(0x00FE, -160160, -5000, 12480, 16000, 0x00)
    ChrMoveTo(0x00FE, -200160, 2000, 1480, 14000, 0x00)

    Return()

# id: 0x0014 offset: 0x3522
@scena.Code('func_14_3522')
def func_14_3522():
    Sleep(500)

    ChrMoveTo(0x00FE, -44160, 0, 21930, 20000, 0x00)
    ChrMoveTo(0x00FE, -80160, -5000, 1680, 20000, 0x00)
    ChrMoveTo(0x00FE, -120160, -10000, 33480, 18000, 0x00)
    ChrMoveTo(0x00FE, -160160, -5000, 12480, 16000, 0x00)
    ChrMoveTo(0x00FE, -200160, 2000, 1480, 14000, 0x00)

    Return()

# id: 0x0015 offset: 0x358C
@scena.Code('func_15_358C')
def func_15_358C():
    @scena.Lambda('lambda_3592')
    def lambda_3592():
        OP_D1(0x00FE, 0, 270000, 60000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3592)

    @scena.Lambda('lambda_35AC')
    def lambda_35AC():
        OP_97(0x00FE, -40000, 0, -180000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_35AC)

    Sleep(400)

    @scena.Lambda('lambda_35CD')
    def lambda_35CD():
        OP_97(0x00FE, -40000, 0, -180000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_35CD)

    Sleep(300)

    @scena.Lambda('lambda_35EE')
    def lambda_35EE():
        OP_97(0x00FE, -40000, 0, -180000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_35EE)

    Sleep(200)

    @scena.Lambda('lambda_360F')
    def lambda_360F():
        OP_97(0x00FE, -40000, 0, -180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_360F)

    Sleep(100)

    @scena.Lambda('lambda_3630')
    def lambda_3630():
        OP_97(0x00FE, -40000, 0, -180000, 22000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3630)

    Sleep(4600)

    @scena.Lambda('lambda_3651')
    def lambda_3651():
        OP_97(0x00FE, -40000, 0, -180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3651)

    Sleep(300)

    @scena.Lambda('lambda_3672')
    def lambda_3672():
        OP_97(0x00FE, -40000, 0, -180000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3672)

    Sleep(200)

    @scena.Lambda('lambda_3693')
    def lambda_3693():
        OP_97(0x00FE, -40000, 0, -180000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3693)

    Sleep(100)

    @scena.Lambda('lambda_36B4')
    def lambda_36B4():
        OP_97(0x00FE, -40000, 0, -180000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_36B4)

    Return()

# id: 0x0016 offset: 0x36CB
@scena.Code('func_16_36CB')
def func_16_36CB():
    @scena.Lambda('lambda_36D1')
    def lambda_36D1():
        OP_D1(0x00FE, 0, 270000, 60000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_36D1)

    @scena.Lambda('lambda_36EB')
    def lambda_36EB():
        OP_97(0x00FE, -40000, 0, -180000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_36EB)

    Sleep(400)

    @scena.Lambda('lambda_370C')
    def lambda_370C():
        OP_97(0x00FE, -40000, 0, -180000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_370C)

    Sleep(300)

    @scena.Lambda('lambda_372D')
    def lambda_372D():
        OP_97(0x00FE, -40000, 0, -180000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_372D)

    Sleep(200)

    @scena.Lambda('lambda_374E')
    def lambda_374E():
        OP_97(0x00FE, -40000, 0, -180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_374E)

    Sleep(100)

    @scena.Lambda('lambda_376F')
    def lambda_376F():
        OP_97(0x00FE, -40000, 0, -180000, 22000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_376F)

    Sleep(4600)

    @scena.Lambda('lambda_3790')
    def lambda_3790():
        OP_97(0x00FE, -40000, 0, -180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3790)

    Sleep(300)

    @scena.Lambda('lambda_37B1')
    def lambda_37B1():
        OP_97(0x00FE, -40000, 0, -180000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_37B1)

    Sleep(200)

    @scena.Lambda('lambda_37D2')
    def lambda_37D2():
        OP_97(0x00FE, -40000, 0, -180000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_37D2)

    Sleep(100)

    @scena.Lambda('lambda_37F3')
    def lambda_37F3():
        OP_97(0x00FE, -40000, 0, -180000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_37F3)

    Return()

# id: 0x0017 offset: 0x380A
@scena.Code('func_17_380A')
def func_17_380A():
    ChrMoveTo(0x00FE, 24300, 0, 33480, 20000, 0x00)
    ChrMoveTo(0x00FE, -44160, 0, 21930, 20000, 0x00)
    ChrMoveTo(0x00FE, -80160, 0, 1680, 20000, 0x00)
    ChrMoveTo(0x00FE, -120160, -5000, 33480, 20000, 0x00)
    ChrMoveTo(0x00FE, -160160, 0, 16480, 20000, 0x00)
    ChrMoveTo(0x00FE, -195160, -12000, 3480, 20000, 0x00)

    Return()

# id: 0x0018 offset: 0x3883
@scena.Code('func_18_3883')
def func_18_3883():
    ChrMoveTo(0x00FE, 24300, 0, 33480, 20000, 0x00)
    ChrMoveTo(0x00FE, -44160, 0, 21930, 20000, 0x00)
    ChrMoveTo(0x00FE, -80160, 0, 1680, 20000, 0x00)
    ChrMoveTo(0x00FE, -120160, -5000, 33480, 20000, 0x00)
    ChrMoveTo(0x00FE, -160160, 0, 16480, 20000, 0x00)
    ChrMoveTo(0x00FE, -195160, -12000, 3480, 20000, 0x00)

    Return()

# id: 0x0019 offset: 0x38FC
@scena.Code('func_19_38FC')
def func_19_38FC():
    ChrMoveTo(0x00FE, 0, 0, 20000, 14000, 0x00)
    OP_98(0x00, 0x00FE)
    OP_98(0x01, -40000, 0, -40000)
    OP_98(0x01, -120000, 0, 0)

    @scena.Lambda('lambda_3936')
    def lambda_3936():
        OP_98(0x02, 0x00FE, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3936)

    @scena.Lambda('lambda_3946')
    def lambda_3946():
        OP_D1(0x00FE, 0, 270000, 15000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3946)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_3965')
    def lambda_3965():
        OP_D1(0x00FE, 0, 270000, -25000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3965)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, -300000, 0, 20000, 14000, 0x00)

    Return()

# id: 0x001A offset: 0x3993
@scena.Code('func_1A_3993')
def func_1A_3993():
    ChrMoveTo(0x00FE, 0, 0, 20000, 14000, 0x00)
    OP_98(0x00, 0x00FE)
    OP_98(0x01, -40000, 0, -40000)
    OP_98(0x01, -120000, 0, 0)

    @scena.Lambda('lambda_39CD')
    def lambda_39CD():
        OP_98(0x02, 0x00FE, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_39CD)

    @scena.Lambda('lambda_39DD')
    def lambda_39DD():
        OP_D1(0x00FE, 0, 270000, 15000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_39DD)

    WaitForThreadExit(0x000F, 0x0003)

    @scena.Lambda('lambda_39FC')
    def lambda_39FC():
        OP_D1(0x00FE, 0, 270000, -25000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_39FC)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveTo(0x00FE, -300000, 0, 20000, 14000, 0x00)

    Return()

# id: 0x001B offset: 0x3A2A
@scena.Code('func_1B_3A2A')
def func_1B_3A2A():
    OP_98(0x00, 0x00FE)
    OP_98(0x01, 35000, 3000, -20000)
    OP_98(0x01, 30000, 1000, 24000)

    @scena.Lambda('lambda_3A50')
    def lambda_3A50():
        OP_98(0x02, 0x00FE, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3A50)

    Sleep(2000)

    @scena.Lambda('lambda_3A65')
    def lambda_3A65():
        OP_D1(0x00FE, 6000, 240000, 25000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3A65)

    @scena.Lambda('lambda_3A7F')
    def lambda_3A7F():
        CameraMove(29550, -10000, -1500, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_3A7F)

    @scena.Lambda('lambda_3A97')
    def lambda_3A97():
        OP_D0(370000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A97)

    WaitForThreadExit(0x00FE, 0x0003)
    TerminateThread(0x00FE, 0x01)

    @scena.Lambda('lambda_3AB0')
    def lambda_3AB0():
        OP_D1(0x00FE, 6000, 240000, 45000, 2500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3AB0)

    @scena.Lambda('lambda_3ACA')
    def lambda_3ACA():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3ACA)

    Sleep(100)

    @scena.Lambda('lambda_3AEA')
    def lambda_3AEA():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3AEA)

    Sleep(100)

    @scena.Lambda('lambda_3B0A')
    def lambda_3B0A():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B0A)

    Sleep(100)

    @scena.Lambda('lambda_3B2A')
    def lambda_3B2A():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B2A)

    Sleep(100)

    @scena.Lambda('lambda_3B4A')
    def lambda_3B4A():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B4A)

    Return()

# id: 0x001C offset: 0x3B60
@scena.Code('func_1C_3B60')
def func_1C_3B60():
    OP_98(0x00, 0x00FE)
    OP_98(0x01, 35000, 3000, -20000)
    OP_98(0x01, 30000, 1000, 24000)

    @scena.Lambda('lambda_3B86')
    def lambda_3B86():
        OP_98(0x02, 0x00FE, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B86)

    Sleep(2000)

    @scena.Lambda('lambda_3B9B')
    def lambda_3B9B():
        OP_D1(0x00FE, 6000, 240000, 25000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3B9B)

    WaitForThreadExit(0x00FE, 0x0003)
    TerminateThread(0x00FE, 0x01)

    @scena.Lambda('lambda_3BBE')
    def lambda_3BBE():
        OP_D1(0x00FE, 6000, 240000, 45000, 2500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3BBE)

    @scena.Lambda('lambda_3BD8')
    def lambda_3BD8():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3BD8)

    Sleep(100)

    @scena.Lambda('lambda_3BF8')
    def lambda_3BF8():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3BF8)

    Sleep(100)

    @scena.Lambda('lambda_3C18')
    def lambda_3C18():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C18)

    Sleep(100)

    @scena.Lambda('lambda_3C38')
    def lambda_3C38():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C38)

    Sleep(100)

    @scena.Lambda('lambda_3C58')
    def lambda_3C58():
        ChrMoveTo(0x00FE, -100000, 9000, -41000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C58)

    Return()

# id: 0x001D offset: 0x3C6E
@scena.Code('func_1D_3C6E')
def func_1D_3C6E():
    @scena.Lambda('lambda_3C74')
    def lambda_3C74():
        OP_97(0x00FE, -10000, 20000, -260000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C74)

    Sleep(400)

    @scena.Lambda('lambda_3C95')
    def lambda_3C95():
        OP_97(0x00FE, -10000, 20000, -260000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C95)

    Sleep(300)

    @scena.Lambda('lambda_3CB6')
    def lambda_3CB6():
        OP_97(0x00FE, -10000, 20000, -260000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3CB6)

    Sleep(200)

    @scena.Lambda('lambda_3CD7')
    def lambda_3CD7():
        OP_97(0x00FE, -10000, 20000, -260000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3CD7)

    Sleep(100)

    @scena.Lambda('lambda_3CF8')
    def lambda_3CF8():
        OP_D1(0x00FE, 0, 270000, 60000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3CF8)

    @scena.Lambda('lambda_3D12')
    def lambda_3D12():
        OP_97(0x00FE, -10000, 20000, -260000, 22000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D12)

    Sleep(7500)

    @scena.Lambda('lambda_3D33')
    def lambda_3D33():
        OP_97(0x00FE, -70000, 0, 180000, 18000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D33)

    Sleep(200)

    @scena.Lambda('lambda_3D54')
    def lambda_3D54():
        OP_97(0x00FE, -70000, 0, 180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D54)

    Sleep(200)

    @scena.Lambda('lambda_3D75')
    def lambda_3D75():
        OP_97(0x00FE, -70000, 0, 180000, 12000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D75)

    Sleep(2000)

    @scena.Lambda('lambda_3D96')
    def lambda_3D96():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3D96)

    @scena.Lambda('lambda_3DB0')
    def lambda_3DB0():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 13800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DB0)

    Sleep(100)

    @scena.Lambda('lambda_3DD0')
    def lambda_3DD0():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 14800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DD0)

    Sleep(100)

    @scena.Lambda('lambda_3DF0')
    def lambda_3DF0():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 16800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DF0)

    Sleep(100)

    @scena.Lambda('lambda_3E10')
    def lambda_3E10():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 18800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3E10)

    Sleep(100)

    @scena.Lambda('lambda_3E30')
    def lambda_3E30():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 21800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3E30)

    Sleep(100)

    @scena.Lambda('lambda_3E50')
    def lambda_3E50():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3E50)

    Sleep(4600)

    @scena.Lambda('lambda_3E70')
    def lambda_3E70():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3E70)

    @scena.Lambda('lambda_3E8B')
    def lambda_3E8B():
        ChrMoveTo(0x00FE, -190000, -2000, 100000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3E8B)

    Return()

# id: 0x001E offset: 0x3EA1
@scena.Code('func_1E_3EA1')
def func_1E_3EA1():
    @scena.Lambda('lambda_3EA7')
    def lambda_3EA7():
        OP_97(0x00FE, -10000, 20000, -260000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3EA7)

    Sleep(400)

    @scena.Lambda('lambda_3EC8')
    def lambda_3EC8():
        OP_97(0x00FE, -10000, 20000, -260000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3EC8)

    Sleep(300)

    @scena.Lambda('lambda_3EE9')
    def lambda_3EE9():
        OP_97(0x00FE, -10000, 20000, -260000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3EE9)

    Sleep(200)

    @scena.Lambda('lambda_3F0A')
    def lambda_3F0A():
        OP_97(0x00FE, -10000, 20000, -260000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3F0A)

    Sleep(100)

    @scena.Lambda('lambda_3F2B')
    def lambda_3F2B():
        OP_D1(0x00FE, 0, 270000, 60000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3F2B)

    @scena.Lambda('lambda_3F45')
    def lambda_3F45():
        OP_97(0x00FE, -10000, 20000, -260000, 22000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3F45)

    Sleep(7500)

    @scena.Lambda('lambda_3F66')
    def lambda_3F66():
        OP_97(0x00FE, -70000, 0, 180000, 18000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3F66)

    Sleep(200)

    @scena.Lambda('lambda_3F87')
    def lambda_3F87():
        OP_97(0x00FE, -70000, 0, 180000, 14000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3F87)

    Sleep(200)

    @scena.Lambda('lambda_3FA8')
    def lambda_3FA8():
        OP_97(0x00FE, -70000, 0, 180000, 12000, 0x0000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3FA8)

    Sleep(2000)

    @scena.Lambda('lambda_3FC9')
    def lambda_3FC9():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3FC9)

    @scena.Lambda('lambda_3FE3')
    def lambda_3FE3():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 13800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3FE3)

    Sleep(100)

    @scena.Lambda('lambda_4003')
    def lambda_4003():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 14800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4003)

    Sleep(100)

    @scena.Lambda('lambda_4023')
    def lambda_4023():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 16800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4023)

    Sleep(100)

    @scena.Lambda('lambda_4043')
    def lambda_4043():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 18800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4043)

    Sleep(100)

    @scena.Lambda('lambda_4063')
    def lambda_4063():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 21800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4063)

    Sleep(100)

    @scena.Lambda('lambda_4083')
    def lambda_4083():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4083)

    Sleep(4600)

    @scena.Lambda('lambda_40A3')
    def lambda_40A3():
        ChrMoveTo(0x00FE, -190000, 0, 80000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_40A3)

    @scena.Lambda('lambda_40BE')
    def lambda_40BE():
        ChrMoveTo(0x00FE, -190000, -2000, 100000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_40BE)

    Return()

# id: 0x001F offset: 0x40D4
@scena.Code('func_1F_40D4')
def func_1F_40D4():
    EventBegin(0x00)
    OP_DB()
    OP_11(0x38, 0x44, 0x58, 100000, 500000, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    ChrSetFlags(0x0102, 0x0080)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    OP_A1(0x000F, 0x0003)
    OP_A1(0x0010, 0x0004)
    ChrSetPos(0x000D, 0, 3000, 0, 270)
    ChrSetPos(0x000E, 0, 3000, 0, 270)
    ChrClearFlags(0x000D, 0x0100)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000D, 0, 270000, 0, 0)
    OP_D1(0x000E, 0, 270000, 0, 0)
    ChrSetPos(0x000F, 110000, 4000, -20000, 270)
    ChrSetPos(0x0010, 110000, 4000, -20000, 270)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_71(0x0001, 0x0004)
    PlaySE(451, 0x00, 0x64)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 360)
    OP_70(0x0003, 460)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 360)
    OP_70(0x0004, 460)
    CameraMove(42110, -10000, -9480, 0)
    OP_67(0, 3620, -10000, 0)
    CameraSetDistance(7610, 0)
    OP_6C(105000, 0)
    OP_6E(1076, 0)
    OP_D0(370000, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_4275')
    def lambda_4275():
        ChrMoveTo(0x00FE, 100000, 4000, -20000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_4275)

    @scena.Lambda('lambda_4290')
    def lambda_4290():
        ChrMoveTo(0x00FE, 100000, 4000, -20000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_4290)

    WaitForThreadExit(0x000F, 0x0000)

    @scena.Lambda('lambda_42B0')
    def lambda_42B0():
        CameraMove(21040, -10000, 44720, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_42B0)

    @scena.Lambda('lambda_42C8')
    def lambda_42C8():
        OP_67(0, 3620, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_42C8)

    @scena.Lambda('lambda_42E0')
    def lambda_42E0():
        OP_6C(24000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_42E0)

    @scena.Lambda('lambda_42F0')
    def lambda_42F0():
        OP_D0(360000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_42F0)

    CreateThread(0x000F, 0x00, 0x00, func_20_43CD)
    CreateThread(0x0010, 0x00, 0x00, func_21_442B)
    CreateThread(0x000F, 0x01, 0x00, func_22_4489)
    CreateThread(0x0010, 0x01, 0x00, func_23_44B6)
    OP_12(0x000186A0, 0x000493E0, 0x00002710)
    Sleep(1000)

    @scena.Lambda('lambda_432E')
    def lambda_432E():
        OP_D1(0x00FE, 0, 260000, 30000, 2400)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_432E)

    @scena.Lambda('lambda_4348')
    def lambda_4348():
        OP_D1(0x00FE, 0, 260000, 30000, 2400)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4348)

    WaitForThreadExit(0x000D, 0x0003)

    @scena.Lambda('lambda_4367')
    def lambda_4367():
        OP_D1(0x00FE, 0, 270000, 15000, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_4367)

    @scena.Lambda('lambda_4381')
    def lambda_4381():
        OP_D1(0x00FE, 0, 270000, 15000, 5000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4381)

    @scena.Lambda('lambda_439B')
    def lambda_439B():
        CameraSetDistance(9610, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_439B)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x43CD
@scena.Code('func_20_43CD')
def func_20_43CD():
    @scena.Lambda('lambda_43D3')
    def lambda_43D3():
        OP_D1(0x00FE, 0, 290000, -40000, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_43D3)

    OP_97(0x00FE, 100000, 50000, 90000, 24000, 0x0000)

    @scena.Lambda('lambda_4402')
    def lambda_4402():
        OP_D1(0x00FE, 0, 310000, 0, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4402)

    ChrMoveTo(0x00FE, -20000, 20000, 300000, 24000, 0x00)

    Return()

# id: 0x0021 offset: 0x442B
@scena.Code('func_21_442B')
def func_21_442B():
    @scena.Lambda('lambda_4431')
    def lambda_4431():
        OP_D1(0x00FE, 0, 290000, -40000, 3500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4431)

    OP_97(0x00FE, 100000, 50000, 90000, 24000, 0x0000)

    @scena.Lambda('lambda_4460')
    def lambda_4460():
        OP_D1(0x00FE, 0, 310000, 0, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4460)

    ChrMoveTo(0x00FE, -20000, 20000, 300000, 24000, 0x00)

    Return()

# id: 0x0022 offset: 0x4489
@scena.Code('func_22_4489')
def func_22_4489():
    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x7D0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_44AA',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xF),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_22_4489')

    def _loc_44AA(): pass

    label('loc_44AA')

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0023 offset: 0x44B6
@scena.Code('func_23_44B6')
def func_23_44B6():
    If(
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.PushLong, 0x7D0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_44D7',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0xF),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(15)

    Jump('func_23_44B6')

    def _loc_44D7(): pass

    label('loc_44D7')

    ExecExpressionWithValue(
        0x00FE,
        0x02,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0024 offset: 0x44E3
@scena.Code('func_24_44E3')
def func_24_44E3():
    EventBegin(0x00)
    OP_DB()
    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetPos(0x0102, 6180, 15930, 17690, 0)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_A1(0x000D, 0x0002)
    ChrSetPos(0x000D, 4780, 14000, 10550, 45)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 700)
    OP_70(0x0002, 780)
    CameraMove(6550, 15930, 18080, 0)
    OP_67(0, 6750, -10000, 0)
    CameraSetDistance(2780, 0)
    OP_6C(124000, 0)
    OP_6E(438, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_458A')
    def lambda_458A():
        CameraMove(7530, 15930, 13960, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_458A)

    @scena.Lambda('lambda_45A2')
    def lambda_45A2():
        OP_67(0, 6750, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_45A2)

    OP_6E(778, 4000)

    @scena.Lambda('lambda_45C3')
    def lambda_45C3():
        CameraMove(-53670, 15930, -95210, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_45C3)

    @scena.Lambda('lambda_45DB')
    def lambda_45DB():
        OP_67(0, 5450, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_45DB)

    @scena.Lambda('lambda_45F3')
    def lambda_45F3():
        CameraSetDistance(4780, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_45F3)

    @scena.Lambda('lambda_4603')
    def lambda_4603():
        OP_6C(67000, 5000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4603)

    @scena.Lambda('lambda_4613')
    def lambda_4613():
        OP_6E(834, 10000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_4613)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0025 offset: 0x464E
@scena.Code('func_25_464E')
def func_25_464E():
    EventBegin(0x00)
    OP_DB()
    OP_11(0x38, 0x44, 0x58, 100000, 500000, 0)
    OP_76(0x0006, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000D, 0, 0, 0, 270)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    ChrClearFlags(0x000D, 0x0100)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000D, 0, 270000, 0, 0)
    OP_D1(0x000E, 0, 270000, 0, 0)
    PlaySE(451, 0x00, 0x64)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x28)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0005, 0x0020)
    OP_B0(0x0005, 0x28)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    ChrSetChipByIndex(0x0102, 5)
    ChrSetSubChip(0x0102, 6)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0102, 0x0001)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetBattleFlags(0x0102, 0x0020)
    ChrSetPos(0x0102, 810, 3380, -2950, 180)
    CameraMove(-6990, 3340, -40, 0)
    OP_67(0, 1430, -10000, 0)
    CameraSetDistance(2760, 0)
    OP_6C(100000, 0)
    OP_6E(438, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_47A1')
    def lambda_47A1():
        CameraMove(-7310, 3340, 410, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_47A1)

    @scena.Lambda('lambda_47B9')
    def lambda_47B9():
        OP_6C(300000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_47B9)

    @scena.Lambda('lambda_47C9')
    def lambda_47C9():
        CameraSetDistance(2260, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_47C9)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    ChrSetChipByIndex(0x0102, 5)
    ChrSetSubChip(0x0102, 1)
    WaitForThreadExit(0x0102, 0x0000)
    Sleep(1000)

    CreateThread(0x000D, 0x00, 0x00, func_26_483F)

    @scena.Lambda('lambda_4803')
    def lambda_4803():
        OP_6C(280000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4803)

    Sleep(3000)

    ChrSetChipByIndex(0x0102, 5)
    ChrSetSubChip(0x0102, 2)
    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0026 offset: 0x483F
@scena.Code('func_26_483F')
def func_26_483F():
    @scena.Lambda('lambda_4845')
    def lambda_4845():
        ChrMoveTo(0x00FE, -200000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4845)

    @scena.Lambda('lambda_4860')
    def lambda_4860():
        ChrMoveTo(0x00FE, -200000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4860)

    Sleep(400)

    @scena.Lambda('lambda_4880')
    def lambda_4880():
        ChrMoveTo(0x00FE, -200000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4880)

    @scena.Lambda('lambda_489B')
    def lambda_489B():
        ChrMoveTo(0x00FE, -200000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_489B)

    Sleep(400)

    @scena.Lambda('lambda_48BB')
    def lambda_48BB():
        ChrMoveTo(0x00FE, -200000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_48BB)

    @scena.Lambda('lambda_48D6')
    def lambda_48D6():
        ChrMoveTo(0x00FE, -200000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_48D6)

    Sleep(300)

    @scena.Lambda('lambda_48F6')
    def lambda_48F6():
        ChrMoveTo(0x00FE, -200000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_48F6)

    @scena.Lambda('lambda_4911')
    def lambda_4911():
        ChrMoveTo(0x00FE, -200000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4911)

    Sleep(300)

    @scena.Lambda('lambda_4931')
    def lambda_4931():
        ChrMoveTo(0x00FE, -200000, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4931)

    @scena.Lambda('lambda_494C')
    def lambda_494C():
        ChrMoveTo(0x00FE, -200000, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_494C)

    Sleep(200)

    @scena.Lambda('lambda_496C')
    def lambda_496C():
        ChrMoveTo(0x00FE, -200000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_496C)

    @scena.Lambda('lambda_4987')
    def lambda_4987():
        ChrMoveTo(0x00FE, -200000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4987)

    Sleep(200)

    @scena.Lambda('lambda_49A7')
    def lambda_49A7():
        ChrMoveTo(0x00FE, -200000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_49A7)

    @scena.Lambda('lambda_49C2')
    def lambda_49C2():
        ChrMoveTo(0x00FE, -200000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_49C2)

    Sleep(100)

    @scena.Lambda('lambda_49E2')
    def lambda_49E2():
        ChrMoveTo(0x00FE, -200000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_49E2)

    @scena.Lambda('lambda_49FD')
    def lambda_49FD():
        ChrMoveTo(0x00FE, -200000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_49FD)

    Sleep(100)

    @scena.Lambda('lambda_4A1D')
    def lambda_4A1D():
        ChrMoveTo(0x00FE, -200000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4A1D)

    @scena.Lambda('lambda_4A38')
    def lambda_4A38():
        ChrMoveTo(0x00FE, -200000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A38)

    Return()

# id: 0x0027 offset: 0x4A4E
@scena.Code('func_27_4A4E')
def func_27_4A4E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A73',
    )

    Call(0, 0x0036)
    Call(0, 0x0037)
    FormationDelMember(0x00, 0xFF)

    def _loc_4A73(): pass

    label('loc_4A73')

    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    CameraMove(220, -15000, 60940, 0)
    OP_67(0, -3800, -10000, 0)
    CameraSetDistance(1220, 0)
    OP_6C(0, 0)
    OP_6E(667, 0)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_A1(0x000D, 0x0002)
    ChrSetPos(0x000D, -38450, -5000, 63740, 45)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 680)
    OP_70(0x0002, 780)
    OP_72(0x0005, 0x0004)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, -38450, -5000, 63740, 45)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 680)
    OP_70(0x0005, 780)
    PlaySE(121, 0x01, 0x4B)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_4B34')
    def lambda_4B34():
        CameraSetDistance(2000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4B34)

    CreateThread(0x000D, 0x00, 0x00, func_28_4DB3)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B95',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070321467V#068F#4S#25A姐姐──！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4D2C')

    def _loc_4B95(): pass

    label('loc_4B95')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BE7',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('科洛丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0060321468V#046F#4S#25A艾丝蒂尔……！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4D2C')

    def _loc_4BE7(): pass

    label('loc_4BE7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C3B',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030321469V#024F#4S#25A艾丝蒂尔──！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4D2C')

    def _loc_4C3B(): pass

    label('loc_4C3B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C8D',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0050321470V#054F#4S#25A艾丝蒂尔──！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4D2C')

    def _loc_4C8D(): pass

    label('loc_4C8D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CE1',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0040321471V#530F#4S#25A艾丝蒂尔……！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4D2C')

    def _loc_4CE1(): pass

    label('loc_4CE1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D2C',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080321472V#076F#4S#25A艾丝蒂尔……！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4D2C(): pass

    label('loc_4D2C')

    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    FadeOut(3000, 0, -1)
    Sleep(300)

    OP_24(0x0079, 0x46)
    Sleep(300)

    OP_24(0x0079, 0x41)
    Sleep(300)

    OP_24(0x0079, 0x3C)
    Sleep(300)

    OP_24(0x0079, 0x37)
    Sleep(300)

    OP_24(0x0079, 0x32)
    Sleep(300)

    OP_24(0x0079, 0x2D)
    Sleep(300)

    OP_24(0x0079, 0x28)
    Sleep(300)

    OP_24(0x0079, 0x23)
    Sleep(300)

    OP_23(0x0079)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(2000)

    OP_DC()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0028 offset: 0x4DB3
@scena.Code('func_28_4DB3')
def func_28_4DB3():
    @scena.Lambda('lambda_4DB9')
    def lambda_4DB9():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4DB9)

    @scena.Lambda('lambda_4DD4')
    def lambda_4DD4():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4DD4)

    Sleep(500)

    @scena.Lambda('lambda_4DF4')
    def lambda_4DF4():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4DF4)

    @scena.Lambda('lambda_4E0F')
    def lambda_4E0F():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 35000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4E0F)

    Sleep(500)

    @scena.Lambda('lambda_4E2F')
    def lambda_4E2F():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4E2F)

    @scena.Lambda('lambda_4E4A')
    def lambda_4E4A():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4E4A)

    Sleep(500)

    @scena.Lambda('lambda_4E6A')
    def lambda_4E6A():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 45000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4E6A)

    @scena.Lambda('lambda_4E85')
    def lambda_4E85():
        ChrMoveToRelative(0x00FE, 400000, 100000, 500000, 45000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4E85)

    Return()

# id: 0x0029 offset: 0x4E9B
@scena.Code('func_29_4E9B')
def func_29_4E9B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    CameraMove(5080, 2500, 55830, 0)
    OP_67(0, 4010, -10000, 0)
    CameraSetDistance(8300, 0)
    OP_6C(47000, 0)
    OP_6E(337, 0)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x000D, 0x0001)
    ChrSetPos(0x000D, 20000, 0, 55000, 0)
    PlaySE(293, 0x01, 0x46)
    OP_B0(0x0001, 0x1E)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 330)
    OP_70(0x0001, 430)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_4F49')
    def lambda_4F49():
        CameraMove(24700, 2500, 55500, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4F49)

    @scena.Lambda('lambda_4F61')
    def lambda_4F61():
        OP_67(0, 8240, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4F61)

    @scena.Lambda('lambda_4F79')
    def lambda_4F79():
        OP_6C(317000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_4F79)

    @scena.Lambda('lambda_4F89')
    def lambda_4F89():
        OP_6E(447, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4F89)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0x4FC8
@scena.Code('func_2A_4FC8')
def func_2A_4FC8():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(16329, 4250, 57660, 0)
    OP_67(0, 8380, -10000, 0)
    CameraSetDistance(5340, 0)
    OP_6C(57000, 0)
    OP_6E(476, 0)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x000D, 0x0001)
    ChrSetPos(0x000D, 20000, 0, 55000, 0)
    PlaySE(293, 0x01, 0x46)
    OP_B0(0x0001, 0x14)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 330)
    OP_70(0x0001, 430)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    Fade(1000)
    CameraMove(22780, 500, 70340, 0)
    OP_67(0, 9440, -10000, 0)
    CameraSetDistance(2620, 0)
    OP_6C(57000, 0)
    OP_6E(375, 0)
    CreateThread(0x0008, 0x01, 0x00, func_2C_56CD)
    CreateThread(0x0009, 0x01, 0x00, func_2D_5758)
    CreateThread(0x0014, 0x01, 0x00, func_2E_579C)
    CreateThread(0x0013, 0x01, 0x00, func_2F_57E7)
    CreateThread(0x0011, 0x01, 0x00, func_30_5832)
    CreateThread(0x0015, 0x01, 0x00, func_31_587D)
    CreateThread(0x0016, 0x01, 0x00, func_32_58C8)
    CreateThread(0x0012, 0x01, 0x00, func_33_5913)
    CreateThread(0x0018, 0x01, 0x00, func_34_5957)
    CreateThread(0x0017, 0x01, 0x00, func_35_598C)
    Yield()
    OP_0D()
    WaitForThreadExit(0x0009, 0x0002)
    Sleep(300)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0010341841V#1002F#5P哪、哪里……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0020341842V#1043F#6P从前方甲板\n',
            '看得最清楚的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0016, 0x0001)
    Sleep(500)

    OP_20(0x000007D0)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0016, 270, 600)
    Sleep(400)

    ChrTalk(
        0x0016,
        (
            '#0180341843V#1069F#2P……就是那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(200)

    PlayBGM(130)
    Sleep(500)

    @scena.Lambda('lambda_51E1')
    def lambda_51E1():
        CameraMove(-23010, 2450, 64140, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_51E1)

    @scena.Lambda('lambda_51F9')
    def lambda_51F9():
        OP_6C(81000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_51F9)

    @scena.Lambda('lambda_5209')
    def lambda_5209():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5209)

    @scena.Lambda('lambda_5217')
    def lambda_5217():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5217)

    Sleep(50)

    @scena.Lambda('lambda_522A')
    def lambda_522A():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_522A)

    @scena.Lambda('lambda_5238')
    def lambda_5238():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_5238)

    Sleep(50)

    @scena.Lambda('lambda_524B')
    def lambda_524B():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_524B)

    @scena.Lambda('lambda_5259')
    def lambda_5259():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_5259)

    Sleep(50)

    @scena.Lambda('lambda_526C')
    def lambda_526C():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_526C)

    @scena.Lambda('lambda_527A')
    def lambda_527A():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_527A)

    Sleep(50)

    @scena.Lambda('lambda_528D')
    def lambda_528D():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_528D)

    Sleep(3500)

    CreateThread(0x0016, 0x03, 0x00, func_2B_565E)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    OP_C4(0x00, 0x00000010)
    FadeIn(1, 0)
    OP_0D()
    OP_26(451)
    OP_26(879)
    OP_26(882)
    OP_26(883)
    OP_26(880)
    OP_26(881)
    PlayMovie(0x00, 'ED6_DT41.dat', 0x0000, 0x0001)
    def _loc_52E9(): pass

    label('loc_52E9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5303',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_5300',
    )

    Jump('loc_5303')

    def _loc_5300(): pass

    label('loc_5300')

    Jump('loc_52E9')

    def _loc_5303(): pass

    label('loc_5303')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    CameraMove(19920, 2450, 67640, 0)
    OP_67(0, 6610, -10000, 0)
    CameraSetDistance(3590, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    LoadEffect(0x01, 'map\\mp092_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, -40000, 8000, 10000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_C4(0x00, 0x00000002)
    OP_7E(1100, -910, -120, 110, 1)
    PlaySE(451, 0x00, 0x64)
    PlaySE(293, 0x01, 0x46)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0010341844V#1020F#5P什、什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0060341845V#043F#5P难不成那就是……\n',
            '……那巨大的城市是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0020341846V#1042F#5P嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0180341847V#1069F#5P『辉之环』……\n',
            '果然是辉之环啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0017,
        (
            '#0540341848V#102F#5P──不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0017, 0x0018, 600)
    Sleep(300)

    ChrTalk(
        0x0017,
        (
            '#0540341849V#105F#2P尤莉亚上尉！\n',
            '赶快让军舰降落！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0018, 0x0017, 500)
    Sleep(300)

    ChrTalk(
        0x0018,
        (
            '#0100341850V#173F#6P……啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0540341851V#105F#2P不是有卡西乌斯发布的\n',
            '紧急指令吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341839V再不动就来不及了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0100341853V#177F#6P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    CreateThread(0x0016, 0x03, 0x00, func_2B_565E)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_C4(0x00, 0x00000010)
    FadeIn(1, 0)
    OP_0D()
    OP_26(451)
    OP_26(886)
    OP_26(884)
    OP_26(887)
    OP_26(888)
    OP_26(885)
    PlayMovie(0x00, 'ED6_DT42.dat', 0x0000, 0x0001)
    def _loc_5619(): pass

    label('loc_5619')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5633',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_5630',
    )

    Jump('loc_5633')

    def _loc_5630(): pass

    label('loc_5630')

    Jump('loc_5619')

    def _loc_5633(): pass

    label('loc_5633')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    OP_C4(0x01, 0x00000010)
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/C5413._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002B offset: 0x565E
@scena.Code('func_2B_565E')
def func_2B_565E():
    OP_24(0x01C3, 0x5A)
    OP_24(0x0125, 0x41)
    Sleep(200)

    OP_24(0x01C3, 0x50)
    OP_24(0x0125, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x46)
    OP_24(0x0125, 0x37)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    OP_24(0x0125, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    OP_24(0x0125, 0x2D)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    OP_24(0x0125, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    OP_24(0x0125, 0x1E)
    Sleep(200)

    OP_24(0x01C3, 0x14)
    OP_24(0x0125, 0x14)
    Sleep(200)

    OP_23(0x01C3)
    OP_23(0x0125)

    Return()

# id: 0x002C offset: 0x56CD
@scena.Code('func_2C_56CD')
def func_2C_56CD():
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetChipByIndex(0x00FE, 23)
    ChrWalkTo(0x00FE, 20610, 2450, 70280, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 27)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x002D offset: 0x5758
@scena.Code('func_2D_5758')
def func_2D_5758():
    Sleep(500)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 24)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 19420, 2450, 69060, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x002E offset: 0x579C
@scena.Code('func_2E_579C')
def func_2E_579C():
    Sleep(1000)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 20)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 21280, 2450, 69170, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 12)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x002F offset: 0x57E7
@scena.Code('func_2F_57E7')
def func_2F_57E7():
    Sleep(1500)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 19)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 21830, 2450, 67860, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 11)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0030 offset: 0x5832
@scena.Code('func_30_5832')
def func_30_5832():
    Sleep(2000)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 17)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 20200, 2450, 67730, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 9)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0031 offset: 0x587D
@scena.Code('func_31_587D')
def func_31_587D():
    Sleep(2500)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 21)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 21730, 2450, 66170, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 13)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0032 offset: 0x58C8
@scena.Code('func_32_58C8')
def func_32_58C8():
    Sleep(3000)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 22)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 18580, 2450, 67350, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 14)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0033 offset: 0x5913
@scena.Code('func_33_5913')
def func_33_5913():
    Sleep(3500)

    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 18)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 18530, 2450, 66070, 4000, 0x00)
    ChrSetChipByIndex(0x00FE, 10)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0034 offset: 0x5957
@scena.Code('func_34_5957')
def func_34_5957():
    Sleep(4000)

    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 20110, 2450, 66380, 4000, 0x00)

    Return()

# id: 0x0035 offset: 0x598C
@scena.Code('func_35_598C')
def func_35_598C():
    Sleep(4500)

    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 20050, 2450, 63530, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 20240, 2450, 65190, 4000, 0x00)

    Return()

# id: 0x0036 offset: 0x59C1
@scena.Code('func_36_59C1')
def func_36_59C1():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5A3E'),
        (0x00000001, 'loc_5A44'),
        (-1, 'loc_5A4A'),
    )

    def _loc_5A3E(): pass

    label('loc_5A3E')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5A4A')

    def _loc_5A44(): pass

    label('loc_5A44')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5A4A')

    def _loc_5A4A(): pass

    label('loc_5A4A')

    Return()

# id: 0x0037 offset: 0x5A4B
@scena.Code('func_37_5A4B')
def func_37_5A4B():
    MapClearFlags(0x00000001)
    CameraMove(-551720, -10000, -227160, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
