import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3200_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3200_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3200_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    PlaySE(455, 0x01, 0x64)
    ChrSetPos(0x0017, 67620, 3420, 25770, 170)
    ChrSetPos(0x0018, 61980, 3020, 26800, 125)
    ChrSetPos(0x0019, 62800, 3020, 25140, 125)
    ChrSetPos(0x001A, 61950, 3020, 23550, 125)
    ChrSetPos(0x001B, 73010, 3020, 25590, 215)
    ChrSetPos(0x001C, 67620, 3020, 25770, 170)
    ChrSetChipByIndex(0x0101, 19)
    ChrSetChipByIndex(0x0107, 24)
    Sleep(2000)

    FadeIn(1000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_174',
    )

    ChrSetChipByIndex(0x0106, 21)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A',
    )

    ChrSetChipByIndex(0x0105, 23)
    Call(1, 0x000B)

    def _loc_15A(): pass

    label('loc_15A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_171',
    )

    ChrSetChipByIndex(0x0104, 22)
    Call(1, 0x000C)

    def _loc_171(): pass

    label('loc_171')

    Jump('loc_1A7')

    def _loc_174(): pass

    label('loc_174')

    ChrSetChipByIndex(0x0103, 20)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_190',
    )

    ChrSetChipByIndex(0x0105, 23)
    Call(1, 0x000D)

    def _loc_190(): pass

    label('loc_190')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A7',
    )

    ChrSetChipByIndex(0x0104, 22)
    Call(1, 0x000E)

    def _loc_1A7(): pass

    label('loc_1A7')

    Return()

# id: 0x0001 offset: 0x1A8
@scena.Code('func_01_1A8')
def func_01_1A8():
    ChrWalkTo(0x0017, 64530, 3420, 26150, 1000, 0x00)
    ChrWalkTo(0x0017, 58510, 3420, 28540, 1000, 0x00)

    Return()

# id: 0x0002 offset: 0x1D1
@scena.Code('func_02_1D1')
def func_02_1D1():
    ChrWalkTo(0x0017, 58510, 4019, 28540, 5000, 0x00)

    Return()

