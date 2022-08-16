import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3605_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3605   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3605.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3605_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT26/CH20280._CH', 'ED6_DT26/CH20280P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT26/CH20420._CH', 'ED6_DT26/CH20420P._CP'),
        ('ED6_DT27/CH04500._CH', 'ED6_DT27/CH04500P._CP'),
        ('ED6_DT27/CH04501._CH', 'ED6_DT27/CH04501P._CP'),
        ('ED6_DT27/CH04502._CH', 'ED6_DT27/CH04502P._CP'),
        ('ED6_DT27/CH04503._CH', 'ED6_DT27/CH04503P._CP'),
        ('ED6_DT27/CH04508._CH', 'ED6_DT27/CH04508P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH00173._CH', 'ED6_DT07/CH00173P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '瘦狼瓦鲁特',
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
            name                = '雾香',
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
            name                = '剑齿虎',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '剑齿虎',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '剑齿虎',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458755,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '偃月轮',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393220,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
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
    )

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x23A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x23A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 5, 0x1E0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25B',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0002)

    Jump('loc_296')

    def _loc_25B(): pass

    label('loc_25B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_27A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_03_43B)

    Jump('loc_296')

    def _loc_27A(): pass

    label('loc_27A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_296',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_04_5E3)

    def _loc_296(): pass

    label('loc_296')

    Return()

# id: 0x0001 offset: 0x297
@scena.Code('func_01_297')
def func_01_297():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A8',
    )

    PlaySE(235, 0x01, 0x50)

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x455),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BD(): pass

    label('loc_2BD')

    Return()

# id: 0x0002 offset: 0x2BE
@scena.Code('func_02_2BE')
def func_02_2BE():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_425')

    def _loc_2E3(): pass

    label('loc_2E3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_425')

    def _loc_2FC(): pass

    label('loc_2FC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_315',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_425')

    def _loc_315(): pass

    label('loc_315')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_425')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_347',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_425')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_360',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_425')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_379',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_425')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_425')

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AB',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_425')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C4',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_425')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_425')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_425')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_425')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_425',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_425')

    def _loc_43A(): pass

    label('loc_43A')

    Return()

# id: 0x0003 offset: 0x43B
@scena.Code('func_03_43B')
def func_03_43B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    StopEffect(0x80, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    CameraMove(-20450, 250, 7600, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4230, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0008, 430, 0, 8430, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    Sleep(1000)

    @scena.Lambda('lambda_04F9')
    def lambda_04F9():
        CameraMove(570, 250, 11510, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_04F9)

    OP_C8(0x0200, 0x0046, 'C_PLAC20._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    WaitForThreadExit(0x000D, 0x0000)
    Sleep(1000)

    Fade(1000)
    CameraMove(570, 250, 11510, 0)
    OP_67(0, 5780, -10000, 0)
    CameraSetDistance(2029, 0)
    OP_6C(36000, 0)
    OP_6E(455, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200340003V#252F这边是『瘦狼』，\n',
            '也已经完成啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200340004V赶快开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C2305._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x5E3
@scena.Code('func_04_5E3')
def func_04_5E3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    ChrSetPos(0x0008, 430, 0, 8430, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    StopEffect(0x80, 0x00)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0000, 60)
    OP_6F(0x0001, 60)
    OP_6F(0x0002, 60)
    OP_6F(0x0003, 60)
    OP_6F(0x0004, 60)
    OP_70(0x0000, 60)
    OP_70(0x0001, 60)
    OP_70(0x0002, 60)
    OP_70(0x0003, 60)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_E8(0xD0, 0x07, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_B0(0x0000, 0x50)
    OP_B0(0x0001, 0x50)
    OP_B0(0x0002, 0x50)
    OP_B0(0x0003, 0x50)
    OP_B0(0x0004, 0x50)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)
    OP_73(0x0002)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 98000, 233000, 0)
    CameraMove(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    LoadEffect(0x00, 'map\\mp049_03.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(312, 0x00, 0x64)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C2305._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x889
@scena.Code('func_05_889')
def func_05_889():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_903'),
        (0x00000001, 'loc_909'),
        (-1, 'loc_90F'),
    )

    def _loc_903(): pass

    label('loc_903')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_90F')

    def _loc_909(): pass

    label('loc_909')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_90F')

    def _loc_90F(): pass

    label('loc_90F')

    Return()

# id: 0x0006 offset: 0x910
@scena.Code('func_06_910')
def func_06_910():
    FadeOut(0, 0, -1)
    CameraMove(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['金'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['凯文神父'],
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
