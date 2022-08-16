import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3104   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3104.x'
    header.mapIndex       = 1
    header.bgm            = 29
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '托兰特平原道方向',
            x                   = 50,
            z                   = -130,
            y                   = -59690,
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

# id: 0x10002 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2800,
            y           = -2000,
            z           = -54300,
            range       = 2800,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFF3030,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -16800,
            y           = -5000,
            z           = -24500,
            range       = 14800,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFFAB3C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -2700,
            y           = -6100,
            z           = -8640,
            range       = 2700,
            dword_10    = 0x00002710,
            dword_14    = 0xFFFFECDC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10004 offset: 0x128
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x128
@scena.Code('Init')
def Init():
    ClearScenaFlags(ScenaFlag(0x02B0, 0, 0x1580))
    ClearScenaFlags(ScenaFlag(0x02B0, 1, 0x1581))
    ClearScenaFlags(ScenaFlag(0x02B0, 2, 0x1582))
    ClearScenaFlags(ScenaFlag(0x02B0, 3, 0x1583))
    ClearScenaFlags(ScenaFlag(0x02B0, 4, 0x1584))
    ClearScenaFlags(ScenaFlag(0x02B0, 5, 0x1585))
    ClearScenaFlags(ScenaFlag(0x02B0, 6, 0x1586))
    ClearScenaFlags(ScenaFlag(0x02B0, 7, 0x1587))
    ClearScenaFlags(ScenaFlag(0x02B1, 0, 0x1588))
    ClearScenaFlags(ScenaFlag(0x02B1, 1, 0x1589))
    ClearScenaFlags(ScenaFlag(0x02B1, 2, 0x158A))
    ClearScenaFlags(ScenaFlag(0x02B1, 3, 0x158B))
    ClearScenaFlags(ScenaFlag(0x02B1, 4, 0x158C))
    ClearScenaFlags(ScenaFlag(0x02B1, 5, 0x158D))
    ClearScenaFlags(ScenaFlag(0x02B1, 6, 0x158E))
    ClearScenaFlags(ScenaFlag(0x02B1, 7, 0x158F))
    ClearScenaFlags(ScenaFlag(0x02B2, 0, 0x1590))
    ClearScenaFlags(ScenaFlag(0x02B2, 1, 0x1591))
    ClearScenaFlags(ScenaFlag(0x02B2, 2, 0x1592))
    ClearScenaFlags(ScenaFlag(0x02B2, 3, 0x1593))
    ClearScenaFlags(ScenaFlag(0x02B2, 4, 0x1594))
    ClearScenaFlags(ScenaFlag(0x03D6, 5, 0x1EB5))
    ClearScenaFlags(ScenaFlag(0x03D6, 6, 0x1EB6))
    ClearScenaFlags(ScenaFlag(0x03D6, 7, 0x1EB7))
    ClearScenaFlags(ScenaFlag(0x03D7, 0, 0x1EB8))
    ClearScenaFlags(ScenaFlag(0x03D7, 1, 0x1EB9))
    ClearScenaFlags(ScenaFlag(0x03D7, 2, 0x1EBA))
    ClearScenaFlags(ScenaFlag(0x03D7, 3, 0x1EBB))
    ClearScenaFlags(ScenaFlag(0x03D7, 4, 0x1EBC))
    ClearScenaFlags(ScenaFlag(0x03D7, 5, 0x1EBD))
    ClearScenaFlags(ScenaFlag(0x03D7, 6, 0x1EBE))
    ClearScenaFlags(ScenaFlag(0x03D7, 7, 0x1EBF))
    ClearScenaFlags(ScenaFlag(0x03D8, 0, 0x1EC0))
    ClearScenaFlags(ScenaFlag(0x03D8, 1, 0x1EC1))
    ClearScenaFlags(ScenaFlag(0x03D8, 2, 0x1EC2))
    ClearScenaFlags(ScenaFlag(0x03D8, 3, 0x1EC3))
    ClearScenaFlags(ScenaFlag(0x03D8, 4, 0x1EC4))
    ClearScenaFlags(ScenaFlag(0x03D8, 5, 0x1EC5))
    ClearScenaFlags(ScenaFlag(0x03D8, 6, 0x1EC6))
    ClearScenaFlags(ScenaFlag(0x03D8, 7, 0x1EC7))
    ClearScenaFlags(ScenaFlag(0x03D9, 0, 0x1EC8))
    ClearScenaFlags(ScenaFlag(0x03D9, 1, 0x1EC9))
    ClearScenaFlags(ScenaFlag(0x03D9, 2, 0x1ECA))
    ClearScenaFlags(ScenaFlag(0x03D9, 3, 0x1ECB))
    ClearScenaFlags(ScenaFlag(0x03D9, 4, 0x1ECC))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1C5',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_342)

    Jump('loc_1D5')

    def _loc_1C5(): pass

    label('loc_1C5')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D5',
    )

    Event(0, func_0C_F43)

    def _loc_1D5(): pass

    label('loc_1D5')

    Return()

