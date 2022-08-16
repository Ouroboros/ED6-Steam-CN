import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0800_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0800   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0800.x'
    header.mapIndex       = 1
    header.bgm            = 1
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
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT06/CH20113._CH', 'ED6_DT06/CH20113P._CP'),
        ('ED6_DT26/CH20254._CH', 'ED6_DT26/CH20254P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '红色飞艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '埃尔赛尤',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古代龙',
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
        ScenaNpcData(
            name                = '目标用照相机',
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
            name                = '目标用照相机',
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
            name                = '目标',
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
            name                = '尤莉亚上尉',
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
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x272
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x272
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_291',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_03_39B)

    Jump('loc_34F')

    def _loc_291(): pass

    label('loc_291')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2B0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_05_AEA)

    Jump('loc_34F')

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_2CF',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0E_17F3)

    Jump('loc_34F')

    def _loc_2CF(): pass

    label('loc_2CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_14_21F9)

    Jump('loc_34F')

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_30D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(0, func_19_286C)

    Jump('loc_34F')

    def _loc_30D(): pass

    label('loc_30D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_327',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_1D_343E)

    Jump('loc_34F')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_341',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    Event(0, func_1B_2F11)

    Jump('loc_34F')

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_34F',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    Event(0, func_20_3706)

    def _loc_34F(): pass

    label('loc_34F')

    Return()

# id: 0x0001 offset: 0x350
@scena.Code('func_01_350')
def func_01_350():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_368',
    )

    OP_B1('E0800_2')

    Jump('loc_384')

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 5, 0x1A1D)),
            Expr.Return,
        ),
        'loc_37B',
    )

    OP_B1('E0800_1')

    Jump('loc_384')

    def _loc_37B(): pass

    label('loc_37B')

    OP_B1('E0800_2')

    def _loc_384(): pass

    label('loc_384')

    Return()

# id: 0x0002 offset: 0x385
@scena.Code('func_02_385')
def func_02_385():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_385')

    def _loc_39A(): pass

    label('loc_39A')

    Return()

# id: 0x0003 offset: 0x39B
@scena.Code('func_03_39B')
def func_03_39B():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-10470, 10000, -5940, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(487, 0)
    ChrSetPos(0x000F, -10470, 10000, -5940, 0)
    OP_6A(0x000F)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_A1(0x0008, 0x0002)
    ChrSetPos(0x0008, 20000, 0, 0, 270)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    PlaySE(121, 0x01, 0x64)
    PlaySE(451, 0x00, 0x64)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0459')
    def lambda_0459():
        ChrMoveToRelative(0x00FE, -250000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0459)

    @scena.Lambda('lambda_0474')
    def lambda_0474():
        ChrMoveToRelative(0x00FE, -200000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0474)

    OP_24(0x0079, 0x50)
    Sleep(1000)

    OP_24(0x0079, 0x55)
    Sleep(1000)

    OP_24(0x0079, 0x5A)
    Sleep(1000)

    OP_24(0x0079, 0x5F)
    Sleep(1000)

    OP_24(0x0079, 0x64)

    @scena.Lambda('lambda_04B7')
    def lambda_04B7():
        OP_6C(315000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04B7)

    Sleep(1000)

    @scena.Lambda('lambda_04CC')
    def lambda_04CC():
        ChrMoveToRelative(0x00FE, -200000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_04CC)

    Sleep(4000)

    @scena.Lambda('lambda_04EC')
    def lambda_04EC():
        ChrMoveToRelative(0x00FE, -200000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_04EC)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_24(0x0079, 0x64)
    Sleep(200)

    OP_24(0x0079, 0x5A)
    Sleep(200)

    OP_24(0x0079, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x32)
    Sleep(200)

    OP_24(0x0079, 0x28)
    Sleep(200)

    OP_24(0x0079, 0x1E)
    Sleep(200)

    OP_24(0x0079, 0x14)
    Sleep(200)

    OP_24(0x0079, 0x0A)
    Sleep(200)

    OP_24(0x0079, 0x00)
    OP_23(0x0079)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0610._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x580
