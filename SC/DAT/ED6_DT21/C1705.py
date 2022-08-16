import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1705_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1705   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1705.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT29/CH12910._CH', 'ED6_DT29/CH12910P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH04510._CH', 'ED6_DT27/CH04510P._CP'),
        ('ED6_DT26/CH20306._CH', 'ED6_DT26/CH20306P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04012._CH', 'ED6_DT27/CH04012P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '歼灭天使玲',
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
            name                = '哨兵改',
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
            name                = '哨兵改',
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
            name                = '哨兵改',
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
            name                = '哨兵改',
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
            name                = '哨兵改',
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
            name                = '哨兵改',
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
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458754,
            chipIndex           = 2,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '帕蒂尔·玛蒂尔',
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

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x20A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 5, 0x1E1D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22B',
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

    Event(0, func_05_970)

    Jump('loc_266')

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_24A',
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

    Event(0, func_03_2D5)

    Jump('loc_266')

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_266',
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

    Event(0, func_04_4A1)

    def _loc_266(): pass

    label('loc_266')

    Return()

# id: 0x0001 offset: 0x267
@scena.Code('func_01_267')
def func_01_267():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 5, 0x1E1D)),
            Expr.Return,
        ),
        'loc_27A',
    )

    OP_B1('C1705_y')

    Jump('loc_283')

    def _loc_27A(): pass

    label('loc_27A')

    OP_B1('C1705_n')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_294',
    )

    PlaySE(235, 0x01, 0x50)

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x3FD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2A9(): pass

    label('loc_2A9')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x453),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2BE(): pass

    label('loc_2BE')

    Return()

# id: 0x0002 offset: 0x2BF
@scena.Code('func_02_2BF')
def func_02_2BF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2BF')

    def _loc_2D4(): pass

    label('loc_2D4')

    Return()