# id: 0x0001 offset: 0x1D6
@scena.Code('func_01_1D6')
def func_01_1D6():
    OP_16(0x02, 4000, -131000, -126000, 2293809)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_202',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_202(): pass

    label('loc_202')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_214',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    def _loc_214(): pass

    label('loc_214')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_223',
    )

    Jump('loc_273')

    def _loc_223(): pass

    label('loc_223')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_273',
    )

    LoadEffect(0x00, 'map\\\\mp086_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 6000, -8100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_273(): pass

    label('loc_273')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C',
    )

    OP_10(0x01, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_292')

    def _loc_28C(): pass

    label('loc_28C')

    OP_10(0x01, 0x01)
    OP_10(0x03, 0x00)

    def _loc_292(): pass

    label('loc_292')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_341',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2F0',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_341')

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_305',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_341')

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31A',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_341')

    def _loc_31A(): pass

    label('loc_31A')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_341')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_341(): pass

    label('loc_341')

    Return()

# id: 0x0002 offset: 0x342
@scena.Code('func_02_342')
def func_02_342():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 4, 0x1E0C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51B',
    )

    CameraMove(310, -60, -23970, 0)
    OP_67(0, 9550, -10000, 0)
    CameraSetDistance(3990, 0)
    OP_6C(45000, 0)
    OP_6E(298, 0)
    ChrSetPos(0x0101, 900, -70, -55000, 0)
    ChrSetPos(0x0102, -400, -160, -55410, 0)
    ChrSetPos(0x0108, 720, -80, -56490, 0)
    ChrSetPos(0x00F9, -570, -130, -56740, 0)

    @scena.Lambda('lambda_03D3')
    def lambda_03D3():
        CameraMove(730, -60, -45850, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03D3)

    OP_C8(0x0200, 0x0046, 'C_PLAC20._CH', 0x00, 0x03E8)
    ShowPlaceName('红莲之塔')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_0419')
    def lambda_0419():
        ChrWalkTo(0x00FE, 1150, -50, -47150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0419)

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        ChrWalkTo(0x00FE, -10, -80, -47440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0434)

    @scena.Lambda('lambda_044F')
    def lambda_044F():
        ChrWalkTo(0x00FE, 1270, -60, -48500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0000, lambda_044F)

    @scena.Lambda('lambda_046A')
    def lambda_046A():
        ChrWalkTo(0x00FE, -330, -110, -48990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_046A)

    WaitForThreadExit(0x0101, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-120, -90, -48500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrSetPos(0x0000, -120, -90, -48500, 0)
    ChrSetPos(0x0001, -120, -90, -48500, 0)
    ChrSetPos(0x0002, -120, -90, -48500, 0)
    ChrSetPos(0x0003, -120, -90, -48500, 0)
    SetScenaFlags(ScenaFlag(0x03C1, 4, 0x1E0C))

    Jump('loc_59C')

    def _loc_51B(): pass

    label('loc_51B')

    CameraMove(-120, -90, -48500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -120, -90, -48500, 0)
    ChrSetPos(0x0001, -120, -90, -48500, 0)
    ChrSetPos(0x0002, -120, -90, -48500, 0)
    ChrSetPos(0x0003, -120, -90, -48500, 0)

    def _loc_59C(): pass

    label('loc_59C')

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0003 offset: 0x5AD
@scena.Code('func_03_5AD')
def func_03_5AD():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 4, 0x1E0C)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5BF',
    )

    Return()

    def _loc_5BF(): pass

    label('loc_5BF')

    EventBegin(0x01)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要回『埃尔赛尤』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
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
        0,
        (
            TXT(0x00, '【回船上】\n'),
            TXT(0x01, '【不回去】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65B',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_67B')

    def _loc_65B(): pass

    label('loc_65B')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_67B(): pass

    label('loc_67B')

    Return()

# id: 0x0004 offset: 0x67C
@scena.Code('func_04_67C')
def func_04_67C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 4, 0x1E0C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 5, 0x1E0D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_689',
    )

    Return()

    def _loc_689(): pass

    label('loc_689')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6AE',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_6AE(): pass

    label('loc_6AE')

    Fade(1000)
    CameraMove(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    CameraSetDistance(2760, 0)
    OP_6C(9000, 0)
    OP_6E(572, 0)
    ChrSetPos(0x0101, 900, 250, -20540, 0)
    ChrSetPos(0x0102, -520, 250, -20720, 0)
    ChrSetPos(0x0108, 800, -90, -22200, 0)
    ChrSetPos(0x00F9, -570, -90, -22350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341027V#1002F#2P和『翡翠之塔』一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341028V还是和那个不知所谓的\n',
            '地方连着吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_822',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341029V#057F#5P这才是它们原本的姿态，\n',
            '也就是所谓的『里塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341030V#1042F#5P嗯……\n',
            '应该没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3C')

    def _loc_822(): pass

    label('loc_822')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341031V#022F#5P这才是它们原本的姿态，\n',
            '也就是所谓的『里塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341030V#1042F#5P嗯……\n',
            '应该没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3C')

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_933',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341033V#1063F#5P这才是它们原本的姿态，\n',
            '也就是所谓的『里塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341030V#1042F#5P嗯……\n',
            '应该没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3C')

    def _loc_933(): pass

    label('loc_933')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9B9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341035V#043F#5P这才是它们原本的姿态，\n',
            '也就是所谓的『里塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341036V#1042F#5P嗯……\n',
            '应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A3C')

    def _loc_9B9(): pass

    label('loc_9B9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341037V#065F#5P这才是它们原本的姿态，\n',
            '也就是所谓的『里塔』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341036V#1042F#5P嗯……\n',
            '应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A3C(): pass

    label('loc_A3C')

    ChrTalk(
        0x0108,
        (
            '#0080341039V#070F总之，这种地方\n',
            '可不能用常理来判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341040V打起精神前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A9A')
    def lambda_0A9A():
        OP_69(0x0000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0A9A)

    @scena.Lambda('lambda_0AA8')
    def lambda_0AA8():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0AA8)

    @scena.Lambda('lambda_0AC0')
    def lambda_0AC0():
        CameraSetDistance(3250, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0AC0)

    @scena.Lambda('lambda_0AD0')
    def lambda_0AD0():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0AD0)

    @scena.Lambda('lambda_0AE0')
    def lambda_0AE0():
        OP_6E(262, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0AE0)

    SetScenaFlags(ScenaFlag(0x03C1, 5, 0x1E0D))
    WaitForThreadExit(0x0000, 0x0000)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0005 offset: 0xAFA
