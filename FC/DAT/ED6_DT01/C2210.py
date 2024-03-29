import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2210   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2210.x'
    header.mapIndex       = 84
    header.bgm            = 31
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
            word_3A         = 84,
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
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH00370._CH', 'ED6_DT07/CH00370P._CP'),
        ('ED6_DT07/CH00371._CH', 'ED6_DT07/CH00371P._CP'),
        ('ED6_DT07/CH00374._CH', 'ED6_DT07/CH00374P._CP'),
        ('ED6_DT07/CH00372._CH', 'ED6_DT07/CH00372P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT06/CH20102._CH', 'ED6_DT06/CH20102P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH00450._CH', 'ED6_DT07/CH00450P._CP'),
        ('ED6_DT07/CH00451._CH', 'ED6_DT07/CH00451P._CP'),
        ('ED6_DT07/CH00454._CH', 'ED6_DT07/CH00454P._CP'),
        ('ED6_DT07/CH00452._CH', 'ED6_DT07/CH00452P._CP'),
        ('ED6_DT07/CH00460._CH', 'ED6_DT07/CH00460P._CP'),
        ('ED6_DT07/CH00461._CH', 'ED6_DT07/CH00461P._CP'),
        ('ED6_DT07/CH00464._CH', 'ED6_DT07/CH00464P._CP'),
        ('ED6_DT07/CH00462._CH', 'ED6_DT07/CH00462P._CP'),
        ('ED6_DT07/CH00470._CH', 'ED6_DT07/CH00470P._CP'),
        ('ED6_DT07/CH00471._CH', 'ED6_DT07/CH00471P._CP'),
        ('ED6_DT07/CH00474._CH', 'ED6_DT07/CH00474P._CP'),
        ('ED6_DT07/CH00472._CH', 'ED6_DT07/CH00472P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20085._CH', 'ED6_DT06/CH20085P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT06/CH20079._CH', 'ED6_DT06/CH20079P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00342._CH', 'ED6_DT07/CH00342P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
        ('ED6_DT06/CH20080._CH', 'ED6_DT06/CH20080P._CP'),
    ]

# id: 0x10001 offset: 0x212
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪恩',
            x                   = -11200,
            z                   = 0,
            y                   = 7490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = -9460,
            z                   = 0,
            y                   = 7150,
            direction           = 90,
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
            name                = '洛克',
            x                   = -10770,
            z                   = 0,
            y                   = 5350,
            direction           = 90,
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
            name                = '青年',
            x                   = -11930,
            z                   = 0,
            y                   = 4280,
            direction           = 90,
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
            name                = '青年',
            x                   = -11460,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
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
            name                = '青年',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 90,
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
            name                = '青年',
            x                   = -11930,
            z                   = 0,
            y                   = 4280,
            direction           = 90,
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
            name                = '青年',
            x                   = -11460,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
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
            name                = '青年',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 90,
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
            name                = '黑衣男子',
            x                   = -11460,
            z                   = 0,
            y                   = 1930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = -10100,
            z                   = 0,
            y                   = 2930,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '秘书基尔巴特',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
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
            name                = '弗科特老人',
            x                   = -3670,
            z                   = 90,
            y                   = 200850,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0104,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x3D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3810,
            y           = 2250,
            z           = 106920,
            range       = 2000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x3F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3F2
@scena.Code('Init')
def Init():
    MapSetFlags(0x40000000)
    FormationAddMember(0xFF, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_40E'),
        (0x00000066, 'loc_421'),
        (0x00000068, 'loc_434'),
        (-1, 'loc_447'),
    )

    def _loc_40E(): pass

    label('loc_40E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 1, 0x439)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41E',
    )

    Event(0, func_03_62A)

    def _loc_41E(): pass

    label('loc_41E')

    Jump('loc_447')

    def _loc_421(): pass

    label('loc_421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 2, 0x43A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_431',
    )

    Event(0, func_04_115A)

    def _loc_431(): pass

    label('loc_431')

    Jump('loc_447')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 3, 0x43B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_444',
    )

    Event(0, func_05_152D)

    def _loc_444(): pass

    label('loc_444')

    Jump('loc_447')

    def _loc_447(): pass

    label('loc_447')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 3, 0x43B)),
            Expr.Return,
        ),
        'loc_4D4',
    )

    ChrSetFlags(0x000F, 0x0800)
    ChrSetFlags(0x0010, 0x0800)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetChipByIndex(0x000A, 31)
    ChrSetChipByIndex(0x000F, 36)
    ChrSetChipByIndex(0x0010, 36)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x000A, 102990, 0, 98020, 270)
    ChrSetPos(0x000F, 104030, 0, 99080, 0)
    ChrSetPos(0x0010, 102870, 0, 100160, 135)

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 2, 0x43A)),
            Expr.Return,
        ),
        'loc_561',
    )

    ChrSetFlags(0x000D, 0x0800)
    ChrSetFlags(0x000E, 0x0800)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetChipByIndex(0x0009, 27)
    ChrSetChipByIndex(0x000D, 36)
    ChrSetChipByIndex(0x000E, 36)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0009, 102640, 0, 1840, 270)
    ChrSetPos(0x000D, 101950, 0, 3240, 0)
    ChrSetPos(0x000E, 101850, 0, 770, 135)

    def _loc_561(): pass

    label('loc_561')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 1, 0x439)),
            Expr.Return,
        ),
        'loc_5EE',
    )

    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x000C, 0x0800)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetPos(0x0008, -240, 0, 6100, 225)
    ChrSetPos(0x000B, 1680, 0, 4920, 180)
    ChrSetPos(0x000C, -1990, 0, 5180, 315)
    ChrSetChipByIndex(0x0008, 23)
    ChrSetChipByIndex(0x000B, 36)
    ChrSetChipByIndex(0x000C, 36)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5EE(): pass

    label('loc_5EE')

    Return()