@scena.Code('func_04_580')
def func_04_580():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    CameraMove(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(4100, 0)
    OP_6C(61000, 0)
    OP_6E(597, 0)
    ChrSetPos(0x0011, -12000, -2550, 20000, 0)
    ChrSetPos(0x000F, -19120, 5000, -3020, 0)
    OP_6A(0x000F)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 0, 0, 0, 270)
    PlaySE(121, 0x01, 0x46)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    ChrClearFlags(0x000A, 0x0100)
    ChrClearFlags(0x000B, 0x0100)
    OP_A1(0x000A, 0x0001)
    OP_A1(0x000B, 0x0002)
    OP_D1(0x000A, 0, 90000, 0, 0)
    OP_D1(0x000B, 0, 90000, 0, 0)
    ChrSetPos(0x000A, 96000, -6550, 20000, 90)
    ChrSetPos(0x000B, 96000, 2550, -20000, 90)
    OP_71(0x0000, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')

    @scena.Lambda('lambda_06A1')
    def lambda_06A1():
        ChrMoveToRelative(0x0101, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_06A1)

    @scena.Lambda('lambda_06BC')
    def lambda_06BC():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_06BC)

    @scena.Lambda('lambda_06D7')
    def lambda_06D7():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_06D7)

    @scena.Lambda('lambda_06F2')
    def lambda_06F2():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06F2)

    @scena.Lambda('lambda_070D')
    def lambda_070D():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_070D)

    @scena.Lambda('lambda_0728')
    def lambda_0728():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0728)

    @scena.Lambda('lambda_0743')
    def lambda_0743():
        OP_67(0, 6390, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0743)

    @scena.Lambda('lambda_075B')
    def lambda_075B():
        CameraSetDistance(5200, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_075B)

    @scena.Lambda('lambda_076B')
    def lambda_076B():
        OP_6C(74000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_076B)

    @scena.Lambda('lambda_077B')
    def lambda_077B():
        OP_6E(616, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_077B)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(3000)

    OP_B0(0x0001, 0x2D)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 520)
    Sleep(100)

    OP_B0(0x0002, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 520)

    @scena.Lambda('lambda_07CD')
    def lambda_07CD():
        ChrMoveToRelativeAsync(0x00FE, -260000, 0, 0, 29000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_07CD)

    @scena.Lambda('lambda_07E8')
    def lambda_07E8():
        ChrMoveToRelativeAsync(0x00FE, -260000, 0, 0, 29000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07E8)

    Sleep(5500)

    @scena.Lambda('lambda_0808')
    def lambda_0808():
        ChrMoveToRelativeAsync(0x00FE, -180000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0808)

    @scena.Lambda('lambda_0823')
    def lambda_0823():
        ChrMoveToRelativeAsync(0x00FE, -180000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0823)

    Sleep(1000)

    @scena.Lambda('lambda_0843')
    def lambda_0843():
        OP_67(0, 4610, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0843)

    @scena.Lambda('lambda_085B')
    def lambda_085B():
        CameraSetDistance(5800, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_085B)

    PlayEffect(0x01, 0x01, 0x0009, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(1000)

    PlayEffect(0x02, 0x01, 0x0009, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x0009, -11000, 2600, 0, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(1500)

    PlayEffect(0x01, 0x01, 0x000A, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(100)

    PlayEffect(0x02, 0x01, 0x000A, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(1000)

    PlayEffect(0x01, 0x01, 0x000B, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    Sleep(100)

    PlayEffect(0x02, 0x01, 0x000B, -5500, 8000, 2000, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    Sleep(20)

    StopEffect(0x01, 0x00)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2500)

    CreateThread(0x000A, 0x00, 0x00, func_0B_145A)
    Sleep(500)

    CreateThread(0x000B, 0x00, 0x00, func_0C_14D0)
    Sleep(1000)

    @scena.Lambda('lambda_0A5C')
    def lambda_0A5C():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0A5C)

    @scena.Lambda('lambda_0A77')
    def lambda_0A77():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A77)

    @scena.Lambda('lambda_0A92')
    def lambda_0A92():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A92)

    Sleep(300)

    @scena.Lambda('lambda_0AB2')
    def lambda_0AB2():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AB2)

    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xAEA
@scena.Code('func_05_AEA')
def func_05_AEA():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\\\mp076_00.eff')
    LoadEffect(0x02, 'map\\\\mp076_01.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(4100, 0)
    OP_6C(61000, 0)
    OP_6E(1065, 0)
    PlaySE(451, 0x00, 0x64)
    OP_76(0x00FF, 0x00000000, 0x0001, -3, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -3, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -8, 0, 0, 0x00, 0x00)
    ChrSetPos(0x0011, -12000, -2550, 20000, 0)
    ChrSetPos(0x000F, -119120, 5000, -3020, 0)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 0, 0, 0, 270)
    PlaySE(293, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_0C2D')
    def lambda_0C2D():
        CameraMove(-12730, -2050, 11180, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C2D)

    @scena.Lambda('lambda_0C45')
    def lambda_0C45():
        OP_67(0, 3710, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C45)

    @scena.Lambda('lambda_0C5D')
    def lambda_0C5D():
        CameraSetDistance(4100, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C5D)

    @scena.Lambda('lambda_0C6D')
    def lambda_0C6D():
        OP_6C(26000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C6D)

    @scena.Lambda('lambda_0C7D')
    def lambda_0C7D():
        OP_6E(885, 8000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0C7D)

    Sleep(6000)

    ChrClearFlags(0x000A, 0x0100)
    ChrClearFlags(0x000B, 0x0100)
    OP_A1(0x000A, 0x0001)
    OP_A1(0x000B, 0x0002)
    OP_D1(0x000A, 0, 90000, 24000, 0)
    OP_D1(0x000B, 0, 90000, 24000, 0)
    ChrSetPos(0x000A, 180000, 550, 40000, 90)
    ChrSetPos(0x000B, 173000, -8550, 20000, 90)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_B0(0x0001, 0x1E)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 500)
    OP_70(0x0001, 520)
    Sleep(100)

    OP_B0(0x0002, 0x1E)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 520)
    PlaySE(121, 0x01, 0x5A)
    CreateThread(0x000B, 0x00, 0x00, func_08_1226)

    @scena.Lambda('lambda_0D37')
    def lambda_0D37():
        OP_D1(0x00FE, 0, 90000, 25000, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0D37)

    Sleep(1500)

    CreateThread(0x000A, 0x00, 0x00, func_07_112A)

    @scena.Lambda('lambda_0D5D')
    def lambda_0D5D():
        OP_D1(0x00FE, 0, 90000, 25000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D5D)

    WaitForThreadExit(0x000B, 0x0002)

    @scena.Lambda('lambda_0D7C')
    def lambda_0D7C():
        OP_D1(0x00FE, 0, 90000, 0, 2500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0D7C)

    WaitForThreadExit(0x000A, 0x0002)

    @scena.Lambda('lambda_0D9B')
    def lambda_0D9B():
        OP_D1(0x00FE, 0, 90000, 0, 2500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D9B)

    WaitForThreadExit(0x000A, 0x0002)
    Sleep(1000)

    PlayEffect(0x01, 0xFF, 0x0009, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    PlayEffect(0x01, 0xFF, 0x0009, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    PlayEffect(0x01, 0xFF, 0x0009, -11000, 2600, 3000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    Sleep(1600)

    PlayEffect(0x01, 0xFF, 0x000A, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    PlayEffect(0x01, 0xFF, 0x000A, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    Sleep(1600)

    PlayEffect(0x01, 0xFF, 0x000B, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    PlayEffect(0x01, 0xFF, 0x000B, -5500, 8000, 2000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    @scena.Lambda('lambda_0F55')
    def lambda_0F55():
        CameraMove(-19120, 5000, -3020, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F55)

    @scena.Lambda('lambda_0F6D')
    def lambda_0F6D():
        OP_67(0, 5210, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F6D)

    @scena.Lambda('lambda_0F85')
    def lambda_0F85():
        CameraSetDistance(4100, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F85)

    @scena.Lambda('lambda_0F95')
    def lambda_0F95():
        OP_6C(61000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F95)

    @scena.Lambda('lambda_0FA5')
    def lambda_0FA5():
        OP_6E(865, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0FA5)

    CreateThread(0x000A, 0x00, 0x00, func_09_1322)

    @scena.Lambda('lambda_0FBC')
    def lambda_0FBC():
        OP_D1(0x00FE, 0, 100000, 30000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0FBC)

    Sleep(1000)

    CreateThread(0x000B, 0x00, 0x00, func_0A_13BE)

    @scena.Lambda('lambda_0FE2')
    def lambda_0FE2():
        OP_D1(0x00FE, 0, 90000, 30000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0FE2)

    CreateThread(0x000A, 0x03, 0x00, func_06_10E7)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x000F, 0x0000)

    @scena.Lambda('lambda_101C')
    def lambda_101C():
        OP_67(0, 510, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_101C)

    @scena.Lambda('lambda_1034')
    def lambda_1034():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1034)

    Sleep(200)

    @scena.Lambda('lambda_1054')
    def lambda_1054():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1054)

    Sleep(200)

    @scena.Lambda('lambda_1074')
    def lambda_1074():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1074)

    Sleep(200)

    @scena.Lambda('lambda_1094')
    def lambda_1094():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1094)

    Sleep(200)

    @scena.Lambda('lambda_10B4')
    def lambda_10B4():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10B4)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0311._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x10E7
@scena.Code('func_06_10E7')
def func_06_10E7():
    OP_24(0x0079, 0x50)
    Sleep(400)

    OP_24(0x0079, 0x46)
    Sleep(400)

    OP_24(0x0079, 0x3C)
    Sleep(400)

    OP_24(0x0079, 0x32)
    Sleep(400)

    OP_24(0x0079, 0x28)
    Sleep(400)

    OP_24(0x0079, 0x1E)
    Sleep(400)

    OP_24(0x0079, 0x14)
    Sleep(400)

    OP_23(0x0079)

    Return()

# id: 0x0007 offset: 0x112A
@scena.Code('func_07_112A')
def func_07_112A():
    @scena.Lambda('lambda_1130')
    def lambda_1130():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 29000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1130)

    Sleep(5000)

    @scena.Lambda('lambda_1150')
    def lambda_1150():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1150)

    Sleep(600)

    @scena.Lambda('lambda_1170')
    def lambda_1170():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1170)

    Sleep(500)

    @scena.Lambda('lambda_1190')
    def lambda_1190():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1190)

    Sleep(400)

    @scena.Lambda('lambda_11B0')
    def lambda_11B0():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11B0)

    Sleep(300)

    @scena.Lambda('lambda_11D0')
    def lambda_11D0():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11D0)

    Sleep(200)

    @scena.Lambda('lambda_11F0')
    def lambda_11F0():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11F0)

    Sleep(100)

    @scena.Lambda('lambda_1210')
    def lambda_1210():
        ChrMoveTo(0x00FE, 4000, 550, 74000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1210)

    Return()