@scena.Code('func_05_AFA')
def func_05_AFA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 5, 0x1E0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C1A',
    )

    EventBegin(0x00)
    Fade(500)
    MapClearFlags(0x00000001)
    CameraMove(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    CameraSetDistance(3540, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    CameraMove(290, 3850, -6790, 0)
    OP_67(0, 2730, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    ChrSetPos(0x0101, 620, 3850, -11000, 0)
    ChrSetPos(0x0102, -750, 3850, -11000, 0)
    ChrSetPos(0x0108, 550, 3450, -12660, 0)
    ChrSetPos(0x00F9, -1000, 3450, -12540, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, func_06_C1B)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, func_07_CA0)
    Sleep(300)

    CreateThread(0x0108, 0x00, 0x00, func_08_D25)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_09_DAA)
    WaitForThreadExit(0x0003, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/C3600._SN', 100, 0, 0)
    IdleLoop()

    def _loc_C1A(): pass

    label('loc_C1A')

    Return()

# id: 0x0006 offset: 0xC1B
@scena.Code('func_06_C1B')
def func_06_C1B():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 1500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0C60')
    def lambda_0C60():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C60)

    @scena.Lambda('lambda_0C7A')
    def lambda_0C7A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C7A)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0007 offset: 0xCA0
@scena.Code('func_07_CA0')
def func_07_CA0():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 1500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0CE5')
    def lambda_0CE5():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0CE5)

    @scena.Lambda('lambda_0CFF')
    def lambda_0CFF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0CFF)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0008 offset: 0xD25
