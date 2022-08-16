import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2300.x'
    header.mapIndex       = 1
    header.bgm            = 60
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
        ('ED6_DT29/CH12730._CH', 'ED6_DT29/CH12730P._CP'),
        ('ED6_DT29/CH12731._CH', 'ED6_DT29/CH12731P._CP'),
        ('ED6_DT29/CH12740._CH', 'ED6_DT29/CH12740P._CP'),
        ('ED6_DT29/CH12741._CH', 'ED6_DT29/CH12741P._CP'),
        ('ED6_DT29/CH12750._CH', 'ED6_DT29/CH12750P._CP'),
        ('ED6_DT29/CH12751._CH', 'ED6_DT29/CH12751P._CP'),
        ('ED6_DT29/CH12760._CH', 'ED6_DT29/CH12760P._CP'),
        ('ED6_DT29/CH12761._CH', 'ED6_DT29/CH12761P._CP'),
        ('ED6_DT29/CH12770._CH', 'ED6_DT29/CH12770P._CP'),
        ('ED6_DT29/CH12771._CH', 'ED6_DT29/CH12771P._CP'),
        ('ED6_DT29/CH12780._CH', 'ED6_DT29/CH12780P._CP'),
        ('ED6_DT29/CH12781._CH', 'ED6_DT29/CH12781P._CP'),
        ('ED6_DT29/CH12790._CH', 'ED6_DT29/CH12790P._CP'),
        ('ED6_DT29/CH12791._CH', 'ED6_DT29/CH12791P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 120,
            z           = -3600,
            y           = -26100,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1E99,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -8600,
            z           = -7200,
            y           = -1440,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1E9A,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 270,
            z           = -7650,
            y           = -200,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1E9B,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 9000,
            z           = -7200,
            y           = 980,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1E9C,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 380,
            z           = 400,
            y           = 50610,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1E9D,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1A6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A6
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A6
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1B6'),
        (0x00000065, 'loc_1BD'),
        (-1, 'loc_1C4'),
    )

    def _loc_1B6(): pass

    label('loc_1B6')

    Event(0, func_02_234)

    Jump('loc_1C4')

    def _loc_1BD(): pass

    label('loc_1BD')

    Event(0, func_08_6A6)

    Jump('loc_1C4')

    def _loc_1C4(): pass

    label('loc_1C4')

    Return()

# id: 0x0001 offset: 0x1C5
@scena.Code('func_01_1C5')
def func_01_1C5():
    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 1, 0x1E99)),
            Expr.Return,
        ),
        'loc_1F9',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_1F9(): pass

    label('loc_1F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 2, 0x1E9A)),
            Expr.Return,
        ),
        'loc_205',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_205(): pass

    label('loc_205')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 3, 0x1E9B)),
            Expr.Return,
        ),
        'loc_211',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_211(): pass

    label('loc_211')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 4, 0x1E9C)),
            Expr.Return,
        ),
        'loc_21D',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_21D(): pass

    label('loc_21D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 5, 0x1E9D)),
            Expr.Return,
        ),
        'loc_229',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_229(): pass

    label('loc_229')

    OP_1B(0x00, 0x00, 0x0007)
    OP_1B(0x01, 0x00, 0x0009)

    Return()

# id: 0x0002 offset: 0x234
@scena.Code('func_02_234')
def func_02_234():
    EventBegin(0x00)
    CameraMove(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 0, 1050, -83970, 0)
    ChrSetPos(0x0102, 0, 1050, -83970, 0)
    ChrSetPos(0x00F8, 0, 1050, -83970, 0)
    ChrSetPos(0x00F9, 0, 1050, -83970, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F8, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F9, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    OP_C8(0x0200, 0x0046, 'C_PLAC22._CH', 0x01, 0x01F4)
    ShowPlaceName('绀碧之塔')
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_03_414)
    Sleep(800)

    @scena.Lambda('lambda_0345')
    def lambda_0345():
        CameraMove(140, 600, -78810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0345)

    CreateThread(0x0102, 0x00, 0x00, func_04_47F)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_05_4EA)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_06_555)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    CameraMove(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 610, 600, -77870, 0)
    ChrSetPos(0x0001, 610, 600, -77870, 0)
    ChrSetPos(0x0002, 610, 600, -77870, 0)
    ChrSetPos(0x0003, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x414
@scena.Code('func_03_414')
def func_03_414():
    @scena.Lambda('lambda_041A')
    def lambda_041A():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_041A)

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0434)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_045F')
    def lambda_045F():
        ChrMoveTo(0x00FE, 610, 600, -77870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_045F)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0004 offset: 0x47F
@scena.Code('func_04_47F')
def func_04_47F():
    @scena.Lambda('lambda_0485')
    def lambda_0485():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0485)

    @scena.Lambda('lambda_049F')
    def lambda_049F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_049F)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_04CA')
    def lambda_04CA():
        ChrMoveTo(0x00FE, -470, 600, -78090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_04CA)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0005 offset: 0x4EA