# id: 0x0003 offset: 0x2D5
@scena.Code('func_03_2D5')
def func_03_2D5():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-210, 0, -3180, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0008, 70, 0, 8530, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 3)
    StopEffect(0x80, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    @scena.Lambda('lambda_0398')
    def lambda_0398():
        CameraMove(240, 0, 10710, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0398)

    OP_C8(0x0200, 0x0046, 'C_PLAC21._CH', 0x00, 0x03E8)
    FadeIn(1000, 0)
    WaitForThreadExit(0x000F, 0x0000)
    Sleep(1000)

    Fade(1000)
    CameraMove(30, 0, 14990, 0)
    OP_67(0, 2470, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(0, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220340007V#263F#6P呵呵呵……这里是『歼灭天使』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220340008V#1305F玲的准备也完毕了，\n',
            '随时都可以开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x4A1
@scena.Code('func_04_4A1')
def func_04_4A1():
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
    ChrSetPos(0x0008, 70, 0, 8530, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 3)
    StopEffect(0x80, 0x00)
    OP_71(0x0000, 0x0004)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0003, 60)
    OP_6F(0x0004, 60)
    OP_6F(0x0005, 60)
    OP_6F(0x0006, 60)
    OP_6F(0x0007, 60)
    OP_70(0x0003, 60)
    OP_70(0x0004, 60)
    OP_70(0x0005, 60)
    OP_70(0x0006, 60)
    OP_70(0x0007, 60)
    ChrSetPos(0x000F, 0, 1100, 13760, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 2)
    ChrSetSubChip(0x000F, 14)
    OP_E8(0xD0, 0x07, 0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp061_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_B0(0x0003, 0x50)
    OP_B0(0x0004, 0x50)
    OP_B0(0x0005, 0x50)
    OP_B0(0x0006, 0x50)
    OP_B0(0x0007, 0x50)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)
    OP_73(0x0005)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)
    OP_73(0x0006)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)
    OP_73(0x0007)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    OP_79(0x00, 0x0001)
    OP_79(0x01, 0x0001)
    OP_79(0x02, 0x0001)
    OP_79(0x03, 0x0001)
    OP_79(0x04, 0x0001)
    OP_7B()
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
    PlayEffect(0x00, 0xFF, 0x00FF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(312, 0x00, 0x64)
    Sleep(3000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    StopEffect(0x00, 0x00)
    Sleep(2000)

    OP_E8(0xE8, 0x03, 0x00, 0x00)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('怀斯曼教授')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0150340017V#1155F好了！各位！\n',
            '祝祭的准备已经就绪！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340018V让我们尽情享受这历史性的一刻吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(80, 60, -1, -1)
    TalkSetChrName('怪盗布卢布兰')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0170340019V#231F──明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(330, 60, -1, -1)
    TalkSetChrName('幻惑之铃露茜奥拉')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0210340020V#241F吾等『执行者』一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(80, 330, -1, -1)
    TalkSetChrName('瘦狼瓦鲁特')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0200340021V#252F遵照伟大盟主的代理人\n',
            '『蛇之使徒』的指示──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(330, 330, -1, -1)
    TalkSetChrName('歼灭天使玲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0220340022V#1306F现在开始『桩』的解锁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    OP_DB()
    OP_AD('ED6_DT24/C_VIS147._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_DC()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x970
@scena.Code('func_05_970')
def func_05_970():
    Call(0, 0x0006)
    Call(0, 0x0007)
    Call(0, 0x0008)

    Return()

# id: 0x0006 offset: 0x97D
@scena.Code('func_06_97D')
def func_06_97D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_99E',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)

    def _loc_99E(): pass

    label('loc_99E')

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0009, 0x0004)
    Call(0, 0x000B)
    LoadChip('ED6_DT27/CH04518._CH', 'ED6_DT27/CH04518P._CP', 10)
    LoadChip('ED6_DT27/CH04516._CH', 'ED6_DT27/CH04516P._CP', 11)
    LoadChip('ED6_DT29/CH12911._CH', 'ED6_DT29/CH12911P._CP', 12)
    CameraMove(-150, 8440, -4110, 0)
    OP_67(0, 2640, -10000, 0)
    CameraSetDistance(2810, 0)
    OP_6C(68000, 0)
    OP_6E(413, 0)
    ChrSetPos(0x0008, -450, 950, 12440, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 740, -1750, -7480, 0)
    ChrSetPos(0x0102, -650, -1750, -7480, 0)
    ChrSetPos(0x00F8, 820, -1750, -7480, 0)
    ChrSetPos(0x00F9, -750, -1750, -7480, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0003, 8)
    OP_70(0x0004, 8)
    OP_70(0x0005, 8)
    OP_70(0x0006, 8)
    OP_70(0x0007, 8)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0B0F')
    def lambda_0B0F():
        CameraMove(430, 0, -2500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B0F)

    @scena.Lambda('lambda_0B27')
    def lambda_0B27():
        OP_67(0, 8960, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B27)

    @scena.Lambda('lambda_0B3F')
    def lambda_0B3F():
        CameraSetDistance(2300, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B3F)

    @scena.Lambda('lambda_0B4F')
    def lambda_0B4F():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0B4F)

    @scena.Lambda('lambda_0B5F')
    def lambda_0B5F():
        OP_6E(315, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0B5F)

    FadeIn(1000, 0)
    Sleep(4000)

    ChrClearFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_0B82')
    def lambda_0B82():
        ChrWalkTo(0x00FE, 740, 0, -2040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B82)

    Sleep(100)

    ChrClearFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_0BA7')
    def lambda_0BA7():
        ChrWalkTo(0x00FE, -650, 0, -2009, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0BA7)

    Sleep(600)

    ChrClearFlags(0x00F8, 0x0080)

    @scena.Lambda('lambda_0BCC')
    def lambda_0BCC():
        ChrWalkTo(0x00FE, 820, 0, -3520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0BCC)

    Sleep(100)

    ChrClearFlags(0x00F9, 0x0080)

    @scena.Lambda('lambda_0BF1')
    def lambda_0BF1():
        ChrWalkTo(0x00FE, -750, 0, -3590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0BF1)

    WaitForThreadExit(0x00F9, 0x0001)

    NpcTalk(
        0x0008,
        '少女的声音',
        (
            '#0220341548V真是的……\n',
            '人家都等得不耐烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA6',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_CE4')

    def _loc_CA6(): pass

    label('loc_CA6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCD',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_CE4')

    def _loc_CCD(): pass

    label('loc_CCD')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_CE4(): pass

    label('loc_CE4')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D10',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D4E')

    def _loc_D10(): pass

    label('loc_D10')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D37',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_D4E')

    def _loc_D37(): pass

    label('loc_D37')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_D4E(): pass

    label('loc_D4E')

    Sleep(1000)

    PlayBGM(111)
    Sleep(500)

    @scena.Lambda('lambda_0D60')
    def lambda_0D60():
        CameraMove(40, 950, 12620, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D60)

    @scena.Lambda('lambda_0D78')
    def lambda_0D78():
        OP_67(0, 5500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D78)

    @scena.Lambda('lambda_0D90')
    def lambda_0D90():
        OP_6E(310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D90)

    WaitForThreadExit(0x0101, 0x0003)
    Sleep(1000)

    Fade(500)
    CameraMove(0, 950, 9500, 0)
    OP_67(0, 3620, -10000, 0)
    CameraSetDistance(4200, 0)
    OP_6C(0, 0)
    OP_6E(247, 0)
    ChrSetPos(0x0101, 150, -1750, -7480, 0)
    ChrSetPos(0x0102, -1000, -1750, -7480, 0)
    ChrSetPos(0x00F8, 900, -1750, -7480, 0)
    ChrSetPos(0x00F9, -200, -1750, -7480, 0)

    @scena.Lambda('lambda_0E30')
    def lambda_0E30():
        ChrWalkTo(0x00FE, 150, 0, 5500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E30)

    Sleep(300)

    @scena.Lambda('lambda_0E50')
    def lambda_0E50():
        ChrWalkTo(0x00FE, -1000, 0, 4540, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E50)

    Sleep(300)

    @scena.Lambda('lambda_0E70')
    def lambda_0E70():
        ChrWalkTo(0x00FE, 900, 0, 4300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0E70)

    Sleep(300)

    @scena.Lambda('lambda_0E90')
    def lambda_0E90():
        ChrWalkTo(0x00FE, -200, 0, 3100, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0E90)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341549V#1002F#6P玲……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341550V#263F#5P哼哼。\n',
            '艾丝蒂尔真是坏孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341551V竟然趁玲不在的时候\n',
            '从『方舟』逃掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341552V#1305F不过也罢。\n',
            '反正你现在也来陪我玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1055',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341553V#063F#6P玲、玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341554V#1306F#5P呵呵，提妲\n',
            '也是特地来玩的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341555V虽然不能请你吃冰淇淋，\n',
            '不过可以在这里随便放松放松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070290104V#065F#6P啊、呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_107C')

    def _loc_1055(): pass

    label('loc_1055')

    ChrTalk(
        0x0101,
        (
            '#0010341557V#1019F#6P来、来玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_107C(): pass

    label('loc_107C')

    ChrTalk(
        0x0008,
        (
            '#0220341558V#263F#5P还有……哈哈哈。\n',
            '终于现身了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341559V#260F我好想你哦，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341560V#1035F#6P……没想到能在这种地方\n',
            '与你再度相会啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341561V#1040F你长大了……玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341562V#261F#5P呵呵，当然了⊙\n',
            '玲已经１１岁了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341563V#265F约修亚也是，一阵子不见\n',
            '就变得好帅了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341564V虽然眼神不再那样冰冷，\n',
            '看起来有些怪怪的......',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341565V#261F不过，现在的约修亚也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341566V#1053F#6P是吗……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341567V#1007F#6P真受不了……\n',
            '你还是那么老气横秋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341568V#1015F……那个，玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341569V我们，是为了阻止『结社』的计划\n',
            '才来这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341570V#263F#5P呵呵，看样子好像确实是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341571V#269F反正玲也很怕无聊，\n',
            '陪你们玩玩也无妨哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x0008, 14)

    @scena.Lambda('lambda_1361')
    def lambda_1361():
        OP_99(0x0008, 0x0E, 0x08, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1361)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_137B')
    def lambda_137B():
        OP_99(0x0008, 0x08, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_137B)

    Sleep(200)

    Fade(500)

    @scena.Lambda('lambda_1395')
    def lambda_1395():
        CameraSetDistance(4000, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1395)

    PlaySE(505, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_13B4')
    def lambda_13B4():
        OP_99(0x0008, 0x02, 0x00, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_13B4)

    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_142D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_146B')

    def _loc_142D(): pass

    label('loc_142D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1454',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_146B')

    def _loc_1454(): pass

    label('loc_1454')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_146B(): pass

    label('loc_146B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1497',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_14D5')

    def _loc_1497(): pass

    label('loc_1497')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14BE',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_14D5')

    def _loc_14BE(): pass

    label('loc_14BE')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_14D5(): pass

    label('loc_14D5')

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0220341572V#1306F#5P嘻嘻……\n',
            '要让我开心一点哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341573V#1042F#6P……玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341574V#1007F#6P抱歉，我并不是打算\n',
            '来和玲战斗的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341575V#1002F而是……有话要对你说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341576V#264F#5P有话说？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341577V#261F哇，不会是\n',
            '来讲故事给我听的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341578V#1003F#6P不是……\n',
            '是关于让我加入『结社』的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341579V#1025F十分感谢你再一次的盛情邀请，\n',
            '不过，我还是打算拒绝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341580V#268F#5P算啦，毕竟你已经和约修亚重逢了，\n',
            '这也是没办法的事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341581V#269F不过，你最好还是能再重新考虑一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341582V就算你们再怎么努力，\n',
            '也不可能阻止『噬身之蛇』的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341583V这点，约修亚\n',
            '应该最清楚不过了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341584V#1043F#6P……这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341585V#265F#5P而且只要加入『结社』\n',
            '艾丝蒂尔会变得更强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341586V这样就能和玲一样\n',
            '成为『执行者』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341587V#261F呜呼呼，不觉得这很棒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341588V#1015F#6P嗯～变得更强\n',
            '确实很吸引人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341589V#1007F不过……\n',
            '我想这样的强并不是真正的强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341590V至少对我来说是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341591V#264F#5P……咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341592V#1006F#6P我的确想变强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341593V强到能够像妈妈一样，\n',
            '守护自己珍视的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341594V强到可以保护好自己，\n',
            '不再让约修亚担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341595V#1044F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341596V#1007F#6P但是，一旦加入了『结社』，\n',
            '我就不再是自己了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341597V我就不能作为真正的我，而逐渐变强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341598V#1025F所以，我觉得这是毫无意义的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341599V#262F#5P……不明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341600V艾丝蒂尔所说的东西\n',
            '玲一点儿也不明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341601V真正的我是什么？\n',
            '那是怎样的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 0, 0, 6110, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341602V#1025F#6P我……\n',
            '真的很喜欢玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341603V爱装成熟，喜欢恶作剧，\n',
            '还意外地会关心别人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341604V#1016F虽然被你骗得很惨，\n',
            '但是我们一点都不恨你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341605V#264F#5P……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341606V#1003F#6P但是，正因为如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341607V#1007F正因为如此我才\n',
            '不希望玲待在『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341608V#1002F如果你长大了，能够以自己的意志\n',
            '来做出选择，那倒又是另外一回事了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341609V而你还是孩子，待在\n',
            '那种地方本身就是错误的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341610V#1003F如果就这样长大的话，\n',
            '一切就会变得无法挽回了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190623V所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341612V#1300F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341613V#266F……我改变主意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341614V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341615V#1042F#6P……呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x01, 'map\\\\mp009_00.eff')
    Sleep(100)

    Fade(500)
    CameraMove(250, 0, 7960, 0)
    OP_67(0, 7630, -10000, 0)
    CameraSetDistance(1230, 0)
    OP_6C(32000, 0)
    OP_6E(609, 0)
    ChrSetDirection(0x0101, 0, 0)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    PlaySE(571, 0x00, 0x64)

    @scena.Lambda('lambda_1E57')
    def lambda_1E57():
        CameraSetDistance(1100, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E57)

    @scena.Lambda('lambda_1E67')
    def lambda_1E67():
        ChrJumpTo(0x00FE, -420, 500, 8140, 1200, 12000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E67)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    Sleep(100)

    PlaySE(505, 0x00, 0x64)
    ChrSetDirection(0x0008, 225, 0)

    @scena.Lambda('lambda_1EA0')
    def lambda_1EA0():
        OP_99(0x00FE, 0x01, 0x07, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1EA0)

    ChrSetAfterImage(0x00, 0x0102, 0x0032, 0x01F4)
    ChrSetSubChip(0x0102, 2)
    ChrSetChipByIndex(0x0102, 7)

    @scena.Lambda('lambda_1EC2')
    def lambda_1EC2():
        ChrJumpTo(0x0102, -320, 0, 6650, 500, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1EC2)

    Sleep(100)

    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_1EEA')
    def lambda_1EEA():
        OP_99(0x00FE, 0x05, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1EEA)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0102, 0x0001)
    PlayEffect(0x01, 0xFF, 0x0102, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    PlaySE(155, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)

    @scena.Lambda('lambda_1F59')
    def lambda_1F59():
        OP_9E(0x00FE, 30, 0, 1000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1F59)

    @scena.Lambda('lambda_1F73')
    def lambda_1F73():
        OP_9E(0x00FE, 30, 0, 1000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1F73)

    @scena.Lambda('lambda_1F8D')
    def lambda_1F8D():
        ChrJumpTo(0x00FE, 600, 0, 9970, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1F8D)

    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x0102, 0x1000)

    @scena.Lambda('lambda_1FB5')
    def lambda_1FB5():
        ChrMoveTo(0x00FE, -900, 0, 5350, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FB5)

    @scena.Lambda('lambda_1FD0')
    def lambda_1FD0():
        ChrMoveTo(0x00FE, 150, 0, 5900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FD0)

    @scena.Lambda('lambda_1FEB')
    def lambda_1FEB():
        CameraSetDistance(1330, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FEB)

    WaitForThreadExit(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x0020)
    ChrClearFlags(0x0008, 0x0004)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetAfterImage(0x01, 0x0102, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010341616V#1020F#4P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(300)

    PlaySE(571, 0x00, 0x64)

    @scena.Lambda('lambda_2058')
    def lambda_2058():
        ChrJumpTo(0x00FE, 1010, 950, 12180, 1500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2058)

    ChrSetDirection(0x0008, 180, 0)
    Fade(500)
    CameraMove(390, 950, 9200, 0)
    OP_67(0, 4570, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(8000, 0)
    OP_6E(357, 0)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(505, 0x00, 0x64)
    OP_99(0x0008, 0x07, 0x0D, 1500)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341617V#1305F#5P呵呵……不愧是约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341618V反应速度相当快嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    OP_99(0x0102, 0x08, 0x0C, 2000)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020341619V#1035F#6P彼此彼此……你也很强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341620V#1042F看来『歼灭天使』的\n',
            '别名真是名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341621V#263F#5P对，玲很强的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341622V比只会藏匿在暗处行动的\n',
            '『漆黑之牙』强得多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010341623V#1020F#6P等、等一下玲！\n',
            '这么突然干什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341624V#1306F#5P哼哼，我改变主意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341625V#261F既然不能做玲的同伴，\n',
            '艾丝蒂尔就去死吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341626V约修亚，其他所有人都一起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341627V#1019F#6P……去死这种话\n',
            '可不能随便说的啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341628V#1005F真是～气死我了！\n',
            '我要打你的屁股一百下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020341629V#1042F#6P艾丝蒂尔，冷静点。\n',
            '可不能小看她──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341630V#1005F#6P约修亚你闭嘴！\n',
            '我这是在教育小孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341631V#263F#5P嘻嘻，好天真。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341632V虽然我也曾经很喜欢\n',
            '艾丝蒂尔这点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341633V#1302F不过现在却很讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_249B')
    def lambda_249B():
        CameraMove(470, 0, 7210, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_249B)

    @scena.Lambda('lambda_24B3')
    def lambda_24B3():
        OP_67(0, 5260, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_24B3)

    @scena.Lambda('lambda_24CB')
    def lambda_24CB():
        CameraSetDistance(3340, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24CB)

    @scena.Lambda('lambda_24DB')
    def lambda_24DB():
        OP_6C(25000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_24DB)

    @scena.Lambda('lambda_24EB')
    def lambda_24EB():
        OP_6E(301, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_24EB)

    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 6)
    Sleep(1000)

    CreateThread(0x0009, 0x00, 0x00, func_02_2BF)
    CreateThread(0x000A, 0x00, 0x00, func_02_2BF)
    CreateThread(0x000B, 0x00, 0x00, func_02_2BF)
    CreateThread(0x000C, 0x00, 0x00, func_02_2BF)
    CreateThread(0x000D, 0x00, 0x00, func_02_2BF)
    CreateThread(0x000E, 0x00, 0x00, func_02_2BF)
    ChrSetPos(0x0009, -2140, 1250, 9460, 135)
    ChrSetPos(0x000A, 3240, 1250, 8880, 225)
    ChrSetPos(0x000B, 5080, 1250, 4410, 270)
    ChrSetPos(0x000C, 440, 1000, -330, 0)
    ChrSetPos(0x000D, -5680, 1250, 1470, 45)
    ChrSetPos(0x000E, -5200, 1250, 5190, 90)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_2622')
    def lambda_2622():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2622)

    @scena.Lambda('lambda_2634')
    def lambda_2634():
        ChrMoveTo(0x00FE, -2140, 250, 9460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2634)

    Sleep(50)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_265E')
    def lambda_265E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_265E)

    @scena.Lambda('lambda_2670')
    def lambda_2670():
        ChrMoveTo(0x00FE, 3240, 250, 8880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2670)

    Sleep(50)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_269A)

    @scena.Lambda('lambda_26AC')
    def lambda_26AC():
        ChrMoveTo(0x00FE, 5080, 250, 4410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_26AC)

    Sleep(50)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_26D6')
    def lambda_26D6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_26D6)

    @scena.Lambda('lambda_26E8')
    def lambda_26E8():
        ChrMoveTo(0x00FE, 440, 0, -330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_26E8)

    Sleep(50)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_2712')
    def lambda_2712():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2712)

    @scena.Lambda('lambda_2724')
    def lambda_2724():
        ChrMoveTo(0x00FE, -5680, 250, 1470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2724)

    Sleep(50)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_274E')
    def lambda_274E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_274E)

    @scena.Lambda('lambda_2760')
    def lambda_2760():
        ChrMoveTo(0x00FE, -5200, 250, 5190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2760)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27CF',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_280D')

    def _loc_27CF(): pass

    label('loc_27CF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27F6',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_280D')

    def _loc_27F6(): pass

    label('loc_27F6')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_280D(): pass

    label('loc_280D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2834',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2872')

    def _loc_2834(): pass

    label('loc_2834')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_285B',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2872')

    def _loc_285B(): pass

    label('loc_285B')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2872(): pass

    label('loc_2872')

    Sleep(1000)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 8)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 9)
    OP_0D()

    @scena.Lambda('lambda_289C')
    def lambda_289C():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_289C)

    @scena.Lambda('lambda_28AA')
    def lambda_28AA():
        ChrSetDirection(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_28AA)

    ChrSetDirection(0x00F8, 90, 600)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0220341634V#263F#6PＮｏ．ⅩⅤ──\n',
            '『歼灭天使』玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341635V#1304F现在开始歼灭敌方集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_292C')
    def lambda_292C():
        CameraMove(600, 0, 6760, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_292C)

    @scena.Lambda('lambda_2944')
    def lambda_2944():
        CameraSetDistance(2500, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2944)

    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2963')
    def lambda_2963():
        ChrJumpTo(0x00FE, 40, 0, 6580, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2963)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 12)

    @scena.Lambda('lambda_298B')
    def lambda_298B():
        ChrMoveTo(0x00FE, -970, 0, 6870, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_298B)

    ChrSetChipByIndex(0x000A, 12)

    @scena.Lambda('lambda_29AB')
    def lambda_29AB():
        ChrMoveTo(0x00FE, 1120, 0, 6620, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_29AB)

    ChrSetChipByIndex(0x000B, 12)

    @scena.Lambda('lambda_29CB')
    def lambda_29CB():
        ChrMoveTo(0x00FE, 1810, 0, 4540, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_29CB)

    ChrSetChipByIndex(0x000C, 12)

    @scena.Lambda('lambda_29EB')
    def lambda_29EB():
        ChrMoveTo(0x00FE, 0, 0, 2410, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_29EB)

    ChrSetChipByIndex(0x000D, 12)

    @scena.Lambda('lambda_2A0B')
    def lambda_2A0B():
        ChrMoveTo(0x00FE, -1840, 0, 3430, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A0B)

    ChrSetChipByIndex(0x000E, 12)

    @scena.Lambda('lambda_2A2B')
    def lambda_2A2B():
        ChrMoveTo(0x00FE, -1930, 0, 5080, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_2A2B)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    Battle(0x000003FD, 0x00000000, 0x01, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2A7A'),
        (-1, 'loc_2A7F'),
    )

    def _loc_2A7A(): pass

    label('loc_2A7A')

    OP_B4(0x00)

    Jump('loc_2A7F')

    def _loc_2A7F(): pass

    label('loc_2A7F')

    Return()