# id: 0x0001 offset: 0x5EF
@scena.Code('func_01_5EF')
def func_01_5EF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5FE',
    )

    Jump('loc_5FE')

    def _loc_5FE(): pass

    label('loc_5FE')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x392),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_613',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_613(): pass

    label('loc_613')

    Return()

# id: 0x0002 offset: 0x614
@scena.Code('func_02_614')
def func_02_614():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_629',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_614')

    def _loc_629(): pass

    label('loc_629')

    Return()

# id: 0x0003 offset: 0x62A
@scena.Code('func_03_62A')
def func_03_62A():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(400, 0, -2430, 0)
    ChrSetPos(0x0101, 1330, 0, -5430, 0)
    ChrSetPos(0x0102, -680, 0, -5890, 0)
    ChrSetPos(0x0106, 380, 0, -4780, 0)
    ChrSetPos(0x0105, 190, 0, -6650, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, 0, 0, 0, 0)
    ChrSetPos(0x000B, 500, 0, 2140, 225)
    ChrSetPos(0x000C, -1740, 0, 1110, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010061172V#005F是、是他们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061173V#043F前、前几天在仓库碰到的那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061174V#057F真没想到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0106, 120, 0, -3000, 2000, 0x00)
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061175V#054F喂，你们几个蠢货……\n',
            '在这种地方干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        ChrTurnDirection(0x00FE, 0x0101, 230)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07B2)

    @scena.Lambda('lambda_07C0')
    def lambda_07C0():
        ChrTurnDirection(0x00FE, 0x0101, 230)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07C0)

    @scena.Lambda('lambda_07CE')
    def lambda_07CE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07CE)

    Sleep(400)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '三个不良青年露出双目呆滞的神态，\n',
            '似乎什么也意识不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0106,
        (
            '#0050061176V#055F喂、喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0898')
    def lambda_0898():
        ChrWalkTo(0x00FE, -170, 0, -1480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0898)

    Sleep(300)

    OP_63(0x0008)
    OP_63(0x000B)
    OP_63(0x000C)
    ChrSetChipByIndex(0x0008, 24)

    ExecExpressionWithValue(
        0x0000,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(508, 0x00, 0x64)

    @scena.Lambda('lambda_08D6')
    def lambda_08D6():
        OP_99(0x00FE, 0x00, 0x02, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_08D6)

    @scena.Lambda('lambda_08E6')
    def lambda_08E6():
        CameraMove(-170, 0, -1480, 700)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_08E6)

    ChrTalk(
        0x0102,
        (
            '#0020061177V#016F阿加特兄，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_092F')
    def lambda_092F():
        OP_93(0x00FE, 0x0106, 900, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_092F)

    ExecExpressionWithValue(
        0x0000,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_99(0x0008, 0x02, 0x04, 4000)
    PlaySE(214, 0x00, 0x64)
    TerminateThread(0x0106, 0xFF)
    ChrSetChipByIndex(0x0106, 12)
    OP_94(0x01, 0x0106, 0x00B4, 0x00000064, 0x00001388, 0x00)

    @scena.Lambda('lambda_0975')
    def lambda_0975():
        OP_9E(0x00FE, 20, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0975)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        OP_9E(0x00FE, 20, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_098F)

    CameraSetDistance(2800, 700)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050061178V#052F#4P这、这力量……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_09E8')
    def lambda_09E8():
        CameraSetDistance(3000, 150)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09E8)

    @scena.Lambda('lambda_09F8')
    def lambda_09F8():
        OP_99(0x0008, 0x04, 0x07, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09F8)

    ChrSetFlags(0x0008, 0x0020)
    ChrJumpToRelative(0x0106, 0, 0, -1500, 300, 5000)
    ChrJumpToRelative(0x0106, 0, 0, -500, 100, 5000)
    ChrSetChipByIndex(0x0106, 11)
    ChrClearFlags(0x0008, 0x0020)
    Sleep(100)

    ChrSetChipByIndex(0x0008, 21)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 7)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050061179V#057F迪恩，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0450061180V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AAC')
    def lambda_0AAC():
        ChrWalkTo(0x00FE, 1200, 0, 176, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0AAC)

    @scena.Lambda('lambda_0AC7')
    def lambda_0AC7():
        ChrWalkTo(0x00FE, -1000, 0, 256, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0AC7)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 1)
    PlaySE(508, 0x00, 0x64)
    ChrSetDirection(0x000C, 180, 0)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 1)
    PlaySE(508, 0x00, 0x64)
    ChrSetDirection(0x000B, 180, 0)

    ChrTalk(
        0x0106,
        (
            '#0050061181V#057F哈，很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061182V虽然不知道\n',
            '你们在做什么梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061183V#054F就让我好好教训教训你们，\n',
            '给我乖乖清醒过来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0101, 8)

    @scena.Lambda('lambda_0BB5')
    def lambda_0BB5():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BB5)

    Sleep(50)

    ChrSetChipByIndex(0x0102, 9)

    @scena.Lambda('lambda_0BDA')
    def lambda_0BDA():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0BDA)

    ChrSetChipByIndex(0x0105, 37)

    @scena.Lambda('lambda_0BFA')
    def lambda_0BFA():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0BFA)

    ChrSetChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_0C1A')
    def lambda_0C1A():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C1A)

    Sleep(100)

    ChrSetChipByIndex(0x000C, 2)

    @scena.Lambda('lambda_0C3F')
    def lambda_0C3F():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0C3F)

    Sleep(50)

    ChrSetChipByIndex(0x0008, 22)

    @scena.Lambda('lambda_0C64')
    def lambda_0C64():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C64)

    TerminateThread(0x0106, 0xFF)
    ChrSetChipByIndex(0x0106, 13)

    @scena.Lambda('lambda_0C88')
    def lambda_0C88():
        OP_99(0x0106, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0C88)

    @scena.Lambda('lambda_0C98')
    def lambda_0C98():
        ChrJumpToRelative(0x0106, 0, 0, 1500, 1500, 7000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_0C98)

    Sleep(300)

    Battle(0x0000038F, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_CCE'),
        (-1, 'loc_CD1'),
    )

    def _loc_CCE(): pass

    label('loc_CCE')

    OP_B4(0x00)

    Return()

    def _loc_CD1(): pass

    label('loc_CD1')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0105, 0xFF)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrClearFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetChipByIndex(0x0102, 35)
    CameraMove(340, 0, 4960, 0)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrSetPos(0x0102, 860, 0, 4710, 90)
    ChrSetPos(0x0106, -830, 0, 4400, 0)
    ChrSetPos(0x0101, 420, 0, 3000, 0)
    ChrSetPos(0x0105, -880, 0, 2850, 0)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetPos(0x0008, -240, 0, 6100, 225)
    ChrSetPos(0x000B, 1680, 0, 4920, 180)
    ChrSetPos(0x000C, -1990, 0, 5180, 315)
    ChrSetChipByIndex(0x0008, 23)
    ChrSetChipByIndex(0x000B, 36)
    ChrSetChipByIndex(0x000C, 36)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010061184V#009F真、真不敢相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061185V他们比在仓库战斗的时候\n',
            '强了好几个档次啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061186V#043F而且样子怪怪的……\n',
            '到底是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061187V#057F哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061188V看来这些蠢货\n',
            '是被什么人操纵了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061189V#004F操、操纵是指……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020061190V#015F嗯，没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0102, 400)
    ChrTurnDirection(0x0105, 0x0102, 400)
    Fade(250)
    ChrSetChipByIndex(0x0102, 65535)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0102, 225, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061191V#012F似乎是同时利用了药品\n',
            '和心理暗示的特殊催眠术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061192V而且身体的潜能也被激发出来。\n',
            '换言之，力量也达到了更高的水平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061193V#004F这、这种事也能做得到吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061194V#057F当然，\n',
            '不过这无疑需要相当高明的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061195V这帮家伙难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0106, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061196V#044F您想到会是谁了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0105, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061197V#053F啊啊……有点数了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061198V#050F总之，往塔顶走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061199V操纵这些蠢货的幕后真凶\n',
            '一定就在那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061200V#006F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0087, 1, 0x439))
    OP_28(0x003E, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x115A
@scena.Code('func_04_115A')
def func_04_115A():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(96710, 0, 2960, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetChipByIndex(0x0106, 11)
    ChrSetPos(0x0101, 96610, 0, 4430, 180)
    ChrSetPos(0x0102, 95640, 0, 5100, 180)
    ChrSetPos(0x0106, 97840, 0, 5070, 180)
    ChrSetPos(0x0105, 96810, 0, 5780, 180)
    ChrSetChipByIndex(0x0009, 25)
    ChrSetChipByIndex(0x000D, 1)
    ChrSetChipByIndex(0x000E, 1)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0009, 96530, 0, -1510, 0)
    ChrSetPos(0x000D, 94530, 0, -1770, 0)
    ChrSetPos(0x000E, 98360, 0, -790, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0470061201V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061202V#005F又、又来了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061203V#012F虽然不想与你们战斗，\n',
            '但为了找出真正的犯人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 26)

    @scena.Lambda('lambda_12EB')
    def lambda_12EB():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_12EB)

    Sleep(50)

    ChrSetChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_1310')
    def lambda_1310():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1310)

    Sleep(50)

    ChrSetChipByIndex(0x000E, 2)

    @scena.Lambda('lambda_1335')
    def lambda_1335():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1335)

    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0101, 8)

    @scena.Lambda('lambda_1369')
    def lambda_1369():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1369)

    Sleep(50)

    ChrSetChipByIndex(0x0102, 9)

    @scena.Lambda('lambda_138E')
    def lambda_138E():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_138E)

    Sleep(50)

    ChrSetChipByIndex(0x0106, 12)

    @scena.Lambda('lambda_13B3')
    def lambda_13B3():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_13B3)

    Sleep(50)

    ChrSetChipByIndex(0x0105, 37)

    @scena.Lambda('lambda_13D8')
    def lambda_13D8():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_13D8)

    Sleep(200)

    Battle(0x00000390, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_140B'),
        (-1, 'loc_140E'),
    )

    def _loc_140B(): pass

    label('loc_140B')

    OP_B4(0x00)

    Return()

    def _loc_140E(): pass

    label('loc_140E')

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0105, 0xFF)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrClearFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    ChrSetFlags(0x000D, 0x0800)
    ChrSetFlags(0x000E, 0x0800)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetChipByIndex(0x0009, 27)
    ChrSetChipByIndex(0x000D, 36)
    ChrSetChipByIndex(0x000E, 36)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0009, 102640, 0, 1840, 270)
    ChrSetPos(0x000D, 101950, 0, 3240, 0)
    ChrSetPos(0x000E, 101850, 0, 770, 135)
    CameraMove(100640, 0, 1850, 0)
    ChrSetPos(0x0101, 100640, 0, 1850, 95)
    ChrSetPos(0x0102, 100640, 0, 1850, 95)
    ChrSetPos(0x0106, 100640, 0, 1850, 95)
    ChrSetPos(0x0105, 100640, 0, 1850, 95)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x0087, 2, 0x43A))
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x152D
@scena.Code('func_05_152D')
def func_05_152D():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(102090, 0, 102370, 0)
    ChrSetChipByIndex(0x000A, 29)
    ChrSetChipByIndex(0x000F, 1)
    ChrSetChipByIndex(0x0010, 1)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetChipByIndex(0x0106, 11)
    ChrSetPos(0x0101, 104660, 0, 103320, 225)
    ChrSetPos(0x0102, 104440, 0, 104470, 225)
    ChrSetPos(0x0106, 103330, 0, 103120, 225)
    ChrSetPos(0x0105, 103150, 0, 104290, 225)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000A, 98520, 0, 98750, 45)
    ChrSetPos(0x000F, 97520, 0, 99170, 45)
    ChrSetPos(0x0010, 99010, 0, 97700, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0460061204V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061205V#043F对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061206V其实我真的不想对\n',
            '只是受控于人的对手出剑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061207V#053F哼，不必客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061208V#054F留他们一口气就够了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x000A, 30)

    @scena.Lambda('lambda_16E3')
    def lambda_16E3():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16E3)

    Sleep(50)

    ChrSetChipByIndex(0x000F, 2)

    @scena.Lambda('lambda_1708')
    def lambda_1708():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1708)

    Sleep(50)

    ChrSetChipByIndex(0x0010, 2)

    @scena.Lambda('lambda_172D')
    def lambda_172D():
        ChrMoveToRelative(0x00FE, 3000, 0, 3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_172D)

    ChrSetChipByIndex(0x0106, 12)

    @scena.Lambda('lambda_174D')
    def lambda_174D():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_174D)

    Sleep(50)

    ChrSetChipByIndex(0x0105, 37)

    @scena.Lambda('lambda_1772')
    def lambda_1772():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1772)

    Sleep(50)

    ChrSetChipByIndex(0x0101, 8)

    @scena.Lambda('lambda_1797')
    def lambda_1797():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1797)

    Sleep(50)

    ChrSetChipByIndex(0x0102, 9)

    @scena.Lambda('lambda_17BC')
    def lambda_17BC():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_17BC)

    Sleep(300)

    Battle(0x00000391, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_17EF'),
        (-1, 'loc_17F2'),
    )

    def _loc_17EF(): pass

    label('loc_17EF')

    OP_B4(0x00)

    Return()

    def _loc_17F2(): pass

    label('loc_17F2')

    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrClearFlags(0x0106, 0x1000)
    CameraMove(100440, 0, 98970, 0)
    ChrSetPos(0x0101, 100440, 0, 98970, 90)
    ChrSetPos(0x0102, 100440, 0, 98970, 90)
    ChrSetPos(0x0106, 100440, 0, 98970, 90)
    ChrSetPos(0x0105, 100440, 0, 98970, 90)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0105, 0xFF)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrSetFlags(0x000F, 0x0800)
    ChrSetFlags(0x0010, 0x0800)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0010, 0x0001)
    ChrSetChipByIndex(0x000A, 31)
    ChrSetChipByIndex(0x000F, 36)
    ChrSetChipByIndex(0x0010, 36)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x000A, 102990, 0, 98020, 270)
    ChrSetPos(0x000F, 104030, 0, 99080, 0)
    ChrSetPos(0x0010, 102870, 0, 100160, 135)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x0087, 3, 0x43B))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1911
