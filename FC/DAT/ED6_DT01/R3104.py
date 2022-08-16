import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
    header.bgm            = 20
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
            word_3A         = 144,
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
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
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

# id: 0x10002 offset: 0x1AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1AA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1AA
@scena.Code('Init')
def Init():
    MapClearFlags(0x40000000)
    FormationAddMember(0xFF, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1C2'),
        (0x00000065, 'loc_1D5'),
        (-1, 'loc_1E8'),
    )

    def _loc_1C2(): pass

    label('loc_1C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 1, 0x539)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D2',
    )

    Event(0, func_03_3BA)

    def _loc_1D2(): pass

    label('loc_1D2')

    Jump('loc_1E8')

    def _loc_1D5(): pass

    label('loc_1D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 3, 0x53B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E5',
    )

    Event(0, func_05_1242)

    def _loc_1E5(): pass

    label('loc_1E5')

    Jump('loc_1E8')

    def _loc_1E8(): pass

    label('loc_1E8')

    Return()

# id: 0x0001 offset: 0x1E9
@scena.Code('func_01_1E9')
def func_01_1E9():
    OP_16(0x02, 4000, -131000, -126000, 196657)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_210',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_228',
    )

    OP_B1('R3104_y')

    Jump('loc_231')

    def _loc_228(): pass

    label('loc_228')

    OP_B1('R3104_n')

    def _loc_231(): pass

    label('loc_231')

    Return()