# id: 0x0003 offset: 0x1E6
@scena.Code('func_03_1E6')
def func_03_1E6():
    OP_4A(0x0017, 255)
    OP_20(0x000007D0)
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x001C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrTurnDirection(0x0018, 0x0101, 0)
    ChrTurnDirection(0x0019, 0x0101, 0)
    ChrTurnDirection(0x001A, 0x0101, 0)
    ChrTurnDirection(0x001C, 0x0101, 0)
    ChrTurnDirection(0x0018, 0x0101, 0)

    @scena.Lambda('lambda_02C5')
    def lambda_02C5():
        ChrTurnDirection(0x0017, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_02C5)

    @scena.Lambda('lambda_02D3')
    def lambda_02D3():
        ChrJumpTo(0x0018, 66090, 4019, 25680, 1400, 2000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_02D3)

    @scena.Lambda('lambda_02F1')
    def lambda_02F1():
        ChrJumpTo(0x0019, 62800, 4019, 25140, 1400, 2000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_02F1)

    @scena.Lambda('lambda_030F')
    def lambda_030F():
        ChrJumpTo(0x001A, 61950, 4019, 23550, 1400, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_030F)

    @scena.Lambda('lambda_032D')
    def lambda_032D():
        ChrJumpTo(0x001C, 67620, 4019, 25770, 1400, 2000)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_032D)

    ChrJumpTo(0x001B, 73010, 4019, 25590, 1400, 2000)
    OP_63(0x0017)
    OP_63(0x0018)
    OP_63(0x0019)
    OP_63(0x001A)
    OP_63(0x001B)
    OP_63(0x001C)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlayBGM(41)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010451467V#444F#2P哈哈！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_23(0x01C7)
    ChrSetChipByIndex(0x0017, 28)
    ChrSetChipByIndex(0x0018, 26)
    ChrSetChipByIndex(0x0019, 26)
    ChrSetChipByIndex(0x001A, 12)
    ChrSetChipByIndex(0x001B, 12)
    ChrSetChipByIndex(0x001C, 12)
    OP_62(0x0017, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0019, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_4B(0x0017, 255)
    CreateThread(0x0017, 0x00, 0x01, 0x0002)

    @scena.Lambda('lambda_044C')
    def lambda_044C():
        ChrWalkTo(0x0018, 57080, 4019, 23300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_044C)

    Sleep(40)

    @scena.Lambda('lambda_046C')
    def lambda_046C():
        ChrWalkTo(0x0019, 57080, 4019, 23300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_046C)

    Sleep(70)

    @scena.Lambda('lambda_048C')
    def lambda_048C():
        ChrWalkTo(0x001A, 57080, 4019, 23300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_048C)

    Sleep(100)

    @scena.Lambda('lambda_04AC')
    def lambda_04AC():
        ChrWalkTo(0x001B, 57080, 4019, 23300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_04AC)

    Sleep(40)

    @scena.Lambda('lambda_04CC')
    def lambda_04CC():
        ChrWalkTo(0x001C, 57080, 4019, 23300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_04CC)

    Return()

# id: 0x0004 offset: 0x4E2
@scena.Code('func_04_4E2')
def func_04_4E2():
    ChrWalkTo(0x0017, 60720, 4019, 26020, 4000, 0x00)
    ChrWalkTo(0x0017, 57360, 4019, 26560, 4000, 0x00)
    ChrWalkTo(0x0017, 54950, 4019, 26560, 4000, 0x00)

    Return()

# id: 0x0005 offset: 0x51F
@scena.Code('func_05_51F')
def func_05_51F():
    ChrWalkTo(0x0018, 57390, 4019, 27410, 4000, 0x00)
    ChrWalkTo(0x0018, 54870, 4019, 27410, 4000, 0x00)

    Return()

# id: 0x0006 offset: 0x548
@scena.Code('func_06_548')
def func_06_548():
    ChrWalkTo(0x0019, 57310, 4019, 22630, 4000, 0x00)
    ChrWalkTo(0x0019, 51880, 4019, 21910, 4000, 0x00)

    Return()

# id: 0x0007 offset: 0x571
@scena.Code('func_07_571')
def func_07_571():
    ChrWalkTo(0x001A, 58370, 4019, 20880, 4000, 0x00)
    ChrWalkTo(0x001A, 52390, 4019, 17770, 4000, 0x00)

    Return()

# id: 0x0008 offset: 0x59A
@scena.Code('func_08_59A')
def func_08_59A():
    ChrWalkTo(0x001B, 67800, 3820, 24990, 4000, 0x00)
    ChrWalkTo(0x001B, 63050, 3920, 25390, 4000, 0x00)
    ChrWalkTo(0x001B, 57730, 4019, 26030, 4000, 0x00)
    ChrWalkTo(0x001B, 54960, 4019, 26030, 4000, 0x00)

    Return()

# id: 0x0009 offset: 0x5EB
@scena.Code('func_09_5EB')
def func_09_5EB():
    ChrWalkTo(0x001C, 63720, 3820, 23820, 4000, 0x00)
    ChrWalkTo(0x001C, 62020, 3820, 21590, 4000, 0x00)
    ChrSetSubChip(0x001C, 1)
    ChrJumpTo(0x001C, 63020, 1000, 19590, 100, 4000)
    PlayEffect(0x01, 0x00, 0x00FF, 63220, 1000, 19590, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlaySE(228, 0x00, 0x64)

    @scena.Lambda('lambda_066F')
    def lambda_066F():
        OP_9E(0x00FE, 30, 0, 800, 2000)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_066F)

    Sleep(800)

    ChrSetDirection(0x001C, 300, 0)
    OP_62(0x001C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x001C, 11)
    ChrSetSubChip(0x001C, 2)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x001C, 61790, 2400, 20420, 2500, 5000)
    ChrSetChipByIndex(0x001C, 11)
    ChrSetSubChip(0x001C, 6)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x001C, 60070, 3820, 21650, 2500, 5000)
    ChrSetChipByIndex(0x001C, 12)
    ChrSetSubChip(0x001C, 0)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x001C, 53300, 4019, 25760, 4000, 0x00)

    Return()