# id: 0x0008 offset: 0x1226
@scena.Code('func_08_1226')
def func_08_1226():
    @scena.Lambda('lambda_122C')
    def lambda_122C():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 29000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_122C)

    Sleep(5000)

    @scena.Lambda('lambda_124C')
    def lambda_124C():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_124C)

    Sleep(600)

    @scena.Lambda('lambda_126C')
    def lambda_126C():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_126C)

    Sleep(500)

    @scena.Lambda('lambda_128C')
    def lambda_128C():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_128C)

    Sleep(400)

    @scena.Lambda('lambda_12AC')
    def lambda_12AC():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12AC)

    Sleep(300)

    @scena.Lambda('lambda_12CC')
    def lambda_12CC():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12CC)

    Sleep(200)

    @scena.Lambda('lambda_12EC')
    def lambda_12EC():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12EC)

    Sleep(100)

    @scena.Lambda('lambda_130C')
    def lambda_130C():
        ChrMoveTo(0x00FE, -3000, -8550, 54000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_130C)

    Return()

# id: 0x0009 offset: 0x1322
@scena.Code('func_09_1322')
def func_09_1322():
    @scena.Lambda('lambda_1328')
    def lambda_1328():
        ChrMoveTo(0x00FE, -26000, 550, 114000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1328)

    Sleep(500)

    @scena.Lambda('lambda_1348')
    def lambda_1348():
        ChrMoveTo(0x00FE, -26000, 550, 114000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1348)

    Sleep(500)

    @scena.Lambda('lambda_1368')
    def lambda_1368():
        ChrMoveTo(0x00FE, -26000, 550, 114000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1368)

    Sleep(500)

    @scena.Lambda('lambda_1388')
    def lambda_1388():
        ChrMoveTo(0x00FE, -26000, 550, 114000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1388)

    Sleep(500)

    @scena.Lambda('lambda_13A8')
    def lambda_13A8():
        ChrMoveTo(0x00FE, -26000, 550, 114000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13A8)

    Return()

# id: 0x000A offset: 0x13BE
@scena.Code('func_0A_13BE')
def func_0A_13BE():
    @scena.Lambda('lambda_13C4')
    def lambda_13C4():
        ChrMoveTo(0x00FE, -33000, -8550, 94000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13C4)

    Sleep(500)

    @scena.Lambda('lambda_13E4')
    def lambda_13E4():
        ChrMoveTo(0x00FE, -33000, -8550, 94000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13E4)

    Sleep(500)

    @scena.Lambda('lambda_1404')
    def lambda_1404():
        ChrMoveTo(0x00FE, -33000, -8550, 94000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1404)

    Sleep(500)

    @scena.Lambda('lambda_1424')
    def lambda_1424():
        ChrMoveTo(0x00FE, -33000, -8550, 94000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1424)

    Sleep(500)

    @scena.Lambda('lambda_1444')
    def lambda_1444():
        ChrMoveTo(0x00FE, -33000, -8550, 94000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1444)

    Return()

# id: 0x000B offset: 0x145A
@scena.Code('func_0B_145A')
def func_0B_145A():
    @scena.Lambda('lambda_1460')
    def lambda_1460():
        OP_D1(0x000A, 0, 90000, 45000, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1460)

    @scena.Lambda('lambda_147A')
    def lambda_147A():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 200000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_147A)

    Sleep(300)

    @scena.Lambda('lambda_149A')
    def lambda_149A():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 200000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_149A)

    Sleep(300)

    @scena.Lambda('lambda_14BA')
    def lambda_14BA():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 200000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_14BA)

    Return()

# id: 0x000C offset: 0x14D0
@scena.Code('func_0C_14D0')
def func_0C_14D0():
    @scena.Lambda('lambda_14D6')
    def lambda_14D6():
        OP_D1(0x000B, 0, 90000, -45000, 800)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_14D6)

    @scena.Lambda('lambda_14F0')
    def lambda_14F0():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -200000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_14F0)

    Sleep(300)

    @scena.Lambda('lambda_1510')
    def lambda_1510():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -200000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1510)

    Sleep(300)

    @scena.Lambda('lambda_1530')
    def lambda_1530():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -200000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1530)

    Return()