@scena.Code('func_06_1911')
def func_06_1911():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_191E',
    )

    Return()

    def _loc_191E(): pass

    label('loc_191E')

    SetScenaFlags(ScenaFlag(0x0087, 4, 0x43C))
    MapClearFlags(0x00000001)
    EventBegin(0x00)

    @scena.Lambda('lambda_192E')
    def lambda_192E():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_192E)

    @scena.Lambda('lambda_193C')
    def lambda_193C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_193C)

    @scena.Lambda('lambda_194A')
    def lambda_194A():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_194A)

    @scena.Lambda('lambda_1958')
    def lambda_1958():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1958)

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19C6',
    )

    ChrTalk(
        0x0101,
        (
            '#0010061209V#004F咦……这声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A8E')

    def _loc_19C6(): pass

    label('loc_19C6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A0B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020061210V#012F等一下。\n',
            '好像听见有人在说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A8E')

    def _loc_1A0B(): pass

    label('loc_1A0B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A50',
    )

    ChrTalk(
        0x0105,
        (
            '#0060061211V#044F啊……\n',
            '好像在哪里听过的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A8E')

    def _loc_1A50(): pass

    label('loc_1A50')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A8E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050061212V#057F等等。\n',
            '我听见有人在说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A8E(): pass

    label('loc_1A8E')

    OP_20(0x000005DC)
    Sleep(100)

    Fade(1000)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, -1490, 0, 198560, 270)
    ChrSetPos(0x0011, -2330, 0, 199540, 180)
    ChrSetPos(0x0012, -2780, 0, 198270, 90)
    CameraMove(-2200, 0, 198720, 0)
    OP_67(0, 7710, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_21()
    PlayBGM(81)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0480061213V#675F呵呵呵……\n',
            '你们做得非常好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061214V接着只要把罪名全推到那帮败类头上，\n',
            '我们以后就万事大吉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061215V我们的办事能力\n',
            '你应该满意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061216V#675F嗯，真是高明的手段。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061217V不过还是确认一下比较稳妥……\n',
            '没留下什么证据吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061218V嘿嘿，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061219V就算他们恢复了意识，\n',
            '也完全不会记得我们的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061220V看守这灯塔的老头\n',
            '不到天亮也不会醒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061221V#675F听你这么说我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061222V这样一来，\n',
            '那个院长也该放弃孤儿院的重建了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061223V纵火等一连串案件\n',
            '也名正言顺推到了那帮败类头上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061224V这就叫做一箭双雕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061225V你能达成计划就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061226V不过我说，\n',
            '毁掉那间孤儿院到底有什么好处……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061227V真是百思不得其解啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061228V#675F呵呵，看在你们劳苦功高的份上，\n',
            '我就破例告诉你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061229V市长打算将那一带的土地\n',
            '开发成高级别墅区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061230V哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061231V#675F那里紧靠着风光明媚的海道，\n',
            '而且离卢安市区又不远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061232V在那种地头建高级别墅区\n',
            '是最合适不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061233V等到豪宅建成之后，\n',
            '再卖给国内外的大富豪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061234V这就是市长的计划了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061235V哦，真是庞大的计划啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061236V但为什么\n',
            '要毁了那孤儿院呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061237V#675F哈哈，你们想想看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061238V要是在豪华的别墅区当中，\n',
            '留着那样一座破旧的房子会怎样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061239V更何况每天还要\n',
            '忍受着那群小鬼的喧哗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061240V原来如此……\n',
            '作为别墅区的价值恐怕会减半吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061241V不过，与其铤而走险，\n',
            '还不如买下那孤儿院比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061242V#675F哈，那个顽固的女人，\n',
            '哪里肯卖掉丈夫留下的土地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061243V但是，只要趁他们不在的时候，\n',
            '把烧毁的房子清理掉，然后再造上别墅，\n',
            '那就是我们的东西了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061244V嘿嘿，连重建费用都被抢走的话，\n',
            '她不认命也不行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetFlags(0x0105, 0x1000)
    ChrSetFlags(0x0106, 0x1000)
    ChrSetPos(0x0101, 3950, 0, 204590, 225)
    ChrSetPos(0x0102, 3860, 0, 205710, 225)
    ChrSetPos(0x0106, 2790, 0, 204560, 225)
    ChrSetPos(0x0105, 2640, 0, 205560, 225)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetChipByIndex(0x0106, 11)

    ChrTalk(
        0x0105,
        (
            '#0060061245V#6P这就是理由吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    @scena.Lambda('lambda_22D0')
    def lambda_22D0():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_22D0)

    @scena.Lambda('lambda_22DE')
    def lambda_22DE():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_22DE)

    @scena.Lambda('lambda_22EC')
    def lambda_22EC():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_22EC)

    @scena.Lambda('lambda_22FA')
    def lambda_22FA():
        CameraMove(1330, 0, 201850, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_22FA)

    @scena.Lambda('lambda_2312')
    def lambda_2312():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2312)

    @scena.Lambda('lambda_232A')
    def lambda_232A():
        CameraSetDistance(3000, 2000)

        ExitThread()

    DispatchAsync(0x0014, 0x0003, lambda_232A)

    WaitForThreadExit(0x0014, 0x0001)
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0013, -1710, 0, 197880, 5000, 0x00)

    ChrTalk(
        0x0013,
        (
            '#0480061246V#676F是、是你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061247V#049F怎能这样呢……\n',
            '为了这种毫无意义的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061248V不但伤害了老师他们……\n',
            '让充满回忆的地方化作灰烬……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061249V还让孩子们的心灵受到创伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061250V#674F你、你们怎么会找到这里来的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061251V还有……\n',
            '那帮败类不是都在看守的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061252V#006F#4P真可惜～\n',
            '大家都睡得正香呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061253V不过，真没想到市长就是\n',
            '这一系列事件的幕后黑手啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061254V而且，似乎还有些\n',
            '相当面善的家伙牵涉其中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061255V哦……？\n',
            '小姑娘你认识我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061256V我们跟那个红发的游击士\n',
            '倒是有过数面之缘……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061257V#057F哈，什么叫数面之缘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061258V东躲西藏、四处逃窜，\n',
            '最后还引魔兽来对付我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061259V不过，这下终于让我\n',
            '抓到你们这些家伙的尾巴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061260V#674F你、你们两个！\n',
            '快把他们全部杀掉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061261V既、既然被他们看见了，\n',
            '就绝不能让他们活着出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061262V#042F前辈……你太让人失望了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0012, -1530, 0, 199070, 3000, 0x00)
    ChrTurnDirection(0x0012, 0x0106, 0)
    ChrSetChipByIndex(0x0012, 38)

    ChrTalk(
        0x0011,
        (
            '#2620061263V#4P好吧，既然客户提出要求的话，\n',
            '那我们不做也不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0011, 41)

    ChrTalk(
        0x0012,
        (
            '#2630061264V#3P就让我们陪你们玩玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061265V#006F#4P哼，正合我意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061266V#042F就算是受人指使，\n',
            '你们的罪行也无可抵赖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061267V#054F让你们好好尝尝……\n',
            '我这把重剑的厉害吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0011, 39)

    @scena.Lambda('lambda_283C')
    def lambda_283C():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_283C)

    Sleep(100)

    ChrSetChipByIndex(0x0012, 42)

    @scena.Lambda('lambda_2861')
    def lambda_2861():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2861)

    ChrSetChipByIndex(0x0106, 12)

    @scena.Lambda('lambda_2881')
    def lambda_2881():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2881)

    Sleep(50)

    ChrSetChipByIndex(0x0105, 37)

    @scena.Lambda('lambda_28A6')
    def lambda_28A6():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_28A6)

    Sleep(50)

    ChrSetChipByIndex(0x0101, 8)

    @scena.Lambda('lambda_28CB')
    def lambda_28CB():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28CB)

    Sleep(50)

    ChrSetChipByIndex(0x0102, 9)

    @scena.Lambda('lambda_28F0')
    def lambda_28F0():
        ChrMoveToRelative(0x00FE, -3000, 0, -3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_28F0)

    Sleep(300)

    Battle(0x00000392, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2923'),
        (-1, 'loc_2926'),
    )

    def _loc_2923(): pass

    label('loc_2923')

    OP_B4(0x00)

    Return()

    def _loc_2926(): pass

    label('loc_2926')

    EventBegin(0x00)
    CameraMove(-390, 0, 200780, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetChipByIndex(0x0106, 11)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0106, 0)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0011, 38)
    ChrSetChipByIndex(0x0012, 41)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0013, -600, 0, 197930, 0)
    ChrSetPos(0x0011, -2220, 0, 197930, 45)
    ChrSetPos(0x0012, -3180, 0, 199000, 45)
    ChrSetPos(0x0101, 1470, 0, 201530, 225)
    ChrSetPos(0x0106, 400, 0, 201760, 225)
    ChrSetPos(0x0102, 120, 0, 202880, 225)
    ChrSetPos(0x0105, 1590, 0, 202760, 225)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0013,
        (
            '#0480061268V#676F这、这怎么可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061269V#057F#1P市长秘书基尔巴特，\n',
            '还有旁边的两个黑衣男子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061270V现基于游击士协会规定，\n',
            '我要将你们逮捕并拘留归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061271V放弃抵抗，乖乖投降吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061272V#676F呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061273V还真有两下子嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061274V正面交手的话\n',
            '果然还是游击士比较强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061275V嗯，就像队长之前说的，\n',
            '我们不该这么大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061276V#012F队长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061277V难道就是当初和空贼交涉时，\n',
            '那个戴着红色面具的男人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061278V这事你们居然也知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061279V不愧是游击士协会养的狗。\n',
            '鼻子还挺灵的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061280V#005F明明是手下败将，\n',
            '竟然还有心情耍嘴皮子！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061281V快点放下武器，\n',
            '老老实实投降吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061282V哈哈，这可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0011, 17)
    ChrWalkTo(0x0011, -1680, 0, 197780, 1500, 0x00)
    ChrTurnDirection(0x0011, 0x0013, 400)
    ChrSetSubChip(0x0011, 0)
    ChrSetChipByIndex(0x0011, 43)
    PlaySE(216, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0013, 0x0011, 400)

    ChrTalk(
        0x0013,
        (
            '#0480061283V#676F#2P什……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061284V#005F你、你们想做什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061285V别动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061286V你们要是再靠近的话，\n',
            '这家伙的脑袋可就不保哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0480061287V#674F#2P你、你们！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061288V你、你们竟然对\n',
            '自己的雇主做出这种事情！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061289V别误会了，小子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061290V我们的雇主是市长，\n',
            '不是你这家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061291V不过就算是市长也一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061292V我们只不过利害关系一致，\n',
            '所以才帮他一把罢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061293V就算你在这里死掉，\n',
            '我们也是完全不痛不痒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x0013, 50, 0, 600, 6000)

    ChrTalk(
        0x0013,
        (
            '#0480061294V#676F#2P啊、啊啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061295V别过来……你们别过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061296V#057F#1P喂，你们玩够没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061297V以为演演这种下三滥的猴戏\n',
            '就能跑得了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0011, 0x00, 0x02, 2000)
    PlaySE(503, 0x00, 0x64)

    @scena.Lambda('lambda_3025')
    def lambda_3025():
        OP_99(0x00FE, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3025)

    @scena.Lambda('lambda_3035')
    def lambda_3035():
        CameraMove(1400, 0, 201500, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3035)

    ChrJumpTo(0x0013, 750, 0, 198530, 100, 5000)
    ChrSetChipByIndex(0x0013, 44)
    LoadEffect(0x00, 'map\\\\mp020_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 700, 0, 198510, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    OP_9E(0x0013, 50, 0, 600, 6000)

    ChrTalk(
        0x0013,
        (
            '#0480061298V#677F#2P啊啊啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480061299V#677F啊，腿……我的腿！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061300V#046F前、前辈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061301V#057F#1P嘁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061302V#012F看来他们是认真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2630061303V要是这样你们还不相信的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0014, 400)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetSubChip(0x0012, 0)
    ChrSetChipByIndex(0x0012, 43)
    ChrClearFlags(0x0012, 0x0020)

    ChrTalk(
        0x0012,
        (
            '#2630061304V把这看守的老头脑袋打穿\n',
            '我也倒是无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061305V#005F#2P住、住手！\n',
            '不要把无辜的人扯进来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0106, 400)

    ChrTalk(
        0x0011,
        (
            '#2620061306V要我不伤害他也行，\n',
            '不过你们要向后退一段距离……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061307V对了……\n',
            '就退到楼梯边上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061308V#050F#1P哼，没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_32D8')
    def lambda_32D8():
        CameraMove(530, 0, 202030, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_32D8)

    ChrSetChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_32F5')
    def lambda_32F5():
        ChrMoveTo(0x00FE, 3590, 0, 205270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_32F5)

    Sleep(100)

    ChrSetChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_331A')
    def lambda_331A():
        ChrMoveTo(0x00FE, 2540, 0, 205320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_331A)

    Sleep(100)

    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_333F')
    def lambda_333F():
        ChrMoveTo(0x00FE, 3740, 0, 204110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_333F)

    Sleep(100)

    ChrSetChipByIndex(0x0106, 33)

    @scena.Lambda('lambda_3364')
    def lambda_3364():
        ChrMoveTo(0x00FE, 2570, 0, 204000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3364)

    Sleep(200)

    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0012,
        (
            '#2630061309V呵呵，很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2620061310V那么，再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33D6')
    def lambda_33D6():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_33D6')

    DispatchAsync2(0x0101, 0x0002, lambda_33D6)

    @scena.Lambda('lambda_33E7')
    def lambda_33E7():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_33E7')

    DispatchAsync2(0x0102, 0x0002, lambda_33E7)

    @scena.Lambda('lambda_33F8')
    def lambda_33F8():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_33F8')

    DispatchAsync2(0x0105, 0x0002, lambda_33F8)

    @scena.Lambda('lambda_3409')
    def lambda_3409():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3409')

    DispatchAsync2(0x0106, 0x0002, lambda_3409)

    ChrSetChipByIndex(0x0011, 42)

    @scena.Lambda('lambda_341F')
    def lambda_341F():
        CameraMove(3130, 0, 201480, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_341F)

    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0011, 0x0004)
    ChrWalkTo(0x0011, -4050, 0, 195240, 6000, 0x00)
    ChrClearFlags(0x0011, 0x0004)
    ChrWalkTo(0x0011, -2670, 0, 195420, 6000, 0x00)

    @scena.Lambda('lambda_346E')
    def lambda_346E():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_346E')

    DispatchAsync2(0x0106, 0x0002, lambda_346E)

    ChrWalkTo(0x0011, 2009, 1000, 195200, 6000, 0x00)

    @scena.Lambda('lambda_3493')
    def lambda_3493():
        ChrWalkTo(0x0011, 7660, 1000, 200960, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3493)

    Sleep(100)

    ChrSetChipByIndex(0x0012, 42)
    ChrMoveTo(0x0012, 990, 0, 199560, 4000, 0x00)
    ChrMoveTo(0x0012, 3580, 0, 198520, 4000, 0x00)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0012, 4800, 1000, 197980, 2000, 6000)

    @scena.Lambda('lambda_34FC')
    def lambda_34FC():
        ChrWalkTo(0x0012, 7660, 1000, 200960, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_34FC)

    WaitForThreadExit(0x0011, 0x0001)
    OP_4A(0x0011, 1)
    OP_4A(0x0012, 1)
    OP_6F(0x0000, 20)
    Yield()
    OP_6F(0x0000, 40)
    Yield()
    OP_70(0x0000, 80)
    OP_4B(0x0011, 1)
    OP_4B(0x0012, 1)

    @scena.Lambda('lambda_3543')
    def lambda_3543():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3543)

    @scena.Lambda('lambda_3555')
    def lambda_3555():
        ChrWalkTo(0x00FE, 8950, 1000, 201290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_3555)

    WaitForThreadExit(0x0012, 0x0001)

    @scena.Lambda('lambda_3575')
    def lambda_3575():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_3575)

    @scena.Lambda('lambda_3587')
    def lambda_3587():
        ChrWalkTo(0x00FE, 8950, 1000, 201290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_3587)

    ChrTalk(
        0x0101,
        (
            '#0010061311V#005F给我站住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061312V#054F你们逃不掉的，混帐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrClearFlags(0x0106, 0x1000)
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C2200._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x361A
@scena.Code('func_07_361A')
def func_07_361A():
    OP_93(0x0013, 0x0106, 600, 12000, 0x00)

    ChrTalk(
        0x0013,
        (
            '#0480061313V#670F哇啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0106, 0x0013, 0)
    ChrTurnDirection(0x0013, 0x0106, 0)

    @scena.Lambda('lambda_365B')
    def lambda_365B():
        OP_94(0x01, 0x0013, 0x0000, 0x00000258, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_365B)

    OP_94(0x01, 0x0106, 0x00B4, 0x00000258, 0x00001770, 0x00)

    Return()

# id: 0x0008 offset: 0x367B
@scena.Code('func_08_367B')
def func_08_367B():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3691')
    def lambda_3691():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3691)

    ChrSetChipByIndex(0x0101, 8)
    ChrWalkTo(0x00FE, 2910, 0, 206810, 5000, 0x00)
    ChrWalkTo(0x00FE, 3180, 0, 206150, 5000, 0x00)
    ChrWalkTo(0x0101, 1750, 0, 203280, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x0101, 5)
    CreateThread(0x0101, 0x02, 0x00, func_02_614)

    Return()

# id: 0x0009 offset: 0x36F2
@scena.Code('func_09_36F2')
def func_09_36F2():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_3708')
    def lambda_3708():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3708)

    ChrWalkTo(0x00FE, 2910, 0, 206810, 5000, 0x00)
    ChrWalkTo(0x00FE, 3180, 0, 206150, 5000, 0x00)
    ChrWalkTo(0x0105, 1110, 0, 203960, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 0)

    Return()

# id: 0x000A offset: 0x3758
@scena.Code('func_0A_3758')
def func_0A_3758():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_376E')
    def lambda_376E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_376E)

    ChrSetChipByIndex(0x0102, 9)
    ChrWalkTo(0x00FE, 2910, 0, 206810, 5000, 0x00)
    ChrWalkTo(0x00FE, 3180, 0, 206150, 5000, 0x00)
    ChrWalkTo(0x0102, 2130, 0, 204950, 5000, 0x00)
    ChrWalkTo(0x0102, 780, 0, 205020, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x0102, 6)
    CreateThread(0x0102, 0x02, 0x00, func_02_614)

    Return()

# id: 0x000B offset: 0x37E3
@scena.Code('func_0B_37E3')
def func_0B_37E3():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_37F9')
    def lambda_37F9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_37F9)

    ChrSetChipByIndex(0x0106, 12)
    ChrWalkTo(0x00FE, 2910, 0, 206810, 5000, 0x00)
    ChrWalkTo(0x00FE, 3180, 0, 206150, 5000, 0x00)
    ChrWalkTo(0x0106, 3370, 0, 203510, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 0)
    ChrSetChipByIndex(0x0106, 11)
    CreateThread(0x0106, 0x02, 0x00, func_02_614)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