# id: 0x0007 offset: 0x2A80
@scena.Code('func_07_2A80')
def func_07_2A80():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0009, 0x0004)
    Call(0, 0x000B)
    LoadChip('ED6_DT27/CH04518._CH', 'ED6_DT27/CH04518P._CP', 10)
    LoadChip('ED6_DT27/CH04516._CH', 'ED6_DT27/CH04516P._CP', 11)
    LoadChip('ED6_DT27/CH04511._CH', 'ED6_DT27/CH04511P._CP', 13)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0003, 8)
    OP_70(0x0004, 8)
    OP_70(0x0005, 8)
    OP_70(0x0006, 8)
    OP_70(0x0007, 8)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetPos(0x0101, 600, 0, 4500, 0)
    ChrSetPos(0x0102, -600, 0, 3600, 0)
    ChrSetPos(0x00F8, 1300, 0, 3200, 0)
    ChrSetPos(0x00F9, 0, 0, 2200, 0)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetSubChip(0x00F8, 1)
    ChrSetChipByIndex(0x00F8, 8)
    ChrSetSubChip(0x00F9, 1)
    ChrSetChipByIndex(0x00F9, 9)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 1220, 950, 12420, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    CameraMove(400, 950, 9010, 0)
    OP_67(0, 3170, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(4000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341636V#264F#5P哎呀，带来的小家伙们\n',
            '全部都被干掉了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341637V#1305F嘻嘻，挺能撑的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341638V#1019F#6P你、你闹够了没有啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341639V#1005F做这种事\n',
            '玲真的很开心吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341640V#263F#5P哈哈哈，当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341641V#1306F玲，最喜欢\n',
            '看人痛苦的样子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341642V似乎只有这样才能\n',
            '填补自己空虚的灵魂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341643V#261F玲，也喜欢\n',
            '听人痛苦的声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341644V他人的呻吟会令玲沉醉梦乡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341645V#1020F#6P……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341646V#1043F#6P是吗……你至今还……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341647V#1302F#5P……约修亚你闭嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2EC7')
    def lambda_2EC7():
        CameraSetDistance(3800, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2EC7)

    Sleep(500)

    PlayBGM(83)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341648V#1305F#5P唔，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341649V玲小的时候，\n',
            '曾有过假的爸爸妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341650V#1026F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341651V#263F#5P假的爸爸妈妈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341652V#260F虽然我很喜欢他们，\n',
            '但是他们在生意场上好像失败了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341653V所以他们不得不把玲\n',
            '交给了那些坏人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341654V#261F他们一边哭着一边不断地说：\n',
            '『我们一定会来接你的』…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341655V#1026F#6P然、然后………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341656V#268F#5P玲被交给那些人之后，\n',
            '他们让玲做各式各样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341657V玲很快就习惯了大部分的事情，\n',
            '但只有疼痛，却一直都无法忍受…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341658V#1300F虽然也有同龄的孩子，\n',
            '但往往很快就搞坏了身体，\n',
            '很多就这样死了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341659V#1305F这种生活持续了半年左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341660V#1022F#6P……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31CB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341661V#065F#6P……玲…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31CB(): pass

    label('loc_31CB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_320C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341662V#1067F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_320C(): pass

    label('loc_320C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3240',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341663V#057F#6P混帐东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3240(): pass

    label('loc_3240')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3278',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341664V#522F#6P……太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3278(): pass

    label('loc_3278')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32AE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341665V#049F#6P……女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32AE(): pass

    label('loc_32AE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32EA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341666V#077F#6P……这些邪道…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32EA(): pass

    label('loc_32EA')

    ChrTalk(
        0x0008,
        (
            '#0220341667V#265F#5P结果就是，\n',
            '我的爸爸妈妈都是冒牌货。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341668V如果是真的，当玲觉得痛的时候\n',
            '应该会马上来接我才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341669V#261F对吧，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341670V#1027F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341671V#263F#5P哼哼，不过无所谓了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341672V#1305F约修亚和莱维\n',
            '代替他们来接玲了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341673V他们把坏人们全部杀光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341674V#1026F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341675V#1043F#6P……『结社』偶尔\n',
            '也会摧毁一些卑劣的犯罪组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341676V这当然不是为了正义，\n',
            '而是为了将其纳入自己的秩序中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341677V#1035F那次也是这类任务之一吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341678V#1026F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341679V#263F#5P被带到『结社』之后\n',
            '玲学会了各式各样的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341680V#260F约修亚教了我隐形术，\n',
            '莱维教了我武术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341681V其他的人们，也各自\n',
            '将擅长的本领教给我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341682V#265F接着在『十三工房』\n',
            '学会了和人偶做朋友的方法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341683V#261F──然后玲\n',
            '遇到了真正的爸爸和妈妈『帕蒂尔·玛蒂尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(250)
    ChrSetChipByIndex(0x0008, 11)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    PlaySE(213, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(500)

    @scena.Lambda('lambda_36C0')
    def lambda_36C0():
        OP_7C(0, 20, 3000, 100)
        Yield()

        Jump('lambda_36C0')

    DispatchAsync2(0x0010, 0x0003, lambda_36C0)

    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    PlaySE(275, 0x00, 0x46)
    OP_A1(0x0010, 0x0000)
    ChrSetPos(0x0010, 10580, 14000, 9330, 225)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 201)
    OP_70(0x0000, 220)
    Sleep(500)

    OP_72(0x0000, 0x0004)
    Sleep(500)

    Fade(500)
    CameraMove(10320, 10980, 5440, 0)
    OP_67(0, -3080, -10000, 0)
    CameraSetDistance(2320, 0)
    OP_6C(359000, 0)
    OP_6E(390, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, 1200, 0, 1600, 45)
    ChrSetPos(0x0102, 600, 0, 2100, 45)
    ChrSetPos(0x00F8, 800, 0, 300, 45)
    ChrSetPos(0x00F9, -750, 0, 1800, 45)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 8)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 9)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 3)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0001)

    ExecExpressionWithValue(
        0x0010,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000040)
    OP_24(0x0113, 0x50)

    @scena.Lambda('lambda_3859')
    def lambda_3859():
        ChrMoveTo(0x00FE, 10580, 500, 9330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3859)

    Sleep(100)

    OP_24(0x0113, 0x5A)

    @scena.Lambda('lambda_387D')
    def lambda_387D():
        CameraMove(10350, 5820, 6780, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_387D)

    @scena.Lambda('lambda_3895')
    def lambda_3895():
        OP_67(0, 6200, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3895)

    @scena.Lambda('lambda_38AD')
    def lambda_38AD():
        CameraSetDistance(2320, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38AD)

    @scena.Lambda('lambda_38BD')
    def lambda_38BD():
        OP_6E(390, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38BD)

    Play3DEffect(0x02, 0x00, 0x00, 'Frame86__jet_0', 0x00000000, 0xFFFFFD44, 0x00000000, 0x003C, 0xFFA6, 0x00B4, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Play3DEffect(0x02, 0x01, 0x00, 'Frame87__jet_1', 0x00000000, 0xFFFFFD44, 0x00000000, 0x001E, 0x0046, 0xFF4C, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)

    @scena.Lambda('lambda_3937')
    def lambda_3937():
        ChrMoveTo(0x00FE, 10580, 1000, 9330, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3937)

    Sleep(100)

    OP_24(0x0113, 0x64)

    @scena.Lambda('lambda_395B')
    def lambda_395B():
        ChrMoveTo(0x00FE, 10580, 500, 9330, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_395B)

    Sleep(100)

    @scena.Lambda('lambda_397B')
    def lambda_397B():
        ChrMoveTo(0x00FE, 10580, 500, 9330, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_397B)

    Sleep(4000)

    Fade(500)
    OP_6F(0x0000, 1)
    OP_70(0x0000, 40)
    PlayEffect(0x01, 0x02, 0x0010, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)

    @scena.Lambda('lambda_39E8')
    def lambda_39E8():
        ChrMoveTo(0x00FE, 10580, 500, 9330, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_39E8)

    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x0010, 0x03)
    OP_72(0x0000, 0x0020)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    OP_23(0x0113)
    Fade(500)
    CameraMove(10600, 250, 14510, 0)
    OP_67(0, 4040, -10000, 0)
    CameraSetDistance(5260, 0)
    OP_6C(35000, 0)
    OP_6E(227, 0)
    OP_6F(0x0000, 221)
    OP_70(0x0000, 240)
    OP_7C(0, 300, 5000, 1000)
    PlaySE(136, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 1)
    OP_70(0x0000, 40)
    OP_D8(0x00, 0x01F4)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Sleep(500)

    PlaySE(980, 0x00, 0x64)
    Sleep(1500)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301311V#1020F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B1F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341685V#1069F#5P那时的人形装甲吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C1E')

    def _loc_3B1F(): pass

    label('loc_3B1F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B60',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341686V#054F#5P那时的人形装甲啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C1E')

    def _loc_3B60(): pass

    label('loc_3B60')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BA3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341687V#065F#5P那、那时的人形兵器……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C1E')

    def _loc_3BA3(): pass

    label('loc_3BA3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BE2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341688V#024F#5P那时的人形兵器……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C1E')

    def _loc_3BE2(): pass

    label('loc_3BE2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C1E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341689V#042F#5P那时的人形兵器……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C1E(): pass

    label('loc_3C1E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C53',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341690V#077F#5P好大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D40')

    def _loc_3C53(): pass

    label('loc_3C53')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C8E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341691V#042F#5P怎么这么大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D40')

    def _loc_3C8E(): pass

    label('loc_3C8E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CC9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341692V#523F#5P怎么这么大……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D40')

    def _loc_3CC9(): pass

    label('loc_3CC9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D06',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341693V#065F#5P怎、怎么这么大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D40')

    def _loc_3D06(): pass

    label('loc_3D06')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D40',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341694V#054F#5P怎么这么大啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D40(): pass

    label('loc_3D40')

    ChrTalk(
        0x0102,
        (
            '#0020341695V#1046F#5P极限级战略人形兵器\n',
            '『帕蒂尔·玛蒂尔』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 13)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0004)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_3DA5')
    def lambda_3DA5():
        CameraMove(10070, 250, 13790, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3DA5)

    ChrJumpTo(0x0008, 4070, 3600, 7090, 4000, 8000)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    PlaySE(164, 0x00, 0x64)
    Sleep(300)

    ChrSetFlags(0x0008, 0x0010)
    ChrSetDirection(0x0008, 225, 400)
    ChrClearFlags(0x0008, 0x0010)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341696V#1306F#5P让还是孩子的玲待在『结社』\n',
            '本身就是一种错误……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341697V如果就这样长大的话，\n',
            '一切都会变得无法挽回……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 461)
    OP_70(0x0000, 480)
    PlaySE(277, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_6F(0x0000, 381)
    OP_70(0x0000, 420)
    Sleep(500)

    @scena.Lambda('lambda_3EBE')
    def lambda_3EBE():
        CameraMove(12860, 250, 16720, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EBE)

    @scena.Lambda('lambda_3ED6')
    def lambda_3ED6():
        OP_67(0, 3800, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3ED6)

    @scena.Lambda('lambda_3EEE')
    def lambda_3EEE():
        CameraSetDistance(5000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3EEE)

    @scena.Lambda('lambda_3EFE')
    def lambda_3EFE():
        OP_6C(35000, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3EFE)

    @scena.Lambda('lambda_3F0E')
    def lambda_3F0E():
        OP_6E(227, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3F0E)

    PlaySE(163, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 13)

    @scena.Lambda('lambda_3F2D')
    def lambda_3F2D():
        OP_99(0x00FE, 0x00, 0x02, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3F2D)

    ChrJumpTo(0x0008, 7320, 3200, 10100, 2500, 8000)
    OP_CF(0x0008, 0x00, 'Frame85__ren')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xA5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 6)
    ChrSetChipByIndex(0x0008, 3)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0220341698V#1301F#5P全都是骗人的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341699V被『结社』收留之后，\n',
            '玲才遇到真正的爸爸妈妈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341700V才能成为这世上最幸福的女孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341701V#1002F#5P……玲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0220341702V#263F#5P如果艾丝蒂尔你想要否定这点，\n',
            '你就是玲的敌人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341703V#1304F被爸爸妈妈捏碎，\n',
            '在痛苦中死去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Battle(0x00000453, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_40E3'),
        (-1, 'loc_40E8'),
    )

    def _loc_40E3(): pass

    label('loc_40E3')

    OP_B4(0x00)

    Jump('loc_40E8')

    def _loc_40E8(): pass

    label('loc_40E8')

    Return()

# id: 0x0008 offset: 0x40E9
@scena.Code('func_08_40E9')
def func_08_40E9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0009, 0x0004)
    Call(0, 0x000B)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0003, 8)
    OP_70(0x0004, 8)
    OP_70(0x0005, 8)
    OP_70(0x0006, 8)
    OP_70(0x0007, 8)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0000, 0x0004)
    OP_A1(0x0010, 0x0000)
    ChrSetPos(0x0010, 10580, 500, 9330, 225)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 381)
    OP_70(0x0000, 420)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0001)

    ExecExpressionWithValue(
        0x0010,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x34,
        (
            (Expr.PushLong, 0xEA60),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000040)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0101, 1200, 0, 1200, 45)
    ChrSetPos(0x0102, 870, 0, 2560, 45)
    ChrSetPos(0x00F8, -50, 0, 110, 45)
    ChrSetPos(0x00F9, -450, 0, 1740, 45)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F8, 8)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x00F9, 9)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 1220, 950, 12420, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 7)
    ChrSetChipByIndex(0x0008, 3)
    ChrClearFlags(0x0008, 0x0001)
    OP_CF(0x0008, 0x00, 'Frame85__ren')
    CameraMove(4920, 2480, 5190, 0)
    OP_67(0, 3420, -10000, 0)
    CameraSetDistance(4470, 0)
    OP_6C(15000, 0)
    OP_6E(243, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43A8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341704V#1070F呜……怎么这么坚固！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449B')

    def _loc_43A8(): pass

    label('loc_43A8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_43E6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341705V#057F可恶……怎么这么坚固！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449B')

    def _loc_43E6(): pass

    label('loc_43E6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4424',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341706V#561F啊呜……太坚固了啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449B')

    def _loc_4424(): pass

    label('loc_4424')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4460',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341707V#523F呜，怎么这么坚固啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_449B')

    def _loc_4460(): pass

    label('loc_4460')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_449B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341708V#043F……怎么这么坚固……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_449B(): pass

    label('loc_449B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_44EA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341709V#077F力量和装甲\n',
            '全都在『幻想乐曲』之上吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4627')

    def _loc_44EA(): pass

    label('loc_44EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_453D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341710V#043F无论力量还是装甲，\n',
            '都在『幻想乐曲』之上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4627')

    def _loc_453D(): pass

    label('loc_453D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_458A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341711V#523F力量和装甲\n',
            '都在『幻想乐曲』之上啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4627')

    def _loc_458A(): pass

    label('loc_458A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45D9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341712V#065F力量和装甲\n',
            '竟然都在『幻想乐曲』之上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4627')

    def _loc_45D9(): pass

    label('loc_45D9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4627',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341713V#057F力量和装甲\n',
            '都凌驾在『幻想乐曲』之上啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4627(): pass

    label('loc_4627')

    ChrTalk(
        0x0008,
        (
            '#0220341714V#1302F#6P……真难缠啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341715V#263F好吧，我玩腻了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220341716V#1304F『帕蒂尔·玛蒂尔』！\n',
            '以最大能量将艾丝蒂尔他们一举歼灭——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(153, 0x00, 0x64)
    OP_23(0x00EB)
    OP_1F(0x5A, 0x000007D0)
    Fade(500)
    CameraSetDistance(4270, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x81, 0x02)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x83, 0x02)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47B1',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_47EF')

    def _loc_47B1(): pass

    label('loc_47B1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47D8',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_47EF')

    def _loc_47D8(): pass

    label('loc_47D8')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_47EF(): pass

    label('loc_47EF')

    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4853',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4891')

    def _loc_4853(): pass

    label('loc_4853')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_487A',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_4891')

    def _loc_487A(): pass

    label('loc_487A')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_4891(): pass

    label('loc_4891')

    Sleep(1000)

    @scena.Lambda('lambda_489C')
    def lambda_489C():
        CameraMove(2470, 950, 15540, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_489C)

    @scena.Lambda('lambda_48B4')
    def lambda_48B4():
        OP_67(0, 3980, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48B4)

    @scena.Lambda('lambda_48CC')
    def lambda_48CC():
        CameraSetDistance(4400, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_48CC)

    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    Sleep(500)

    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 60)
    Sleep(100)

    OP_72(0x0005, 0x0020)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 60)
    Sleep(100)

    OP_72(0x0006, 0x0020)
    OP_6F(0x0006, 0)
    OP_70(0x0006, 60)
    Sleep(100)

    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 60)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)

    @scena.Lambda('lambda_4968')
    def lambda_4968():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4968)

    @scena.Lambda('lambda_4976')
    def lambda_4976():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4976)

    Sleep(100)

    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)

    @scena.Lambda('lambda_499D')
    def lambda_499D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_499D)

    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0220341717V#264F#8P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_1F(0x64, 0x000007D0)
    Fade(1000)
    CameraMove(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    @scena.Lambda('lambda_4A20')
    def lambda_4A20():
        CameraSetDistance(5500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4A20)

    Sleep(500)

    PlaySE(313, 0x00, 0x64)
    LoadEffect(0x02, 'map\\mp049_02.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    StopEffect(0x80, 0x00)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1707._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x4AA6
@scena.Code('func_09_4AA6')
def func_09_4AA6():
    ChrJumpTo(0x00FE, 600, 0, 9970, 500, 10000)
    ChrJumpTo(0x00FE, 1010, 950, 12180, 1500, 10000)
    ChrClearFlags(0x0008, 0x0020)
    ChrClearFlags(0x0008, 0x0004)

    Return()

# id: 0x000A offset: 0x4ADF
@scena.Code('func_0A_4ADF')
def func_0A_4ADF():
    ChrJumpTo(0x00FE, 460, 0, 7090, 1000, 12000)
    ChrJumpTo(0x00FE, 740, 0, 6540, 1000, 12000)

    Return()

# id: 0x000B offset: 0x4B0E
@scena.Code('func_0B_4B0E')
def func_0B_4B0E():
    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4B2F'),
        (0x00000005, 'loc_4B3C'),
        (0x00000004, 'loc_4B49'),
        (0x00000006, 'loc_4B56'),
        (0x00000007, 'loc_4B63'),
        (0x00000008, 'loc_4B70'),
        (-1, 'loc_4B7D'),
    )

    def _loc_4B2F(): pass

    label('loc_4B2F')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B3C(): pass

    label('loc_4B3C')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B49(): pass

    label('loc_4B49')

    LoadChip('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B56(): pass

    label('loc_4B56')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B63(): pass

    label('loc_4B63')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B70(): pass

    label('loc_4B70')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 8)

    Jump('loc_4B7D')

    def _loc_4B7D(): pass

    label('loc_4B7D')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_4B9E'),
        (0x00000005, 'loc_4BAB'),
        (0x00000004, 'loc_4BB8'),
        (0x00000006, 'loc_4BC5'),
        (0x00000007, 'loc_4BD2'),
        (0x00000008, 'loc_4BDF'),
        (-1, 'loc_4BEC'),
    )

    def _loc_4B9E(): pass

    label('loc_4B9E')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BAB(): pass

    label('loc_4BAB')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BB8(): pass

    label('loc_4BB8')

    LoadChip('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BC5(): pass

    label('loc_4BC5')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BD2(): pass

    label('loc_4BD2')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BDF(): pass

    label('loc_4BDF')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 9)

    Jump('loc_4BEC')

    def _loc_4BEC(): pass

    label('loc_4BEC')

    Return()

# id: 0x000C offset: 0x4BED
@scena.Code('func_0C_4BED')
def func_0C_4BED():
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
        (0x00000000, 'loc_4C67'),
        (0x00000001, 'loc_4C6D'),
        (-1, 'loc_4C73'),
    )

    def _loc_4C67(): pass

    label('loc_4C67')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4C73')

    def _loc_4C6D(): pass

    label('loc_4C6D')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4C73')

    def _loc_4C73(): pass

    label('loc_4C73')

    Return()

# id: 0x000D offset: 0x4C74
@scena.Code('func_0D_4C74')
def func_0D_4C74():
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
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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