# id: 0x000A offset: 0x711
@scena.Code('func_0A_711')
def func_0A_711():
    TerminateThread(0x0017, 0x00)
    LoadEffect(0x01, 'map\\\\sibuki0.eff')
    OP_EB(0x8F, 0x05)
    OP_EB(0x72, 0x05)
    OP_EB(0x74, 0x01)
    Fade(200)
    CameraMove(67620, 4500, 23820, 0)
    OP_67(0, 8700, -10000, 0)
    OP_6E(262, 0)
    OP_6C(350000, 0)
    OP_0D()

    @scena.Lambda('lambda_0771')
    def lambda_0771():
        ChrWalkTo(0x00FE, 65910, 3420, 25760, 650, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_0771)

    Sleep(200)

    @scena.Lambda('lambda_0791')
    def lambda_0791():
        ChrTurnDirection(0x00FE, 0x0017, 0)
        Yield()

        Jump('lambda_0791')

    DispatchAsync2(0x0101, 0x0003, lambda_0791)

    ChrSetFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_07A7')
    def lambda_07A7():
        ChrWalkTo(0x00FE, 67180, 1000, 22340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07A7)

    ChrTalk(
        0x0101,
        (
            '#0010451464V#372F#3S#10A#5P喂────！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451465V#372F#3S#10A#5P你给我等等──！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    WaitForThreadExit(0x0017, 0x0000)
    OP_20(0x000007D0)
    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0019, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrClearFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_08EE')
    def lambda_08EE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0003, lambda_08EE)

    @scena.Lambda('lambda_08FC')
    def lambda_08FC():
        ChrJumpTo(0x00FE, 65910, 3820, 25760, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_08FC)

    @scena.Lambda('lambda_091A')
    def lambda_091A():
        ChrJumpTo(0x00FE, 62800, 3820, 25140, 1400, 3000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_091A)

    Sleep(50)

    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)

    @scena.Lambda('lambda_094C')
    def lambda_094C():
        ChrJumpTo(0x00FE, 61980, 3820, 26800, 1400, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_094C)

    @scena.Lambda('lambda_096A')
    def lambda_096A():
        ChrJumpTo(0x00FE, 73010, 3820, 25590, 1400, 3000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_096A)

    @scena.Lambda('lambda_0988')
    def lambda_0988():
        ChrJumpTo(0x00FE, 67620, 3820, 25770, 1400, 3000)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_0988)

    Sleep(50)

    ChrClearFlags(0x001A, 0x0080)

    @scena.Lambda('lambda_09B0')
    def lambda_09B0():
        ChrJumpTo(0x00FE, 61950, 3820, 23550, 1400, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_09B0)

    WaitForThreadExit(0x001A, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    PlayBGM(41)
    Sleep(400)

    OP_63(0x0017)
    OP_63(0x0018)
    OP_63(0x0019)
    OP_63(0x001A)
    OP_63(0x001B)
    OP_63(0x001C)
    ChrSetPos(0x00F7, 63100, 1000, 17560, 0)
    ChrSetFlags(0x00F8, 0x0008)
    ChrSetFlags(0x00F9, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010451466V#444F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(41)
    OP_23(0x01C7)

    @scena.Lambda('lambda_0A41')
    def lambda_0A41():
        CameraMove(66470, 4500, 24570, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_0A41)

    @scena.Lambda('lambda_0A59')
    def lambda_0A59():
        OP_6C(302000, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0A59)

    ChrSetChipByIndex(0x0017, 28)
    ChrSetChipByIndex(0x0018, 26)
    ChrSetChipByIndex(0x0019, 26)
    ChrSetChipByIndex(0x001A, 12)
    ChrSetChipByIndex(0x001B, 12)
    ChrSetChipByIndex(0x001C, 12)
    ChrSetSubChip(0x0017, 0)
    ChrSetSubChip(0x0018, 0)
    ChrSetSubChip(0x0019, 0)
    ChrSetSubChip(0x001A, 0)
    ChrSetSubChip(0x001B, 0)
    ChrSetSubChip(0x001C, 0)
    OP_62(0x0017, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0019, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x001C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x0017, 0x01, 0x01, 0x0004)
    CreateThread(0x0018, 0x01, 0x01, 0x0005)
    CreateThread(0x0019, 0x01, 0x01, 0x0006)
    CreateThread(0x001A, 0x01, 0x01, 0x0007)
    CreateThread(0x001B, 0x01, 0x01, 0x0008)
    CreateThread(0x001C, 0x01, 0x01, 0x0009)
    PlaySE(129, 0x00, 0x64)
    Sleep(300)

    PlaySE(129, 0x00, 0x64)
    Sleep(300)

    PlaySE(129, 0x00, 0x64)
    WaitForThreadExit(0x00F7, 0x0000)
    Sleep(500)

    Return()

# id: 0x000B offset: 0xB59
@scena.Code('func_0B_B59')
def func_0B_B59():
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0106, 64610, 1000, 16420, 200)
    ChrSetPos(0x0107, 66280, 1000, 18830, 110)
    ChrSetPos(0x0105, 67940, 1000, 19460, 200)
    Call(1, 0x000F)

    ChrTalk(
        0x0101,
        (
            '#0010451195V#377F#1P啊～真惬意～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451196V嗯，还是\n',
            '露天浴令人心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451263V#1416F#2P嗯，这风也很舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451264V#370F#1P科洛丝以前\n',
            '在这里洗过澡吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060451265V#1410F#2P不，这是我的第一次露天浴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451266V#1415F以前因公来这里的时候\n',
            '只是洗过室内浴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451267V#370F#2P哦，这样啊。\n',
            '就是说你以前来过这里喽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451268V#442F呼，不过说起来\n',
            '一边看着蓝天一边洗澡的\n',
            '感觉真不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451269V#395F#1P嘿嘿，确实，\n',
            '上回是晚上呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451270V#396F现在已经是晌午了，\n',
            '不过一早来洗的话也很舒服哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451271V外边的空气比较凉，\n',
            '也更能感觉到澡堂的温暖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E0C')
    def lambda_0E0C():
        ChrTurnDirection(0x0105, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0E0C)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451272V#370F#2P不愧是土生土长的孩子，知道得真清楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451273V顺便问一下，提妲最喜欢\n',
            '什么时候来洗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451274V#390F#1P嗯，早晚我都\n',
            '很喜欢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451275V#396F啊，不过论季节的话，\n',
            '下雪的时候最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451276V#374F#2P下、下雪！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451277V那是隆冬吧。\n',
            '赤身裸体的不冷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451278V#396F#1P只要泡在热水里就没问题哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451279V#395F周围都在下雪，\n',
            '可只有自己的身体是暖洋洋的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451280V那种不可思议的感觉\n',
            '总觉得很喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451281V#1416F#2P真美妙啊。\n',
            '雪中的露天浴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451282V#371F#2P嗯嗯，真想\n',
            '尝试一回啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1076')
    def lambda_1076():
        CameraMove(65670, 1000, 18470, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1076)

    ChrTurnDirection(0x0106, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050451283V#1425F#1P喂，聊天是可以，\n',
            '不过别太入迷了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451284V尤其是艾丝蒂尔，\n',
            '你可是在执行任务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1109')
    def lambda_1109():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1109)

    Sleep(350)

    @scena.Lambda('lambda_111C')
    def lambda_111C():
        ChrTurnDirection(0x0107, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_111C)

    Sleep(100)

    ChrSetDirection(0x0105, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451285V#445F#2P嗯、嗯……\n',
            '知道了，不过阿加特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451286V#444F#2P你、你为什么要\n',
            '披着一块印花大手巾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451287V老实说你那个样子\n',
            '特别惹人注目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070451219V#395F#1P这、这个么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451220V#1422F#1P什么注目不注目的\n',
            '我才不在乎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451221V没这东西的话\n',
            '我就提不起精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451291V#442F#2P嗯，虽说这属于\n',
            '个人的自由……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451292V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451293V#374F不过你不会连洗头时\n',
            '都扎着头巾吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451225V#1426F#1P#3S啊──！\n',
            '你用常识考虑一下啊，常识！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451226V那种时候\n',
            '当然要拿下来了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451227V#377F#2P哈……还好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451228V#395F#1P嘿嘿……\n',
            '是、是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451229V果然还是会摘下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451230V#1424F#1P你、你们都是傻瓜吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451231V把我当成是\n',
            '什么人了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451232V#378F#2P嗯～我觉得阿加特\n',
            '有可能会这么做啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451233V你是属于只要下了决定，就无论\n',
            '多冒失的事情都做得出来的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451234V#1427F#1P我说啊，这根本就是\n',
            '两码事…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451304V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451305V#370F#2P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451306V怎么了？\n',
            '突然沉默下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451238V#1422F#1P呼…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451239V#1420F看来敌人\n',
            '开始登场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0107,
        (
            '#0070451240V#393F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451310V#1412F#2P莫非……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451241V#374F#2P偷、偷窥色魔来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451242V#1425F#1P（艾丝蒂尔，\n',
            '　你能看到北边的草丛吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451243V（以不会被察觉的方式\n',
            '　偷偷地查看一下情况。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451314V#445F#2P（嗯、嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    ChrClearFlags(0x0017, 0x0080)
    Call(1, 0x0010)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451245V#445F#2P（确、确实有什么东西在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451246V#1425F#2P（嗯，那个恐怕就是\n',
            '　我们要逮的『偷窥犯』了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    ChrSetPos(0x0101, 66830, 1000, 19670, 200)
    ChrSetPos(0x0107, 66280, 1000, 18830, 200)
    ChrSetPos(0x0105, 67940, 1000, 19460, 200)
    ChrSetPos(0x0106, 64610, 1000, 16420, 200)
    ChrTurnDirection(0x0106, 0x0101, 0)
    CameraMove(65670, 1000, 18470, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060451317V#1413F（可是应该怎么做呢？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451318V（就算想抓，\n',
            '　从这里也没办法出手啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451249V#445F#2P（嗯，需要有人先出来\n',
            '　从背后绕过去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451250V#1425F#1P（只能这么办了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451251V（好，我和艾丝蒂尔\n',
            '　绕到那家伙的背后去。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451322V（公主你们就在\n',
            '　这里吸引敌人的注意。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451323V#1412F（嗯，明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451253V#398F#1P（嗯、嗯！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451255V#445F#2P（那么，赶快……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0017, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451256V#374F#2P（……咦，奇、奇怪！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451257V#1421F#1P（怎么了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451258V#374F#2P（你、你看！\n',
            '　那家伙要逃跑了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1ADB')
    def lambda_1ADB():
        ChrTurnDirection(0x0106, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1ADB)

    @scena.Lambda('lambda_1AE9')
    def lambda_1AE9():
        ChrTurnDirection(0x0105, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1AE9)

    ChrTurnDirection(0x0107, 0x0017, 400)
    OP_59()
    Call(1, 0x000A)

    ChrTalk(
        0x0106,
        (
            '#0050451259V#1423F#2P艾丝蒂尔！　追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x03)
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451260V#372F#2P明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/R3101._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x1B76
@scena.Code('func_0C_1B76')
def func_0C_1B76():
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0106, 64610, 1000, 16420, 200)
    ChrSetPos(0x0107, 66280, 1000, 18830, 110)
    ChrSetPos(0x0104, 67940, 1000, 19460, 200)
    Call(1, 0x000F)

    ChrTalk(
        0x0101,
        (
            '#0010451195V#377F#1P啊～真惬意～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451196V嗯，还是\n',
            '露天浴令人心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451197V#1401F#2P呵呵，我有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451198V我也完全被这种\n',
            '雅趣给迷住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451199V#442F#1P对了，奥利维尔也\n',
            '曾经在这里住过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451200V#1400F#2P嗯，诞辰庆典后\n',
            '我在这里好好地享受了一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451201V我也约了雪拉，\n',
            '不过不凑巧，她好像很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1D56')
    def lambda_1D56():
        ChrTurnDirection(0x0107, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1D56)

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451202V#374F#1P咦！？\n',
            '你约了雪拉姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451203V#393F#1P啊，那个那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451204V雪拉姐和\n',
            '奥利维尔先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451205V莫非是\n',
            '那种关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451206V#1401F#2P呵呵，这就任凭你想象吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451207V不过你放心好了。\n',
            '现在我只对提妲一心一意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451208V#394F#1P啊、啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050451209V#1425F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451210V#443F#1P喂喂，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451211V对面有个可怕的哥哥\n',
            '在朝这边看哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 200, 400)

    ChrTalk(
        0x0104,
        (
            '#0040451212V#1403F#2P哦，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451213V#1401F哈哈，阿加特。\n',
            '你不参加谈话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F8D')
    def lambda_1F8D():
        CameraMove(65670, 1000, 18470, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F8D)

    ChrTurnDirection(0x0106, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050451214V#1422F#1P算了，先不管这些……\n',
            '可别忘了我们来这里的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451215V#1420F别放松警惕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_201D')
    def lambda_201D():
        ChrSetDirection(0x0101, 200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_201D)

    Sleep(350)

    ChrSetDirection(0x0107, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451216V#445F#2P嗯、嗯……\n',
            '知道了，不过阿加特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451217V#444F#2P你、你为什么要\n',
            '披着一块印花大手巾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451218V老实说你那个样子\n',
            '特别惹人注目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070451219V#395F#1P这、这个么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451220V#1422F#1P什么注目啊闭目的\n',
            '我可不管。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451221V没这东西的话\n',
            '我就提不起精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451222V#1404F#2P呼，个人的习惯倒是\n',
            '不便干涉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451223V…………………………………\n',
            '…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451224V#1403F不过想不到他会披着\n',
            '印花大手巾洗头呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451225V#1426F#1P#3S啊──！\n',
            '你用常识考虑一下啊，常识！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451226V那种时候\n',
            '当然要拿下来了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451227V#377F#2P哦……太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451228V#395F#1P嘿嘿……\n',
            '是、是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451229V还是会拿下来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451230V#1424F#1P都、都是傻瓜！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451231V你们以为我是\n',
            '什么人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451232V#378F#2P嗯～我觉得阿加特\n',
            '有可能会这么做啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451233V你是属于只要下了决定，就无论\n',
            '多冒失的事情都做得出来的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451234V#1427F#1P我说啊，这根本就是\n',
            '两码事…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451235V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451236V#370F#2P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451237V怎么了？\n',
            '突然沉默下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451238V#1422F#1P呼…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451239V#1420F看来敌人\n',
            '开始登场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0107,
        (
            '#0070451240V#393F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451241V#374F#2P偷、偷窥色魔来了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451242V#1425F#1P（艾丝蒂尔，\n',
            '　你能看到北边的草丛吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451243V（以不会被察觉的方式\n',
            '　偷偷地查看一下情况。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451244V#445F（嗯、嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    ChrClearFlags(0x0017, 0x0080)
    Call(1, 0x0010)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451245V#445F#2P（确、确实有什么东西在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451246V#1425F#2P（嗯，那个恐怕就是\n',
            '　我们要逮的『偷窥犯』了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    ChrSetPos(0x0101, 66830, 1000, 19670, 200)
    ChrSetPos(0x0107, 66280, 1000, 18830, 200)
    ChrSetPos(0x0104, 67940, 1000, 19460, 200)
    ChrSetPos(0x0106, 64610, 1000, 16420, 200)
    ChrTurnDirection(0x0106, 0x0101, 0)
    CameraMove(65670, 1000, 18470, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040451247V#1402F#2P（那接下来该怎么办呢？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451248V（就算想抓，\n',
            '　介入起来非常困难吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451249V#445F#2P（嗯，需要有人先出来\n',
            '　从背后绕过去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451250V#1425F#1P（只能这么办了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451251V（好，我和艾丝蒂尔\n',
            '　绕到那家伙的背后去。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451252V（奥利维尔你们在这里\n',
            '　这里吸引敌人的注意。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451253V#398F#1P（嗯、嗯！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451254V#1400F（嗯，明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451255V#445F#2P（那么，赶快……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0017, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451256V#374F#2P（……咦，奇、奇怪！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050451257V#1421F#1P（怎么了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451258V#374F#2P（你、你看！\n',
            '　那家伙要逃跑了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29A9')
    def lambda_29A9():
        ChrTurnDirection(0x0106, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_29A9)

    @scena.Lambda('lambda_29B7')
    def lambda_29B7():
        ChrTurnDirection(0x0104, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_29B7)

    ChrTurnDirection(0x0107, 0x0017, 400)
    OP_59()
    Call(1, 0x000A)

    ChrTalk(
        0x0106,
        (
            '#0050451259V#1423F#2P艾丝蒂尔！　追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x03)
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451260V#372F#2P明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/R3101._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x2A44
@scena.Code('func_0D_2A44')
def func_0D_2A44():
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0103, 65900, 1000, 18260, 108)
    ChrSetPos(0x0107, 66310, 1000, 19250, 153)
    ChrSetPos(0x0105, 68340, 1000, 19480, 200)
    Call(1, 0x000F)

    ChrTalk(
        0x0101,
        (
            '#0010451195V#377F#1P啊～真惬意～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451196V嗯，还是\n',
            '露天浴令人心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451333V#1416F#2P风真令人感到舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451334V#1391F#1P呵呵，真像仙境一般。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451335V要是能再来上一杯\n',
            '就没的说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451336V#370F那倒是无所谓，不过雪拉姐，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451337V你的头发没放下来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2BC4')
    def lambda_2BC4():
        ChrSetDirection(0x0107, 200, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2BC4)

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451338V#1390F#1P这样的话只要穿上\n',
            '衣服就能立即飞奔到外面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451339V一旦解开再\n',
            '绕起来就要花很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451340V#442F嗯，确实不知道\n',
            '罪犯什么时候会来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 155, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451341V#395F不过也因为那个罪犯\n',
            '我们大家才能在一起洗个澡啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070451342V嘿嘿，虽然对方不是好人，\n',
            '不过还是有点心存感激。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 300, 400)

    ChrTalk(
        0x0105,
        (
            '#0060451343V#1410F#2P呵呵，我明白你的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451344V总觉得这样一来\n',
            '就像是来旅行的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451345V#371F又是4个人，就好像和睦的\n',
            '家庭旅行一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451346V#1393F#1P这种情况下的话……\n',
            '难道说我是提妲的妈妈？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451347V#1395F至少希望你说成是４姐妹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E2D')
    def lambda_2E2D():
        ChrSetDirection(0x0101, 200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E2D)

    ChrSetDirection(0x0107, 200, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451348V#390F啊，那就这样好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451349V#1411F#2P嘻嘻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451350V#1410F不过，想想看的话\n',
            '洗澡成员都是女性还是第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2ED1')
    def lambda_2ED1():
        ChrSetDirection(0x0101, 108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ED1)

    Sleep(100)

    @scena.Lambda('lambda_2EE4')
    def lambda_2EE4():
        ChrSetDirection(0x0103, 108, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2EE4)

    ChrSetDirection(0x0107, 108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451351V#370F#1P嗯，这么说起来确实如此呢。\n',
            '今天奥利维尔也不在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451352V#443F嗯，如果让那家伙知道的话\n',
            '一定会哭着喊不甘心的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451353V#395F#1P这、这个么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451354V#1415F#2P完、完全可以想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451355V#1396F#1P算了，就对他保密吧。\n',
            '可不想给他增添不必要的记恨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451356V奥利维尔好像也\n',
            '非常中意这个温泉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451357V#370F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451358V#390F#1P姐姐，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451359V#443F#2P咦……？\n',
            '不，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451360V#442F我只是在想，难得有机会，\n',
            '是不是要问问看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451361V#393F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451362V#378F#2P那、那个，雪拉姐。\n',
            '我能问你一件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451363V#1393F#1P哎呀，怎么了？一本正经的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451364V#442F#2P我说，你真～的\n',
            '和奥利维尔完全没什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_321F')
    def lambda_321F():
        ChrTurnDirection(0x0105, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_321F)

    Sleep(150)

    ChrTurnDirection(0x0107, 0x0103, 400)

    ChrTalk(
        0x0105,
        (
            '#0060451365V#1414F#2P…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451366V#1393F#1P什么指的是……\n',
            '那种关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451367V#441F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451368V#1391F#1P傻瓜，怎么可能有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451369V只是普通的酒友啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451370V#378F啊～真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451371V你们偶尔会进行只有你们\n',
            '两个人才能明白的对话吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451372V那种彼此了解的协调感觉\n',
            '还真是挺让人在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451373V#396F（心、心砰砰跳……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451374V#1396F#1P哦，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451375V所以你才突然问\n',
            '这么奇怪的话啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451376V很遗憾，那也只是工作的对话哦。\n',
            '稍微有点原因的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451377V#370F#2P原因？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451378V#1390F#1P嗯，不过以后再向你说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451379V总之现在不能太\n',
            '热衷于聊天。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451380V我们是为了搜查来的，\n',
            '必须对周围再警惕一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451381V#379F啊，被你蒙混过关了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 300, 400)

    ChrTalk(
        0x0105,
        (
            '#0060451382V#1412F#2P不过，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451383V……看来雪拉小姐\n',
            '说的没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_35CD')
    def lambda_35CD():
        ChrTurnDirection(0x0103, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_35CD)

    Sleep(150)

    @scena.Lambda('lambda_35E0')
    def lambda_35E0():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35E0)

    Sleep(150)

    ChrSetDirection(0x0107, 108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451384V#374F#2P咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451385V#393F#1P莫、莫非……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451386V#1392F#1P（偷窥色魔来了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451387V#1412F#2P（……在北边的草丛里。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451388V#445F（明白了，北边的草丛是吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    ChrClearFlags(0x0017, 0x0080)
    Call(1, 0x0010)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451245V#445F#2P（确、确实有什么东西在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451390V#1392F#2P（莫非，那就是\n',
            '　『偷窥犯』的原形？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0103, 65900, 1000, 18260, 108)
    ChrSetPos(0x0107, 66310, 1000, 19250, 153)
    ChrSetPos(0x0105, 68340, 1000, 19480, 200)
    Fade(1000)
    CameraMove(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060451391V#1413F#2P（可是，我们该怎么办？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060451318V（就算想抓住他，\n',
            '　从这里也没办法出手啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451393V#445F#2P（嗯，需要有人先出来\n',
            '　从背后绕过去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451394V#1392F#1P（我和艾丝蒂尔绕到\n',
            '　那家伙的背后去。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451395V（公主大人和提妲在这里\n',
            '　吸引敌人的注意。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060451396V#1412F#2P（嗯，明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451397V#398F（嗯、嗯！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451398V#445F#2P（那么，赶快……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0017, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451256V#374F#2P（……咦，奇、奇怪！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_39D7')
    def lambda_39D7():
        ChrSetDirection(0x0103, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_39D7)

    Sleep(150)

    @scena.Lambda('lambda_39EA')
    def lambda_39EA():
        ChrSetDirection(0x0105, 300, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_39EA)

    Sleep(150)

    ChrSetDirection(0x0107, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451400V#1393F#1P（怎么了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451258V#374F#2P（你、你看！\n',
            '　那家伙要逃跑了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A68')
    def lambda_3A68():
        ChrSetDirection(0x0105, 350, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3A68)

    @scena.Lambda('lambda_3A76')
    def lambda_3A76():
        ChrTurnDirection(0x0103, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3A76)

    ChrTurnDirection(0x0107, 0x0017, 400)
    WaitForThreadExit(0x0105, 0x0001)
    OP_59()
    Call(1, 0x000A)

    ChrTalk(
        0x0103,
        (
            '#0030451402V#1394F#2P艾丝蒂尔！追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x03)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451260V#372F#2P明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/R3101._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x3B06
@scena.Code('func_0E_3B06')
def func_0E_3B06():
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0103, 65900, 1000, 18260, 108)
    ChrSetPos(0x0107, 66310, 1000, 19250, 153)
    ChrSetPos(0x0104, 68340, 1000, 19480, 200)
    Call(1, 0x000F)

    ChrTalk(
        0x0101,
        (
            '#0010451195V#377F#1P啊～真惬意～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451196V嗯，还是\n',
            '露天浴令人心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451334V#1391F#1P呵呵，真像仙境一般。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451335V要是能再来上一杯\n',
            '就没的说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 200, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451336V#370F那倒是无所谓，不过雪拉姐，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451337V你的头发没放下来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C57')
    def lambda_3C57():
        ChrSetDirection(0x0107, 200, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3C57)

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451338V#1390F#1P这样的话只要穿上\n',
            '衣服就能立即飞奔到外面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451339V一旦解开再\n',
            '绕起来就要花很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451340V#442F嗯，确实不知道\n',
            '罪犯什么时候会来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451413V#1404F#2P呼，不过有点遗憾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451414V洗后披散着的头发的雪拉也\n',
            '也一定很有魅力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 108, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451415V#1396F#1P呵呵，那就留待下次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451416V#1401F#2P呵呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451417V那么，下次我就\n',
            '邀请你去帝国领土内的\n',
            '高级温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451418V#370F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070451419V#390F姐姐，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451420V#443F#2P咦……？\n',
            '不，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451421V#442F只是感觉……\n',
            '有点可疑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451422V#393F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451423V#1393F#1P可疑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451424V莫非，\n',
            '是说我和奥利维尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451367V#441F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 200, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451426V#1391F#1P傻瓜，没什么的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451427V只是普通的酒友啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040451428V#1401F#2P这、这个称号\n',
            '我可不敢当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451370V#378F啊～真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451371V你们偶尔会进行只有你们\n',
            '两个人才能明白的对话吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451372V那只互相了解的感觉\n',
            '挺让人在意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451432V#396F（心、心砰砰跳……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451374V#1396F#1P哦，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451375V所以你才突然问\n',
            '这么奇怪的话吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451376V很遗憾，那也只是工作方面的对话哦。\n',
            '稍微有点原因的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451377V#370F#2P原因？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451378V#1390F#1P嗯，不过以后再向你说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451379V总之现在不能太\n',
            '热衷于聊天。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451380V我们是为了搜查来的，\n',
            '必须对周围再警惕一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451381V#379F啊，被你蒙混过关了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451441V#1401F#2P呼，不过……\n',
            '偶然还真是可怕的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451442V看来真的必须要\n',
            '警惕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_4303')
    def lambda_4303():
        ChrTurnDirection(0x0103, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4303)

    Sleep(150)

    @scena.Lambda('lambda_4316')
    def lambda_4316():
        ChrSetDirection(0x0101, 108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4316)

    Sleep(150)

    ChrSetDirection(0x0107, 108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451384V#374F#2P咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451385V#393F#1P莫、莫非……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451445V#1392F#1P（偷窥色魔来了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451446V#1402F#2P（能看到北边的草丛吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451447V（以不会被察觉的方式\n',
            '　偷偷地查看一下情况。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451448V#445F#2P（嗯、嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    ChrClearFlags(0x0017, 0x0080)
    Call(1, 0x0010)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010451245V#445F#2P（确、确实有什么东西在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451390V#1392F#2P（莫非，那就是\n',
            '　『偷窥犯』的原形？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    ChrSetPos(0x0101, 66830, 1000, 19670, 155)
    ChrSetPos(0x0103, 65900, 1000, 18260, 108)
    ChrSetPos(0x0107, 66310, 1000, 19250, 153)
    ChrSetPos(0x0104, 68340, 1000, 19480, 200)
    CameraMove(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040451247V#1402F#2P（那接下来该怎么办呢？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040451248V（就算想抓，\n',
            '　介入起来非常困难吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451393V#445F#2P（嗯，需要有人先出来\n',
            '　从背后绕过去。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030451394V#1392F#1P（我和艾丝蒂尔绕到\n',
            '　那家伙的背后去。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451455V（奥利维尔和提妲在这里\n',
            '　吸引敌人的注意。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070451456V#398F#1P（嗯、嗯！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040451457V#1400F#2P（嗯，明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451398V#445F#2P（那么，赶快……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0017, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451256V#374F#2P（……咦，奇、奇怪！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4738')
    def lambda_4738():
        ChrSetDirection(0x0103, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4738)

    Sleep(150)

    @scena.Lambda('lambda_474B')
    def lambda_474B():
        ChrSetDirection(0x0104, 300, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_474B)

    Sleep(150)

    ChrSetDirection(0x0107, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030451400V#1393F#1P（怎么了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010451258V#374F#2P（你、你看！\n',
            '　那家伙要逃跑了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_47C9')
    def lambda_47C9():
        ChrSetDirection(0x0104, 350, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_47C9)

    @scena.Lambda('lambda_47D7')
    def lambda_47D7():
        ChrTurnDirection(0x0103, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_47D7)

    ChrTurnDirection(0x0107, 0x0017, 400)
    WaitForThreadExit(0x0104, 0x0001)
    OP_59()
    Call(1, 0x000A)

    ChrTalk(
        0x0103,
        (
            '#0030451402V#1394F#2P艾丝蒂尔！　追！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x03)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010451260V#372F#2P明、明白！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/R3101._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x4869
@scena.Code('func_0F_4869')
def func_0F_4869():
    CameraMove(65820, 2000, 7860, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(80000, 0)
    OP_6E(246, 0)

    @scena.Lambda('lambda_48AC')
    def lambda_48AC():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_48AC)

    CameraMove(65820, 2000, 17860, 6000)
    Fade(2000)
    PlaySE(162, 0x00, 0x64)
    CameraMove(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(335000, 0)
    OP_0D()
    Sleep(1000)

    Return()

# id: 0x0010 offset: 0x490C
@scena.Code('func_10_490C')
def func_10_490C():
    @scena.Lambda('lambda_4912')
    def lambda_4912():
        CameraMove(67620, 4000, 23820, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4912)

    @scena.Lambda('lambda_492A')
    def lambda_492A():
        OP_67(0, 3370, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_492A)

    @scena.Lambda('lambda_4942')
    def lambda_4942():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4942)

    @scena.Lambda('lambda_4952')
    def lambda_4952():
        OP_6C(350000, 3000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_4952)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