# id: 0x000D offset: 0x1546
@scena.Code('func_0D_1546')
def func_0D_1546():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    CameraMove(16900, 5000, -140, 0)
    OP_67(0, 5280, -10000, 0)
    CameraSetDistance(4910, 0)
    OP_6C(75000, 0)
    OP_6E(713, 0)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 150000, -30000, 0, 270)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_71(0x0005, 0x0004)
    OP_A1(0x000E, 0x0000)
    ChrSetPos(0x000E, 50000, -30000, 0, 270)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_72(0x0000, 0x0004)

    @scena.Lambda('lambda_1632')
    def lambda_1632():
        ChrMoveTo(0x00FE, 20000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1632)

    WaitForThreadExit(0x000E, 0x0001)
    Sleep(4000)

    OP_72(0x0005, 0x0004)

    @scena.Lambda('lambda_165C')
    def lambda_165C():
        ChrMoveTo(0x00FE, 120000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_165C)

    @scena.Lambda('lambda_1677')
    def lambda_1677():
        CameraMove(28100, 5000, -5050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1677)

    @scena.Lambda('lambda_168F')
    def lambda_168F():
        OP_67(0, 4320, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_168F)

    @scena.Lambda('lambda_16A7')
    def lambda_16A7():
        CameraSetDistance(6700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_16A7)

    @scena.Lambda('lambda_16B7')
    def lambda_16B7():
        OP_6E(669, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_16B7)

    PlaySE(121, 0x01, 0x50)
    Sleep(500)

    OP_24(0x0079, 0x55)
    Sleep(500)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x5F)
    Sleep(500)

    OP_24(0x0079, 0x64)
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(6000)

    LoadEffect(0x00, 'Scraft\\\\sc003_12.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 117730, -1780, -9290, 270, 0, 0, 8000, 8000, 8000, 0x00FF, 0, 0, 0, 0)
    OP_D1(0x000E, 0, 270000, -45000, 300)
    Sleep(800)

    OP_D1(0x000E, 0, 270000, 0, 300)
    Sleep(1000)

    PlayEffect(0x00, 0xFF, 0x00FF, 117730, -1780, 9290, 270, 0, 0, 8000, 8000, 8000, 0x00FF, 0, 0, 0, 0)
    OP_D1(0x000E, 0, 270000, 45000, 300)
    Sleep(800)

    OP_D1(0x000E, 0, 270000, 0, 300)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x17F3
@scena.Code('func_0E_17F3')
def func_0E_17F3():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'monster\\\\msc0331.eff')
    LoadEffect(0x01, 'map\\\\mp077_00.eff')
    LoadEffect(0x02, 'map\\\\mp077_01.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    CameraMove(9310, -8300, 11010, 0)
    OP_67(0, 2200, -10000, 0)
    CameraSetDistance(4910, 0)
    OP_6C(44000, 0)
    OP_6E(953, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -3, -3, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -15, -6, 0, 0x00, 0x00)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 150000, -30000, 0, 270)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_71(0x0005, 0x0004)
    OP_A1(0x000E, 0x0000)
    ChrSetPos(0x000E, 30000, -30000, 0, 270)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_72(0x0000, 0x0004)
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 0, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 0, 15000, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 0, -15000, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x000E, 0x03, 0x00, func_0F_1D67)
    Sleep(200)

    CreateThread(0x000E, 0x00, 0x00, func_10_1D7E)

    @scena.Lambda('lambda_1A1A')
    def lambda_1A1A():
        CameraMove(24590, -10000, 10600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A1A)

    @scena.Lambda('lambda_1A32')
    def lambda_1A32():
        OP_67(0, 4490, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A32)

    @scena.Lambda('lambda_1A4A')
    def lambda_1A4A():
        OP_6C(65000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A4A)

    @scena.Lambda('lambda_1A5A')
    def lambda_1A5A():
        CameraSetDistance(4910, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A5A)

    @scena.Lambda('lambda_1A6A')
    def lambda_1A6A():
        OP_6E(1230, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_1A6A)

    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x0D)
    OP_6F(0x0000, 76)
    OP_70(0x0000, 95)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(2000)

    OP_72(0x0005, 0x0004)
    CreateThread(0x0009, 0x00, 0x00, func_11_1DFA)
    Sleep(400)

    PlayEffect(0x01, 0xFF, 0x00FF, 120000, -5000, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(293, 0x01, 0x50)
    Sleep(500)

    OP_24(0x0125, 0x55)
    Sleep(500)

    OP_24(0x0125, 0x5A)
    Sleep(500)

    OP_24(0x0125, 0x5F)
    Sleep(500)

    OP_24(0x0125, 0x64)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_1B29')
    def lambda_1B29():
        CameraMove(20670, -10000, 3290, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B29)

    @scena.Lambda('lambda_1B41')
    def lambda_1B41():
        OP_67(0, 5480, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B41)

    @scena.Lambda('lambda_1B59')
    def lambda_1B59():
        OP_6C(80000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B59)

    PlayEffect(0x00, 0xFF, 0x0009, -2270, -1780, -9290, 0, 0, 0, 5000, 5000, 5000, 0x000E, -20000, -1000, -6000, 0)

    @scena.Lambda('lambda_1B9E')
    def lambda_1B9E():
        ChrMoveTo(0x00FE, 0, 1000, 6000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B9E)

    OP_D1(0x000E, 0, 270000, -30000, 1000)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(400)

    CreateThread(0x000E, 0x00, 0x00, func_12_1E76)
    OP_D1(0x000E, 0, 270000, 0, 1500)
    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    PlayEffect(0x00, 0xFF, 0x0009, -2270, -1780, 9290, 0, 0, 0, 5000, 5000, 5000, 0x000E, -20000, -1000, 6000, 0)

    @scena.Lambda('lambda_1C2F')
    def lambda_1C2F():
        ChrMoveTo(0x00FE, 0, 1000, -6000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C2F)

    OP_D1(0x000E, 0, 270000, 30000, 1000)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(400)

    CreateThread(0x000E, 0x00, 0x00, func_12_1E76)
    OP_D1(0x000E, 0, 270000, 0, 1500)
    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_1C8B')
    def lambda_1C8B():
        ChrMoveTo(0x00FE, -100000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C8B)

    Sleep(500)

    @scena.Lambda('lambda_1CAB')
    def lambda_1CAB():
        ChrMoveTo(0x00FE, -100000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1CAB)

    Sleep(400)

    @scena.Lambda('lambda_1CCB')
    def lambda_1CCB():
        ChrMoveTo(0x00FE, -100000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1CCB)

    Sleep(300)

    @scena.Lambda('lambda_1CEB')
    def lambda_1CEB():
        ChrMoveTo(0x00FE, -100000, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1CEB)

    Sleep(200)

    @scena.Lambda('lambda_1D0B')
    def lambda_1D0B():
        ChrMoveTo(0x00FE, -100000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D0B)

    Sleep(100)

    @scena.Lambda('lambda_1D2B')
    def lambda_1D2B():
        ChrMoveTo(0x00FE, -100000, 0, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D2B)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000E, 0x03)
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x1D67
@scena.Code('func_0F_1D67')
def func_0F_1D67():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1D7D',
    )

    PlaySE(288, 0x00, 0x64)
    Sleep(1300)

    Jump('func_0F_1D67')

    def _loc_1D7D(): pass

    label('loc_1D7D')

    Return()

# id: 0x0010 offset: 0x1D7E
@scena.Code('func_10_1D7E')
def func_10_1D7E():
    @scena.Lambda('lambda_1D84')
    def lambda_1D84():
        ChrMoveTo(0x00FE, 0, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D84)

    Sleep(1500)

    @scena.Lambda('lambda_1DA4')
    def lambda_1DA4():
        ChrMoveTo(0x00FE, 0, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DA4)

    Sleep(300)

    @scena.Lambda('lambda_1DC4')
    def lambda_1DC4():
        ChrMoveTo(0x00FE, 0, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DC4)

    Sleep(100)

    @scena.Lambda('lambda_1DE4')
    def lambda_1DE4():
        ChrMoveTo(0x00FE, 0, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DE4)

    Return()