@scena.Code('func_08_D25')
def func_08_D25():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 2500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0D6A')
    def lambda_0D6A():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0D6A)

    @scena.Lambda('lambda_0D84')
    def lambda_0D84():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D84)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0009 offset: 0xDAA
@scena.Code('func_09_DAA')
def func_09_DAA():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, 2500, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0DEF')
    def lambda_0DEF():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0DEF)

    @scena.Lambda('lambda_0E09')
    def lambda_0E09():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0E09)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000A offset: 0xE2F
@scena.Code('func_0A_E2F')
def func_0A_E2F():
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
        (0x00000000, 'loc_EA9'),
        (0x00000001, 'loc_EAF'),
        (-1, 'loc_EB5'),
    )

    def _loc_EA9(): pass

    label('loc_EA9')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_EB5')

    def _loc_EAF(): pass

    label('loc_EAF')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_EB5')

    def _loc_EB5(): pass

    label('loc_EB5')

    Return()

# id: 0x000B offset: 0xEB6
@scena.Code('func_0B_EB6')
def func_0B_EB6():
    FadeOut(0, 0, -1)
    CameraMove(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
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

# id: 0x000C offset: 0xF43
@scena.Code('func_0C_F43')
def func_0C_F43():
    EventBegin(0x00)
    CameraMove(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    CameraSetDistance(3540, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    CameraMove(290, 3850, -6790, 0)
    OP_67(0, 2730, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    ChrSetPos(0x0101, 500, 4400, -7730, 180)
    ChrSetPos(0x0102, -500, 4400, -7730, 180)
    ChrSetPos(0x00F8, 500, 4400, -7730, 180)
    ChrSetPos(0x00F9, -500, 4400, -7730, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, func_0D_110C)
    Sleep(800)

    CreateThread(0x0102, 0x00, 0x00, func_0E_1172)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_0F_11D8)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_10_123E)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    CameraMove(-120, 3850, -10670, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -120, 3850, -10670, 180)
    ChrSetPos(0x0001, -120, 3850, -10670, 180)
    ChrSetPos(0x0002, -120, 3850, -10670, 180)
    ChrSetPos(0x0003, -120, 3850, -10670, 180)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x000D offset: 0x110C
@scena.Code('func_0D_110C')
def func_0D_110C():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1117')
    def lambda_1117():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1117)

    @scena.Lambda('lambda_1131')
    def lambda_1131():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1131)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1152')
    def lambda_1152():
        ChrMoveTo(0x00FE, 500, 4000, -10500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1152)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x000E offset: 0x1172
@scena.Code('func_0E_1172')
def func_0E_1172():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_117D')
    def lambda_117D():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_117D)

    @scena.Lambda('lambda_1197')
    def lambda_1197():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1197)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_11B8')
    def lambda_11B8():
        ChrMoveTo(0x00FE, -500, 4000, -10500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_11B8)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x000F offset: 0x11D8
@scena.Code('func_0F_11D8')
def func_0F_11D8():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_11E3')
    def lambda_11E3():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_11E3)

    @scena.Lambda('lambda_11FD')
    def lambda_11FD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_11FD)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_121E')
    def lambda_121E():
        ChrMoveTo(0x00FE, 500, 3600, -9500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_121E)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0010 offset: 0x123E
@scena.Code('func_10_123E')
def func_10_123E():
    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_1249')
    def lambda_1249():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1249)

    @scena.Lambda('lambda_1263')
    def lambda_1263():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1263)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_1284')
    def lambda_1284():
        ChrMoveTo(0x00FE, -500, 3600, -9500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1284)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