# id: 0x0002 offset: 0x232
@scena.Code('func_02_232')
def func_02_232():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_262',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3A4')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3A4')

    def _loc_27B(): pass

    label('loc_27B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_294',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3A4')

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2AD',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3A4')

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C6',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3A4')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3A4')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3A4')

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_311',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3A4')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3A4')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_343',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3A4')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_35C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3A4')

    def _loc_35C(): pass

    label('loc_35C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_375',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3A4')

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3A4')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A4',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3A4(): pass

    label('loc_3A4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3A4')

    def _loc_3B9(): pass

    label('loc_3B9')

    Return()

# id: 0x0003 offset: 0x3BA
@scena.Code('func_03_3BA')
def func_03_3BA():
    EventBegin(0x00)
    CameraMove(620, -50, -47670, 0)
    ChrSetPos(0x0101, 430, -70, -48480, 0)
    ChrSetPos(0x0106, 950, -90, -49600, 0)
    ChrSetPos(0x0102, -1020, -40, -49790, 0)
    FadeIn(1000, 0)
    OP_66(0x0000)

    @scena.Lambda('lambda_0412')
    def lambda_0412():
        OP_67(-22360, 30130, -70650, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0412)

    CameraMove(270, 5050, -6000, 6000)
    Fade(1000)
    OP_66(0x0001)
    CameraMove(380, 650, -19840, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 380, -100, -22070, 0)
    ChrSetPos(0x0106, 1170, -30, -23100, 0)
    ChrSetPos(0x0102, -1140, -60, -23590, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010081114V#002F这里就是『红莲之塔』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081115V博士真的被那帮家伙\n',
            '掳到这种地方来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081116V#552F看来没错……\n',
            '地上有很多纷乱的脚印。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081117V而且这里作为藏身之处\n',
            '确实是最合适不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    PlaySE(501, 0x00, 0x64)
    ChrSetChipByIndex(0x0102, 4)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020081118V#016F你们两个小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05D8')
    def lambda_05D8():
        OP_6C(32000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_05D8)

    CameraMove(-150, 3850, -10760, 2000)
    ChrSetPos(0x0008, -1210, 5050, -5570, 0)
    ChrSetPos(0x0009, -670, 4650, -6550, 0)
    ChrSetPos(0x000A, 260, 5050, -5940, 0)
    ChrSetPos(0x000B, 990, 5050, -5750, 0)
    ChrSetPos(0x000C, 1500, 5050, -5570, 0)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)

    @scena.Lambda('lambda_0667')
    def lambda_0667():
        CameraMove(400, 650, -19840, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0667)

    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0106, 6)
    ChrClearFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_068E')
    def lambda_068E():
        ChrWalkTo(0x00FE, -1050, 1050, -18590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_068E)

    Sleep(200)

    ChrClearFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_06B3')
    def lambda_06B3():
        ChrWalkTo(0x00FE, 1370, 1050, -18490, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_06B3)

    Sleep(500)

    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_06D8')
    def lambda_06D8():
        ChrWalkTo(0x00FE, 30, 1050, -18840, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06D8)

    Sleep(500)

    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        ChrWalkTo(0x00FE, -500, 1450, -17110, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06FD)

    Sleep(200)

    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0722')
    def lambda_0722():
        ChrWalkTo(0x00FE, 740, 1450, -17090, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0722)

    CreateThread(0x0106, 0x00, 0x00, func_04_120F)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_074E')
    def lambda_074E():
        ChrJumpTo(0x00FE, -2490, 3050, -21420, 2500, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_074E)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetFlags(0x000C, 0x0004)
    ChrJumpTo(0x000C, 2510, 3050, -21420, 2500, 7000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010081119V#005F这些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081120V#054F哼……\n',
            '果然押对了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_07FA')
    def lambda_07FA():
        ChrWalkTo(0x00FE, 160, -50, -33290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07FA)

    @scena.Lambda('lambda_0815')
    def lambda_0815():
        ChrWalkTo(0x00FE, 160, -50, -33290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0815)

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        ChrWalkTo(0x00FE, 160, -50, -33290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0830)

    Sleep(150)

    TerminateThread(0x0008, 0xFF)
    ChrSetChipByIndex(0x0008, 1)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x0008, 0x0101, 0)

    @scena.Lambda('lambda_086B')
    def lambda_086B():
        ChrJumpTo(0x00FE, -130, -90, -23660, 900, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_086B)

    Sleep(100)

    TerminateThread(0x000C, 0xFF)
    ChrSetChipByIndex(0x000C, 1)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTurnDirection(0x000C, 0x0101, 0)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        ChrJumpTo(0x00FE, -130, -90, -23660, 900, 7000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_08A9)

    Sleep(250)

    Battle(0x000003A6, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_8DF'),
        (-1, 'loc_8E2'),
    )

    def _loc_8DF(): pass

    label('loc_8DF')

    OP_B4(0x00)

    Return()

    def _loc_8E2(): pass

    label('loc_8E2')

    EventBegin(0x00)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0101, 380, -100, -22070, 0)
    ChrSetPos(0x0106, 880, -30, -23670, 0)
    ChrSetPos(0x0102, -1140, -60, -23590, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0106, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    CameraMove(310, -90, -21210, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010081121V#002F#5P可是……\n',
            '为什么那些魔兽会在这里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081122V#004F啊，难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09D0')
    def lambda_09D0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_09D0)

    @scena.Lambda('lambda_09DE')
    def lambda_09DE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09DE)

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
            TXT(0x00, '「只是单纯的巧合？」\n'),
            TXT(0x01, '「是在这座塔里栖息的吗？」\n'),
            TXT(0x02, '「和那伙黑衣人有关系吗？」\n'),
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
        (0x00000000, 'loc_A86'),
        (0x00000001, 'loc_BD2'),
        (0x00000002, 'loc_D25'),
        (-1, 'loc_DB8'),
    )

    def _loc_A86(): pass

    label('loc_A86')

    ChrTalk(
        0x0101,
        (
            '#0010081123V#005F#5P只是单纯的巧合？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081124V#053F傻丫头，怎么可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 600)

    ChrTalk(
        0x0101,
        (
            '#0010081125V#509F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081126V#012F虽然可能是巧合……\n',
            '但从以前和它们交战的记录来看，\n',
            '更可能是那些黑衣人所做的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081127V#057F啊啊，不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081128V恐怕那些魔兽\n',
            '就是他们训练出来的战斗犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB8')

    def _loc_BD2(): pass

    label('loc_BD2')

    ChrTalk(
        0x0101,
        (
            '#0010081129V#005F#5P它们栖息在这塔里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081130V#053F傻丫头，怎么可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 600)

    ChrTalk(
        0x0101,
        (
            '#0010081131V#509F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081132V#012F虽然可能是巧合……\n',
            '但从以前和它们交战的记录来看，\n',
            '更可能是那些黑衣人所做的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081133V#057F啊啊，不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081134V恐怕那些魔兽\n',
            '就是他们训练出来的战斗犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0041, 0x0001)

    Jump('loc_DB8')

    def _loc_D25(): pass

    label('loc_D25')

    ChrTalk(
        0x0101,
        (
            '#0010081135V#005F#5P和黑衣人有关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081136V#057F啊啊，不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081137V恐怕那些魔兽\n',
            '就是他们训练出来的战斗犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0041, 0x0003)
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_DB8')

    def _loc_DB8(): pass

    label('loc_DB8')

    @scena.Lambda('lambda_0DBE')
    def lambda_0DBE():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DBE)

    ChrTalk(
        0x0101,
        (
            '#0010081138V#580F#5P战、战斗犬……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081139V#552F我从调查他们开始，\n',
            '就接连受到那种魔兽的袭击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081140V那些疯狗应该是那些家伙养的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081141V#007F#5P是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010081142V#005F这么说……\n',
            '我们上次在山顶关所遭袭击，\n',
            '都是拜你所赐的啦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081143V#053F啊，追根究底算是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081144V#050F别忘记了，把调查他们的任务强塞给我的\n',
            '就是你们的好老爸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081145V不知道谁才是受害者呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081146V#509F#5P唔，被你这样一说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081147V#012F对了，阿加特兄。\n',
            '之前嘉恩先生也说起过这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081148V可以告诉我们这件事的来龙去脉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081149V#551F你们的老爸是在空贼事件发生之前\n',
            '突然过来要我调查这件事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081150V说什么自己有其他要事去做，\n',
            '丢下几句话就马上溜掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081151V真是的，大叔就爱装傻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081152V#505F#5P是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081153V#057F不过事到如今，\n',
            '我也下定决心一定要调查到底。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081154V特别是那个混蛋，\n',
            '我一定要亲手抓到他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081155V#002F#5P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081156V#014F那个混蛋……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081157V#552F……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081158V总之赶快抓到那帮家伙，\n',
            '把老爷子救出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00A7, 1, 0x539))
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x120F
@scena.Code('func_04_120F')
def func_04_120F():
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 0)
    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 0)
    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 0)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 0)

    Return()

# id: 0x0005 offset: 0x1242
@scena.Code('func_05_1242')
def func_05_1242():
    EventBegin(0x00)
    CameraMove(120, 5050, -5370, 0)
    ChrSetPos(0x0101, 0, 5050, -5210, 0)
    ChrSetPos(0x0102, -830, 5050, -5210, 0)
    ChrSetPos(0x0107, 900, 5050, -5210, 0)
    ChrSetPos(0x0106, 0, 5050, -5210, 0)

    @scena.Lambda('lambda_129F')
    def lambda_129F():
        CameraMove(250, 3850, -10670, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_129F)

    @scena.Lambda('lambda_12B7')
    def lambda_12B7():
        ChrWalkTo(0x00FE, -10, 3850, -11850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12B7)

    Sleep(400)

    @scena.Lambda('lambda_12D7')
    def lambda_12D7():
        ChrWalkTo(0x00FE, -1070, 3850, -11400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_12D7)

    Sleep(200)

    @scena.Lambda('lambda_12F7')
    def lambda_12F7():
        ChrWalkTo(0x00FE, 710, 3850, -10180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_12F7)

    Sleep(200)

    @scena.Lambda('lambda_1317')
    def lambda_1317():
        ChrWalkTo(0x00FE, 80, 3850, -9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1317)

    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050081298V#053F……唔……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0106, 30, 0, 600, 3000)

    @scena.Lambda('lambda_136A')
    def lambda_136A():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_136A)

    @scena.Lambda('lambda_1378')
    def lambda_1378():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1378)

    @scena.Lambda('lambda_1386')
    def lambda_1386():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1386)

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081299V#004F怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081300V#552F不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081301V只是有点头晕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081302V#065F#2P啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081303V难、难道是\n',
            '在保护我的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081304V#004F这、这么说来……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081305V#012F难道说……\n',
            '你被他们导力弹打中了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081306V#053F只是擦伤一点而已。\n',
            '没什么大碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070081307V#063F#2P但、但是……\n',
            '都怪我不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050081308V#055F不怕告诉你们，\n',
            '这种小伤对我来说根本是家常便饭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050081309V别再说废话了，\n',
            '加快脚步回蔡斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010081310V#002F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020081311V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00A7, 3, 0x53B))
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