# id: 0x0011 offset: 0x1DFA
@scena.Code('func_11_1DFA')
def func_11_1DFA():
    @scena.Lambda('lambda_1E00')
    def lambda_1E00():
        ChrMoveTo(0x00FE, 120000, 0, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E00)

    Sleep(1500)

    @scena.Lambda('lambda_1E20')
    def lambda_1E20():
        ChrMoveTo(0x00FE, 120000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E20)

    Sleep(300)

    @scena.Lambda('lambda_1E40')
    def lambda_1E40():
        ChrMoveTo(0x00FE, 120000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E40)

    Sleep(100)

    @scena.Lambda('lambda_1E60')
    def lambda_1E60():
        ChrMoveTo(0x00FE, 120000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E60)

    Return()

# id: 0x0012 offset: 0x1E76
@scena.Code('func_12_1E76')
def func_12_1E76():
    @scena.Lambda('lambda_1E7C')
    def lambda_1E7C():
        ChrMoveTo(0x00FE, 0, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E7C)

    Sleep(100)

    @scena.Lambda('lambda_1E9C')
    def lambda_1E9C():
        ChrMoveTo(0x00FE, 0, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E9C)

    Sleep(100)

    @scena.Lambda('lambda_1EBC')
    def lambda_1EBC():
        ChrMoveTo(0x00FE, 0, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EBC)

    Sleep(500)

    @scena.Lambda('lambda_1EDC')
    def lambda_1EDC():
        ChrMoveTo(0x00FE, 0, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EDC)

    Sleep(100)

    @scena.Lambda('lambda_1EFC')
    def lambda_1EFC():
        ChrMoveTo(0x00FE, 0, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EFC)

    Return()

# id: 0x0013 offset: 0x1F12
@scena.Code('func_13_1F12')
def func_13_1F12():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    CameraMove(138530, 2510, -4630, 0)
    OP_67(0, 4780, -10000, 0)
    CameraSetDistance(7240, 0)
    OP_6C(295000, 0)
    OP_6E(784, 0)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 150000, 0, 0, 270)
    ChrClearFlags(0x0009, 0x0100)
    OP_D1(0x0009, 0, 270000, 0, 0)
    PlaySE(121, 0x01, 0x46)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    OP_A1(0x000E, 0x0000)
    ChrSetPos(0x000E, 50000, 0, 0, 270)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_200C')
    def lambda_200C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_200C)

    @scena.Lambda('lambda_2027')
    def lambda_2027():
        OP_D1(0x00FE, 0, 270000, -30000, 300)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2027)

    Sleep(500)

    @scena.Lambda('lambda_2046')
    def lambda_2046():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 20000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2046)

    @scena.Lambda('lambda_2061')
    def lambda_2061():
        OP_D1(0x00FE, 0, 270000, -20000, 300)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2061)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_2080')
    def lambda_2080():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -40000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2080)

    @scena.Lambda('lambda_209B')
    def lambda_209B():
        OP_D1(0x00FE, 0, 270000, 30000, 300)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_209B)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_20BA')
    def lambda_20BA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -40000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20BA)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        OP_D1(0x00FE, 0, 270000, 20000, 300)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_20D5)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_20F4')
    def lambda_20F4():
        ChrMoveTo(0x00FE, 50000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_20F4)

    @scena.Lambda('lambda_210F')
    def lambda_210F():
        OP_D1(0x00FE, 0, 270000, -30000, 300)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_210F)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_212E')
    def lambda_212E():
        ChrMoveTo(0x00FE, 150000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_212E)

    @scena.Lambda('lambda_2149')
    def lambda_2149():
        OP_D1(0x00FE, 0, 270000, -20000, 300)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2149)

    WaitForThreadExit(0x000E, 0x0001)

    @scena.Lambda('lambda_2168')
    def lambda_2168():
        OP_D1(0x00FE, 0, 270000, 0, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2168)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_2187')
    def lambda_2187():
        OP_D1(0x00FE, 0, 270000, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2187)

    Sleep(1500)

    @scena.Lambda('lambda_21A6')
    def lambda_21A6():
        ChrMoveToRelativeAsync(0x00FE, 40000, -30000, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_21A6)

    Sleep(1000)

    @scena.Lambda('lambda_21C6')
    def lambda_21C6():
        ChrMoveToRelativeAsync(0x00FE, 40000, -30000, 0, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_21C6)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x21F9