@scena.Code('func_05_4EA')
def func_05_4EA():
    @scena.Lambda('lambda_04F0')
    def lambda_04F0():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_04F0)

    @scena.Lambda('lambda_050A')
    def lambda_050A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_050A)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0535')
    def lambda_0535():
        ChrMoveTo(0x00FE, 630, 750, -79310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0535)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0006 offset: 0x555
@scena.Code('func_06_555')
def func_06_555():
    @scena.Lambda('lambda_055B')
    def lambda_055B():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_055B)

    @scena.Lambda('lambda_0575')
    def lambda_0575():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0575)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_05A0')
    def lambda_05A0():
        ChrMoveTo(0x00FE, -540, 750, -79320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_05A0)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0007 offset: 0x5C0
@scena.Code('func_07_5C0')
def func_07_5C0():
    EventBegin(0x00)
    Fade(500)
    MapClearFlags(0x00000001)
    CameraMove(-600, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(219000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 680, 700, -81310, 180)
    ChrSetPos(0x0102, -330, 700, -81100, 180)
    ChrSetPos(0x00F8, 910, 750, -79600, 180)
    ChrSetPos(0x00F9, -270, 750, -79450, 180)
    CreateThread(0x0101, 0x00, 0x00, func_0A_819)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, func_0B_89E)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, func_0C_923)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0D_9A8)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/R2401._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x6A6
@scena.Code('func_08_6A6')
def func_08_6A6():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 250, 84500, 0)
    ChrSetPos(0x0101, 500, 250, 84000, 180)
    ChrSetPos(0x0102, -500, 250, 84000, 180)
    ChrSetPos(0x00F8, 500, 250, 85000, 180)
    ChrSetPos(0x00F9, -500, 250, 85000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0010)
    Fade(500)
    CameraMove(70, 250, 82530, 0)
    ChrSetPos(0x0000, 70, 250, 82530, 180)
    ChrSetPos(0x0001, 70, 250, 82530, 180)
    ChrSetPos(0x0002, 70, 250, 82530, 180)
    ChrSetPos(0x0003, 70, 250, 82530, 180)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x7A1
@scena.Code('func_09_7A1')
def func_09_7A1():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, 250, 84500, 0)
    ChrSetPos(0x0101, -500, 250, 85000, 0)
    ChrSetPos(0x0102, 500, 250, 85000, 0)
    ChrSetPos(0x00F8, -500, 250, 84000, 0)
    ChrSetPos(0x00F9, 500, 250, 84000, 0)
    OP_0D()
    Call(0, 0x000F)
    Call(0, 0x0011)
    NewScene('ED6_DT21/C2301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x819
@scena.Code('func_0A_819')
def func_0A_819():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_085E')
    def lambda_085E():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_085E)

    @scena.Lambda('lambda_0878')
    def lambda_0878():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0878)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x89E
@scena.Code('func_0B_89E')
def func_0B_89E():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_08E3')
    def lambda_08E3():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_08E3)

    @scena.Lambda('lambda_08FD')
    def lambda_08FD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_08FD)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x923
@scena.Code('func_0C_923')
def func_0C_923():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0968')
    def lambda_0968():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0968)

    @scena.Lambda('lambda_0982')
    def lambda_0982():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0982)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000D offset: 0x9A8
@scena.Code('func_0D_9A8')
def func_0D_9A8():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_09ED')
    def lambda_09ED():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_09ED)

    @scena.Lambda('lambda_0A07')
    def lambda_0A07():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A07)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000E offset: 0xA2D
@scena.Code('func_0E_A2D')
def func_0E_A2D():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x000F offset: 0xB0C
@scena.Code('func_0F_B0C')
def func_0F_B0C():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0010 offset: 0xBEB
@scena.Code('func_10_BEB')
def func_10_BEB():
    @scena.Lambda('lambda_0BF1')
    def lambda_0BF1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0BF1)

    @scena.Lambda('lambda_0C03')
    def lambda_0C03():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C03)

    @scena.Lambda('lambda_0C15')
    def lambda_0C15():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0C15)

    @scena.Lambda('lambda_0C27')
    def lambda_0C27():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0C27)

    Sleep(2500)

    Return()

# id: 0x0011 offset: 0xC39
@scena.Code('func_11_C39')
def func_11_C39():
    @scena.Lambda('lambda_0C3F')
    def lambda_0C3F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C3F)

    @scena.Lambda('lambda_0C51')
    def lambda_0C51():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0C51)

    @scena.Lambda('lambda_0C63')
    def lambda_0C63():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0C63)

    @scena.Lambda('lambda_0C75')
    def lambda_0C75():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0C75)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