@scena.Code('func_14_21F9')
def func_14_21F9():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x01, 'map\\\\mp077_00.eff')
    LoadEffect(0x02, 'map\\\\mp077_01.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    CameraMove(157720, -10000, 2940, 0)
    OP_67(0, 2670, -10000, 0)
    CameraSetDistance(7460, 0)
    OP_6C(284000, 0)
    OP_6E(828, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -30, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -30, -5, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -60, -10, 0, 0x00, 0x00)
    PlaySE(299, 0x00, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 555000, 0)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 200000, 0, 0, 270)
    ChrClearFlags(0x0009, 0x0100)
    OP_D1(0x0009, 0, 270000, 0, 0)
    PlaySE(298, 0x00, 0x64)
    OP_B0(0x0005, 0x3C)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 1340)
    OP_70(0x0005, 1540)
    OP_A1(0x000E, 0x0000)
    ChrSetPos(0x000E, -50000, 0, 0, 270)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x19)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    CreateThread(0x000F, 0x03, 0x00, func_15_25BF)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)

    @scena.Lambda('lambda_2384')
    def lambda_2384():
        OP_7C(100, 100, 3000, 100)
        Yield()

        Jump('lambda_2384')

    DispatchAsync2(0x000F, 0x0000, lambda_2384)

    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x000E, 0x00, 0x00, func_16_25DB)
    Sleep(4600)

    @scena.Lambda('lambda_23B5')
    def lambda_23B5():
        OP_D1(0x00FE, 0, 276000, -20000, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_23B5)

    @scena.Lambda('lambda_23CF')
    def lambda_23CF():
        CameraMove(157720, -8000, 2940, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_23CF)

    @scena.Lambda('lambda_23E7')
    def lambda_23E7():
        OP_D0(15000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23E7)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(3000)

    @scena.Lambda('lambda_2406')
    def lambda_2406():
        OP_D1(0x00FE, 0, 268000, 15000, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2406)

    @scena.Lambda('lambda_2420')
    def lambda_2420():
        CameraMove(157720, -8000, -2940, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2420)

    @scena.Lambda('lambda_2438')
    def lambda_2438():
        OP_D0(-15000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2438)

    @scena.Lambda('lambda_2448')
    def lambda_2448():
        OP_6C(256000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2448)

    @scena.Lambda('lambda_2458')
    def lambda_2458():
        CameraSetDistance(7860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2458)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_246D')
    def lambda_246D():
        CameraSetDistance(7460, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_246D)

    WaitForThreadExit(0x000E, 0x0000)
    CreateThread(0x000E, 0x00, 0x00, func_17_26C0)
    Sleep(1600)

    PlayEffect(0x01, 0xFF, 0x00FF, 95000, -5000, 20000, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0xFF, 0x00FF, 90000, -15000, 25000, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    TerminateThread(0x000F, 0x03)
    OP_71(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)

    @scena.Lambda('lambda_2518')
    def lambda_2518():
        CameraMove(166500, -10000, -19590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2518)

    @scena.Lambda('lambda_2530')
    def lambda_2530():
        OP_6C(238000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2530)

    @scena.Lambda('lambda_2540')
    def lambda_2540():
        OP_6E(876, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2540)

    Sleep(1000)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    CreateThread(0x0009, 0x00, 0x00, func_18_2796)
    Sleep(1600)

    PlayEffect(0x01, 0xFF, 0x00FF, 180000, 0, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x000F, 0x00)
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x25BF
@scena.Code('func_15_25BF')
def func_15_25BF():
    Sleep(400)

    def _loc_25C4(): pass

    label('loc_25C4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25DA',
    )

    PlaySE(288, 0x00, 0x50)
    Sleep(800)

    Jump('loc_25C4')

    def _loc_25DA(): pass

    label('loc_25DA')

    Return()

# id: 0x0016 offset: 0x25DB
@scena.Code('func_16_25DB')
def func_16_25DB():
    OP_94(0x01, 0x000E, 0x00B4, 0x00007530, 0x00002710, 0x00)

    @scena.Lambda('lambda_25F0')
    def lambda_25F0():
        OP_97(0x00FE, 200000, 0, 8000, 5000, 0x0003)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_25F0)

    @scena.Lambda('lambda_260C')
    def lambda_260C():
        OP_D1(0x00FE, 0, 270000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_260C)

    WaitForThreadExit(0x000E, 0x0002)
    TerminateThread(0x000E, 0x03)

    @scena.Lambda('lambda_262F')
    def lambda_262F():
        OP_D1(0x00FE, 0, 270000, 0, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_262F)

    OP_94(0x01, 0x000E, 0x00B4, 0x00007530, 0x00002710, 0x00)

    @scena.Lambda('lambda_2658')
    def lambda_2658():
        OP_97(0x00FE, 200000, 0, -10000, 5000, 0x0003)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2658)

    @scena.Lambda('lambda_2674')
    def lambda_2674():
        OP_D1(0x00FE, 0, 270000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_2674)

    WaitForThreadExit(0x000E, 0x0002)
    TerminateThread(0x000E, 0x03)

    @scena.Lambda('lambda_2697')
    def lambda_2697():
        OP_D1(0x00FE, 0, 270000, 0, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_2697)

    ChrMoveTo(0x000E, 100000, 0, 0, 18000, 0x00)

    Return()

# id: 0x0017 offset: 0x26C0
@scena.Code('func_17_26C0')
def func_17_26C0():
    @scena.Lambda('lambda_26C6')
    def lambda_26C6():
        OP_D1(0x00FE, 0, 270000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_26C6)

    @scena.Lambda('lambda_26E0')
    def lambda_26E0():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_26E0)

    Sleep(400)

    @scena.Lambda('lambda_2700')
    def lambda_2700():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2700)

    Sleep(300)

    @scena.Lambda('lambda_2720')
    def lambda_2720():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2720)

    Sleep(200)

    @scena.Lambda('lambda_2740')
    def lambda_2740():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2740)

    Sleep(100)

    @scena.Lambda('lambda_2760')
    def lambda_2760():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2760)

    Sleep(100)

    @scena.Lambda('lambda_2780')
    def lambda_2780():
        ChrMoveTo(0x00FE, 90000, -40000, 40000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2780)

    Return()

# id: 0x0018 offset: 0x2796
@scena.Code('func_18_2796')
def func_18_2796():
    @scena.Lambda('lambda_279C')
    def lambda_279C():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_279C)

    @scena.Lambda('lambda_27B6')
    def lambda_27B6():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27B6)

    Sleep(500)

    @scena.Lambda('lambda_27D6')
    def lambda_27D6():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27D6)

    Sleep(400)

    @scena.Lambda('lambda_27F6')
    def lambda_27F6():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27F6)

    Sleep(300)

    @scena.Lambda('lambda_2816')
    def lambda_2816():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2816)

    Sleep(200)

    @scena.Lambda('lambda_2836')
    def lambda_2836():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2836)

    Sleep(100)

    @scena.Lambda('lambda_2856')
    def lambda_2856():
        ChrMoveTo(0x00FE, 140000, -40000, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2856)

    Return()

# id: 0x0019 offset: 0x286C
@scena.Code('func_19_286C')
def func_19_286C():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-8910, 6280, -6210, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(20340, 0)
    OP_6C(31000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 0, 650000, 0)
    OP_71(0x0000, 0x0004)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 0, 0, 0, 270)
    PlaySE(293, 0x01, 0x46)
    PlaySE(121, 0x01, 0x46)
    OP_71(0x0005, 0x0020)
    OP_B0(0x0005, 0x14)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    Yield()
    OP_A1(0x000A, 0x0001)
    OP_A1(0x000B, 0x0002)
    OP_A1(0x000C, 0x0003)
    OP_A1(0x000D, 0x0004)
    ChrSetPos(0x000A, 33000, 0, 32000, 90)
    ChrSetPos(0x000B, 29000, 0, -30000, 90)
    ChrSetPos(0x000C, -31000, 0, 31000, 90)
    ChrSetPos(0x000D, -34000, 0, -33000, 90)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetBattleFlags(0x0013, 0x0020)
    ChrSetBattleFlags(0x0012, 0x0020)
    OP_89(0x0013, -18360, 3000, -500, 270)
    OP_89(0x0012, -17700, 3000, 690, 270)

    @scena.Lambda('lambda_29A6')
    def lambda_29A6():
        OP_67(0, 4670, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29A6)

    @scena.Lambda('lambda_29BE')
    def lambda_29BE():
        CameraSetDistance(18000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_29BE)

    OP_C8(0x0200, 0x0046, 'C_PLAC17._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 355000, 0)
    CameraMove(-18070, 3020, 390, 0)
    OP_67(0, 6660, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    OP_0D()
    Sleep(1000)

    ChrSetPos(0x0014, -36450, -220, 4480, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0040)
    PlaySE(407, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0012,
        (
            '#0100310992V#171F#2P基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0600310993V#161F#2P哟，来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0014, 0x00, 0x00, func_02_385)

    @scena.Lambda('lambda_2AF5')
    def lambda_2AF5():
        CameraMove(-28310, 3530, 600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2AF5)

    @scena.Lambda('lambda_2B0D')
    def lambda_2B0D():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_2B0D')

    DispatchAsync2(0x0013, 0x0001, lambda_2B0D)

    WaitForThreadExit(0x0101, 0x0002)
    ChrClearFlags(0x0014, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_2B2D')
    def lambda_2B2D():
        CameraMove(-18070, 3020, 390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B2D)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_2B4A')
    def lambda_2B4A():
        ChrWalkTo(0x0014, -18790, 5000, 1550, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2B4A)

    Sleep(1000)

    @scena.Lambda('lambda_2B6A')
    def lambda_2B6A():
        ChrWalkTo(0x0014, -18790, 5000, 1550, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2B6A)

    Sleep(500)

    @scena.Lambda('lambda_2B8A')
    def lambda_2B8A():
        ChrWalkTo(0x0014, -18790, 5000, 1550, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2B8A)

    Sleep(500)

    @scena.Lambda('lambda_2BAA')
    def lambda_2BAA():
        ChrWalkTo(0x0014, -18790, 5000, 1550, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_2BAA)

    WaitForThreadExit(0x0014, 0x0002)
    ChrSetChipByIndex(0x0014, 4)
    ChrSetSubChip(0x0014, 0)

    @scena.Lambda('lambda_2BD4')
    def lambda_2BD4():
        ChrSetDirection(0x0014, 180, 100)

        ExitThread()

    DispatchAsync(0x0014, 0x0003, lambda_2BD4)

    @scena.Lambda('lambda_2BE2')
    def lambda_2BE2():
        ChrSetDirection(0x0012, 270, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2BE2)

    ChrSetFlags(0x0012, 0x0020)
    Fade(250)
    ChrSetChipByIndex(0x0012, 3)
    ChrSetSubChip(0x0012, 2)
    WaitForThreadExit(0x0014, 0x0003)
    ChrMoveTo(0x0014, -18080, 3200, 930, 1500, 0x00)
    Fade(250)
    ChrSetChipByIndex(0x0012, 3)
    ChrSetSubChip(0x0012, 0)
    ChrSetFlags(0x0014, 0x0080)
    OP_0D()
    TerminateThread(0x0013, 0x01)

    ChrTalk(
        0x0014,
        (
            '#0440310994V#311F啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '尤莉亚从基库的脚上拿起了一张纸条。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0012, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0012)
    Sleep(400)

    ChrTurnDirection(0x0012, 0x0013, 400)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#0100310995V#178F#5P……艾丝蒂尔他们已经\n',
            '平安到达了龙所在的岩山。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100310996V接下来他们要穿过岩山内部，\n',
            '前往龙的所在之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0600310997V#160F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0013,
        (
            '#0600310998V#163F#5P……通告全舰艇！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600310999V装填好穿甲弹之后，\n',
            '在指定位置待命！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311000V#162F万一龙逃了出来，\n',
            '也绝不能让它突破包围！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0100311001V#177F#5P是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1600._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x2E55
@scena.Code('func_1A_2E55')
def func_1A_2E55():
    @scena.Lambda('lambda_2E5B')
    def lambda_2E5B():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E5B)

    Sleep(500)

    @scena.Lambda('lambda_2E7B')
    def lambda_2E7B():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E7B)

    Sleep(500)

    @scena.Lambda('lambda_2E9B')
    def lambda_2E9B():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E9B)

    Sleep(500)

    @scena.Lambda('lambda_2EBB')
    def lambda_2EBB():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EBB)

    Sleep(500)

    @scena.Lambda('lambda_2EDB')
    def lambda_2EDB():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EDB)

    Sleep(500)

    @scena.Lambda('lambda_2EFB')
    def lambda_2EFB():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EFB)

    Return()

# id: 0x001B offset: 0x2F11
@scena.Code('func_1B_2F11')
def func_1B_2F11():
    EventBegin(0x00)
    OP_DB()
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_76(0x00FF, 0x00000000, 0x0001, -3, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -3, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -8, 0, 0, 0x00, 0x00)
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS244._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS245._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS244._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C6(0x02, 0x03, -1, 0, 0)
    Sleep(2000)

    OP_C6(0x01, 0x00, -174000, -113000, 0)
    OP_C6(0x01, 0x01, 1300, 1300, 0)
    OP_C6(0x02, 0x00, -174000, -113000, 0)
    OP_C6(0x02, 0x01, 1300, 1300, 0)
    OP_C6(0x00, 0x00, -174000, -113000, 1000)
    OP_C6(0x00, 0x01, 1300, 1300, 1000)
    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C7(0x00, 0x00, 0x00)
    OP_C7(0x00, 0x00, 0x01)
    Sleep(1500)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x00, 0, -66000, 1000)
    OP_C6(0x02, 0x00, 0, -66000, 1000)
    Sleep(400)

    OP_C6(0x01, 0x03, -1, 1000, 0)
    OP_C7(0x00, 0x01, 0x00)
    OP_C7(0x00, 0x01, 0x03)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    CameraMove(-19120, 5000, -3020, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(3990, 0)
    OP_6C(61000, 0)
    OP_6E(597, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0011, -12000, -2550, 20000, 0)
    ChrSetPos(0x000F, -19120, 5000, -3020, 0)
    OP_6A(0x000F)
    OP_A1(0x0009, 0x0005)
    ChrSetPos(0x0009, 0, 0, 0, 270)
    PlaySE(293, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)

    @scena.Lambda('lambda_3207')
    def lambda_3207():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_3207)

    @scena.Lambda('lambda_3222')
    def lambda_3222():
        ChrMoveToRelativeAsync(0x00FE, -300000, 0, 0, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3222)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x326E
@scena.Code('func_1C_326E')
def func_1C_326E():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, -119400, -10000, -115010, 0)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x0F)
    OP_6F(0x0001, 400)
    OP_70(0x0001, 460)
    PlaySE(121, 0x01, 0x64)
    OP_A1(0x000A, 0x0001)
    ChrSetPos(0x000A, -99470, 15000, -91440, 270)
    ChrClearFlags(0x000A, 0x0100)
    OP_D1(0x000A, 45000, 270000, 0, 0)
    CreateThread(0x000A, 0x01, 0x00, func_1F_366A)
    CameraMove(-109880, -10000, -98990, 0)
    OP_67(0, -16070, -10000, 0)
    CameraSetDistance(6000, 0)
    OP_6C(119000, 0)
    OP_6E(699, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_3347')
    def lambda_3347():
        CameraMove(-95610, -10000, -97790, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3347)

    @scena.Lambda('lambda_335F')
    def lambda_335F():
        CameraSetDistance(2750, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_335F)

    @scena.Lambda('lambda_336F')
    def lambda_336F():
        ChrMoveTo(0x00FE, -110470, -80000, -91440, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_336F)

    Sleep(1000)

    SetMessageWindowPos(350, 60, -1, -1)
    TalkSetChrName('乔丝特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#210F不是吧～～～～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(80, 60, -1, -1)
    TalkSetChrName('多伦')

    Talk(
        (
            '#190F喔喔喔喔喔！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    WaitForThreadExit(0x0000, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS148._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x343E
@scena.Code('func_1D_343E')
def func_1D_343E():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 360)
    OP_A1(0x000A, 0x0001)
    ChrClearFlags(0x000A, 0x0100)
    ChrSetPos(0x000A, 0, 40000, 0, 270)
    OP_D1(0x000A, 45000, 270000, 0, 0)
    CameraMove(-44780, -10000, -24460, 0)
    OP_67(0, -16059, -10000, 0)
    CameraSetDistance(6000, 0)
    OP_6C(144000, 0)
    OP_6E(700, 0)
    MapClearFlags(0x00100000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_34F9')
    def lambda_34F9():
        CameraMove(-53240, -10000, -30460, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_34F9)

    CreateThread(0x0000, 0x01, 0x00, func_1E_362C)
    CreateThread(0x000A, 0x00, 0x00, func_1F_366A)

    @scena.Lambda('lambda_351F')
    def lambda_351F():
        OP_D1(0x00FE, 90000, 270000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_351F)

    OP_0D()
    SetMessageWindowPos(350, 60, -1, -1)
    TalkSetChrName('乔丝特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0090350045V#216F#3S不是吧～～～～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(120, 260, -1, -1)
    TalkSetChrName('多伦')

    Talk(
        (
            '#0300350046V#192F#3S啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    OP_56(0x00)
    FadeOut(2000, 0, -1)
    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x32)
    OP_0D()
    TerminateThread(0x0000, 0x02)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_23(0x0079)
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS148._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    OP_20(0x000007D0)
    OP_21()
    MapClearFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x362C
@scena.Code('func_1E_362C')
def func_1E_362C():
    OP_7C(800, 200, 2000, 1000)
    Sleep(1000)

    OP_7C(600, 160, 1500, 1000)
    Sleep(1000)

    OP_7C(400, 120, 1000, 1000)

    Return()

# id: 0x001F offset: 0x366A
@scena.Code('func_1F_366A')
def func_1F_366A():
    @scena.Lambda('lambda_3670')
    def lambda_3670():
        ChrMoveTo(0x00FE, -90000, -100000, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3670)

    Sleep(400)

    @scena.Lambda('lambda_3690')
    def lambda_3690():
        ChrMoveTo(0x00FE, -90000, -100000, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3690)

    Sleep(300)

    @scena.Lambda('lambda_36B0')
    def lambda_36B0():
        ChrMoveTo(0x00FE, -90000, -100000, 0, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_36B0)

    Sleep(200)

    @scena.Lambda('lambda_36D0')
    def lambda_36D0():
        ChrMoveTo(0x00FE, -90000, -100000, 0, 46000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_36D0)

    Sleep(100)

    @scena.Lambda('lambda_36F0')
    def lambda_36F0():
        ChrMoveTo(0x00FE, -90000, -100000, 0, 62000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_36F0)

    Return()

# id: 0x0020 offset: 0x3706
@scena.Code('func_20_3706')
def func_20_3706():
    EventBegin(0x00)
    OP_DB()
    OP_76(0x00FF, 0x00000000, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -2, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -5, -2, 0, 0x00, 0x00)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 555000, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(10490, -10000, 13050, 0)
    OP_67(0, 5750, -10000, 0)
    CameraSetDistance(18200, 0)
    OP_6C(48000, 0)
    OP_6E(337, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0000, 76380, 1000, -14320, 0)
    OP_A1(0x0009, 0x0005)
    ChrClearFlags(0x0009, 0x0100)
    OP_D1(0x0009, 0, 270000, 0, 0)
    ChrSetPos(0x0009, 50000, 0, 0, 270)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 1100)
    OP_70(0x0005, 1300)
    PlaySE(293, 0x01, 0x50)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_3833')
    def lambda_3833():
        CameraMove(9890, -10000, 26390, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_3833)

    @scena.Lambda('lambda_384B')
    def lambda_384B():
        OP_67(0, 3280, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_384B)

    @scena.Lambda('lambda_3863')
    def lambda_3863():
        OP_6C(37000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3863)

    @scena.Lambda('lambda_3873')
    def lambda_3873():
        CameraSetDistance(12900, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3873)

    @scena.Lambda('lambda_3883')
    def lambda_3883():
        ChrMoveTo(0x00FE, 0, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3883)

    WaitForThreadExit(0x0009, 0x0001)
    OP_72(0x0005, 0x0020)
    OP_73(0x0005)
    OP_6F(0x0005, 1300)
    OP_70(0x0005, 1340)
    PlaySE(221, 0x00, 0x64)
    Sleep(240)

    PlaySE(221, 0x00, 0x64)
    Sleep(240)

    PlaySE(221, 0x00, 0x64)
    OP_73(0x0005)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 1340)
    OP_70(0x0005, 1540)
    Sleep(400)

    @scena.Lambda('lambda_38ED')
    def lambda_38ED():
        CameraMove(-209890, 1000, 280, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_38ED)

    @scena.Lambda('lambda_3905')
    def lambda_3905():
        OP_67(0, 720, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3905)

    @scena.Lambda('lambda_391D')
    def lambda_391D():
        OP_6C(277000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_391D)

    @scena.Lambda('lambda_392D')
    def lambda_392D():
        OP_D1(0x00FE, 0, 270000, -20000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_392D)

    @scena.Lambda('lambda_3947')
    def lambda_3947():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3947)

    Sleep(100)

    @scena.Lambda('lambda_3967')
    def lambda_3967():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3967)

    Sleep(100)

    @scena.Lambda('lambda_3987')
    def lambda_3987():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3987)

    Sleep(100)

    @scena.Lambda('lambda_39A7')
    def lambda_39A7():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_39A7)

    Sleep(100)

    @scena.Lambda('lambda_39C7')
    def lambda_39C7():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_39C7)

    Sleep(100)

    @scena.Lambda('lambda_39E7')
    def lambda_39E7():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_39E7)

    Sleep(100)

    @scena.Lambda('lambda_3A07')
    def lambda_3A07():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A07)

    Sleep(100)

    @scena.Lambda('lambda_3A27')
    def lambda_3A27():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A27)

    Sleep(100)

    @scena.Lambda('lambda_3A47')
    def lambda_3A47():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 80000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A47)

    Sleep(100)

    @scena.Lambda('lambda_3A67')
    def lambda_3A67():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 90000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A67)

    Sleep(100)

    @scena.Lambda('lambda_3A87')
    def lambda_3A87():
        ChrMoveTo(0x00FE, -500000, 0, 20000, 100000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3A87)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
