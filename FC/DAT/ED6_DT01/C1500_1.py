import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1500_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1500_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 61
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E7',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrTurnDirection(0x0000, 0x0008, 400)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_107',
    )

    ChrTalk(
        0x0101,
        (
            '#0010151196V#004F…………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151197V好像有什么东西在动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A0')

    def _loc_107(): pass

    label('loc_107')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_153',
    )

    ChrTalk(
        0x0102,
        (
            '#0020151198V#014F…………嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151199V那是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A0')

    def _loc_153(): pass

    label('loc_153')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030151200V#023F…………嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151201V……大家等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A0(): pass

    label('loc_1A0')

    @scena.Lambda('lambda_01A6')
    def lambda_01A6():
        CameraMove(-149500, 2000, 60700, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_01A6)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0008, 0x01, 0x01, 0x0006)
    CreateThread(0x0009, 0x01, 0x01, 0x0007)
    CreateThread(0x000A, 0x01, 0x01, 0x0008)
    CreateThread(0x000B, 0x01, 0x01, 0x0009)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Sleep(600)

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Sleep(600)

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(800)

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrSetPos(0x0101, -143800, 3500, 73400, 165)
    ChrSetPos(0x0103, -143590, 2970, 74590, 165)
    ChrSetPos(0x0102, -144440, 2820, 73810, 165)
    ChrSetPos(0x0135, -144850, 3310, 75450, 165)

    @scena.Lambda('lambda_0291')
    def lambda_0291():
        OP_6C(300000, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_0291)

    OP_A5(0x0000)
    OP_A5(0x0001)
    OP_A5(0x0002)
    OP_A5(0x0003)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020151202V#012F我们中埋伏了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTurnDirection(0x0102, 0x000C, 400)
    Sleep(400)

    @scena.Lambda('lambda_0301')
    def lambda_0301():
        CameraMove(-146900, 4000, 81700, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0301)

    @scena.Lambda('lambda_0319')
    def lambda_0319():
        ChrTurnDirection(0x0101, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0319)

    @scena.Lambda('lambda_0327')
    def lambda_0327():
        ChrTurnDirection(0x0103, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0327)

    Sleep(400)

    @scena.Lambda('lambda_033A')
    def lambda_033A():
        ChrTurnDirection(0x0135, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0135, 0x0001, lambda_033A)

    CreateThread(0x000C, 0x01, 0x01, 0x000A)
    CreateThread(0x000D, 0x01, 0x01, 0x000B)
    CreateThread(0x000E, 0x01, 0x01, 0x000C)
    CreateThread(0x000F, 0x01, 0x01, 0x000D)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    Sleep(600)

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    Sleep(800)

    OP_62(0x0135, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0135, 0, 0, 0, 800, 12000)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Sleep(400)

    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    Sleep(600)

    ChrWalkTo(0x0135, -144640, 3100, 74730, 2000, 0x00)
    ChrTurnDirection(0x0135, 0x000C, 400)
    OP_A5(0x0004)
    OP_A5(0x0005)
    OP_A5(0x0006)
    OP_A5(0x0007)
    Sleep(400)

    ChrTurnDirection(0x0135, 0x0103, 0)

    ChrTalk(
        0x0135,
        (
            '#1370151203V怎、怎、怎么办！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0135, 0)

    ChrTalk(
        0x0103,
        (
            '#0030151204V#024F冷静一点！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151205V没关系的，\n',
            '我们一定会好好保护你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ExecExpressionWithValue(
        0x0011,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x04,
        (
            (Expr.GetChrWork, 0x101, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010151206V#002F前面和后面都有魔兽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151207V好～那么我们就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_504(): pass

    label('loc_504')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6DD',
    )

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
            TXT(0x00, '【正面突破！】\n'),
            TXT(0x01, '【保护后方！】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_574'),
        (0x00000001, 'loc_605'),
        (-1, 'loc_6DA'),
    )

    def _loc_574(): pass

    label('loc_574')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010151208V#005F正面突破！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151209V#022F嗯，对。\n',
            '队伍分散是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0010, 0x01, 0x0008)
    OP_2C(0x0010, 0x00C8)
    OP_2B(0x0010, 0x0001)
    Call(1, 0x0001)

    Jump('loc_6DA')

    def _loc_605(): pass

    label('loc_605')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010151210V#005F赶快保护后方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0011, 0xFF)
    ChrSetFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_0657')
    def lambda_0657():
        ChrTurnDirection(0x0135, 0x0011, 0)
        Yield()

        Jump('lambda_0657')

    DispatchAsync2(0x0135, 0x0001, lambda_0657)

    @scena.Lambda('lambda_0668')
    def lambda_0668():
        ChrTurnDirection(0x0103, 0x0011, 0)
        Yield()

        Jump('lambda_0668')

    DispatchAsync2(0x0103, 0x0001, lambda_0668)

    @scena.Lambda('lambda_0679')
    def lambda_0679():
        ChrTurnDirection(0x0102, 0x0011, 0)
        Yield()

        Jump('lambda_0679')

    DispatchAsync2(0x0102, 0x0001, lambda_0679)

    ChrSetChipByIndex(0x0011, 5)

    @scena.Lambda('lambda_068F')
    def lambda_068F():
        CameraMove(-144030, 3060, 74750, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_068F)

    ChrWalkTo(0x0011, -144370, 3600, 76050, 5000, 0x00)
    ChrSetChipByIndex(0x0011, 2)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)
    TerminateThread(0x0135, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0102, 0x01)
    OP_28(0x0010, 0x01, 0x0010)
    Call(1, 0x0003)

    Jump('loc_6DA')

    def _loc_6DA(): pass

    label('loc_6DA')

    Jump('loc_504')

    def _loc_6DD(): pass

    label('loc_6DD')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6E7(): pass

    label('loc_6E7')

    Return()

# id: 0x0001 offset: 0x6E8
@scena.Code('func_01_6E8')
def func_01_6E8():
    @scena.Lambda('lambda_06EE')
    def lambda_06EE():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06EE)

    @scena.Lambda('lambda_06FC')
    def lambda_06FC():
        ChrTurnDirection(0x0135, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0135, 0x0001, lambda_06FC)

    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020151211V#012F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x04,
        (
            (Expr.GetChrWork, 0x102, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    CreateThread(0x0012, 0x03, 0x00, 0x0002)

    ChrTalk(
        0x0103,
        (
            '#0030151212V#022F速战速决！把前方的敌人杀个片甲不留！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0013,
        0x01,
        (
            (Expr.GetChrWork, 0x103, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x02,
        (
            (Expr.GetChrWork, 0x103, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x03,
        (
            (Expr.GetChrWork, 0x103, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x04,
        (
            (Expr.GetChrWork, 0x103, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    CreateThread(0x0013, 0x03, 0x00, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010151213V#002F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0012, 0x03)
    TerminateThread(0x0013, 0x03)
    ChrSetChipByIndex(0x0011, 5)
    ChrSetChipByIndex(0x0012, 6)
    ChrSetChipByIndex(0x0013, 7)

    @scena.Lambda('lambda_080F')
    def lambda_080F():
        CameraMove(-142800, 2000, 69900, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_080F)

    @scena.Lambda('lambda_0827')
    def lambda_0827():
        OP_92(0x0011, 0x0010, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0827)

    @scena.Lambda('lambda_083C')
    def lambda_083C():
        OP_92(0x0013, 0x0010, 4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_083C)

    @scena.Lambda('lambda_0851')
    def lambda_0851():
        OP_92(0x0012, 0x0010, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0851)

    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0878')
    def lambda_0878():
        OP_92(0x0135, 0x0010, 6000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0135, 0x0002, lambda_0878)

    @scena.Lambda('lambda_088D')
    def lambda_088D():
        OP_92(0x0008, 0x0101, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_088D)

    @scena.Lambda('lambda_08A2')
    def lambda_08A2():
        OP_92(0x0009, 0x0101, 4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_08A2)

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        OP_92(0x000A, 0x0101, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_08B7)

    @scena.Lambda('lambda_08CC')
    def lambda_08CC():
        OP_92(0x000B, 0x0101, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08CC)

    Sleep(800)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0135, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0012, 0xFF)
    Battle(0x000003F0, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_915'),
        (-1, 'loc_918'),
    )

    def _loc_915(): pass

    label('loc_915')

    OP_B4(0x00)

    Return()

    def _loc_918(): pass

    label('loc_918')

    EventBegin(0x00)
    CameraMove(-142800, 2000, 69900, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetPos(0x0011, -142200, 2500, 67300, 165)
    ChrSetPos(0x0013, -143500, 2500, 67900, 165)
    ChrSetPos(0x0012, -141300, 2500, 68600, 165)
    ChrSetPos(0x0135, -143500, 2000, 70600, 165)
    ChrSetChipByIndex(0x0011, 2)
    ChrSetChipByIndex(0x0012, 3)
    ChrSetChipByIndex(0x0013, 4)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)
    CreateThread(0x0012, 0x03, 0x00, 0x0002)
    CreateThread(0x0013, 0x03, 0x00, 0x0002)
    ChrSetPos(0x000C, -146200, 4000, 79800, 165)
    ChrSetPos(0x000D, -146200, 4000, 79800, 165)
    ChrSetPos(0x000E, -146200, 4000, 79800, 165)
    ChrSetPos(0x000F, -146200, 4000, 79800, 165)
    ChrSetChipByIndex(0x000C, 1)
    ChrSetChipByIndex(0x000D, 1)
    ChrSetChipByIndex(0x000E, 1)
    ChrSetChipByIndex(0x000F, 1)
    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0A17')
    def lambda_0A17():
        ChrWalkTo(0x0135, -142600, 2100, 65700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0135, 0x0002, lambda_0A17)

    OP_0D()
    ChrSetDirection(0x0011, 345, 400)
    ChrSetDirection(0x0012, 345, 400)
    ChrSetDirection(0x0013, 345, 400)
    Sleep(800)

    ChrSetDirection(0x0135, 345, 400)

    ChrTalk(
        0x0013,
        (
            '#0030151214V#022F好了，还剩后面的。\n',
            '集中精神！一鼓作气消灭它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A9A')
    def lambda_0A9A():
        ChrTurnDirection(0x0011, 0x000C, 0)
        Yield()

        Jump('lambda_0A9A')

    DispatchAsync2(0x0011, 0x0001, lambda_0A9A)

    @scena.Lambda('lambda_0AAB')
    def lambda_0AAB():
        ChrTurnDirection(0x0013, 0x000C, 0)
        Yield()

        Jump('lambda_0AAB')

    DispatchAsync2(0x0013, 0x0001, lambda_0AAB)

    @scena.Lambda('lambda_0ABC')
    def lambda_0ABC():
        ChrTurnDirection(0x0012, 0x000C, 0)
        Yield()

        Jump('lambda_0ABC')

    DispatchAsync2(0x0012, 0x0001, lambda_0ABC)

    @scena.Lambda('lambda_0ACD')
    def lambda_0ACD():
        OP_92(0x000C, 0x0010, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0ACD)

    Sleep(400)

    @scena.Lambda('lambda_0AE7')
    def lambda_0AE7():
        OP_92(0x000D, 0x0010, 2000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0AE7)

    Sleep(400)

    @scena.Lambda('lambda_0B01')
    def lambda_0B01():
        OP_92(0x000E, 0x0010, 3000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0B01)

    Sleep(400)

    @scena.Lambda('lambda_0B1B')
    def lambda_0B1B():
        OP_92(0x000F, 0x0010, 4000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0B1B)

    Sleep(600)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0135, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0012, 0xFF)
    Battle(0x000003F0, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_B64'),
        (-1, 'loc_B67'),
    )

    def _loc_B64(): pass

    label('loc_B64')

    OP_B4(0x00)

    Return()

    def _loc_B67(): pass

    label('loc_B67')

    EventBegin(0x00)
    CameraMove(-142180, 2040, 67240, 0)
    ChrSetPos(0x0101, -142200, 2000, 67300, 0)
    ChrSetPos(0x0103, -143500, 2000, 67900, 0)
    ChrSetPos(0x0102, -141300, 2000, 68600, 0)
    ChrSetPos(0x0135, -143500, 2000, 70600, 0)
    ChrSetPos(0x0135, -142600, 2100, 65700, 345)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0103, 4)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0103, 0x0080)
    OP_0D()
    Call(1, 0x0002)

    Return()

# id: 0x0002 offset: 0xC16
@scena.Code('func_02_C16')
def func_02_C16():
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151223V#007F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151224V#014F总算是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0103, 65535)
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151225V#020F……已经结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151226V呼呼～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151227V得、得救了～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0135, 400)

    @scena.Lambda('lambda_0CEC')
    def lambda_0CEC():
        ChrTurnDirection(0x0102, 0x0135, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CEC)

    ChrSetDirection(0x0101, 165, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151228V#021F如何？我说没问题的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151229V呼…………\n',
            '不敢相信我竟然平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151230V呀，你们游击士真是太厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151231V那样的魔兽\n',
            '简单几下就收拾掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0135, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151232V#001F嘿嘿㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151233V当然了，我的棒术用来对付魔兽，\n',
            '可以说是一击必杀的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151234V啊，对了。\n',
            '我就给您专门来一场棒术表演吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(500, 0x00, 0x64)
    ChrSetDirection(0x0101, 300, 2000)
    ChrSetDirection(0x0101, 75, 2000)
    ChrSetDirection(0x0101, 165, 2000)
    ChrSetChipByIndex(0x0101, 2)
    CreateThread(0x0101, 0x00, 0x00, 0x0002)
    ChrTurnDirection(0x0103, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_1001',
    )

    ChrTalk(
        0x0103,
        (
            '#0030151235V#022F好了，不要再得意忘形了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151236V如果不是因为判断失误的话，\n',
            '那些魔兽应该很好解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151237V#007F呜呜……我知道错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151238V#020F嗯，就当作经验教训吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151239V那么，\n',
            '我们就继续向目的地出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151240V还不知道魔兽\n',
            '会不会再来袭击呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1084')

    def _loc_1001(): pass

    label('loc_1001')

    ChrTalk(
        0x0103,
        (
            '#0030151241V#026F好啦好啦，不用继续了，\n',
            '以后有的是机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151242V我们就继续向目的地出发吧。\n',
            '说不定还会有魔兽再来袭击呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1084(): pass

    label('loc_1084')

    ChrTurnDirection(0x0135, 0x0103, 0)
    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x0135, 0, 0, 0, 800, 12000)

    ChrTalk(
        0x0135,
        (
            '#1370151243V那、那可就麻烦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0135,
        (
            '#1370151244V快、快点出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1193',
    )

    ChrTalk(
        0x0102,
        (
            '#0020151245V#010F好啦，艾丝蒂尔，\n',
            '我们继续赶路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151246V#007F嘁，知道啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1193(): pass

    label('loc_1193')

    ChrTalk(
        0x0103,
        (
            '#0030151247V#020F关所就在前面不远了，\n',
            '在到达之前可不要掉以轻心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151248V#006F好～的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0010, 0x01, 0x4000)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x120A
@scena.Code('func_03_120A')
def func_03_120A():
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020151215V#014F艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151216V#023F不要分散了啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151217V#025F……唉，来不及了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0010151218V#004F咦……？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12EB')
    def lambda_12EB():
        OP_92(0x0008, 0x0101, 4800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_12EB)

    @scena.Lambda('lambda_1300')
    def lambda_1300():
        OP_92(0x0009, 0x0101, 3800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1300)

    @scena.Lambda('lambda_1315')
    def lambda_1315():
        OP_92(0x000A, 0x0101, 4800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1315)

    @scena.Lambda('lambda_132A')
    def lambda_132A():
        OP_92(0x000B, 0x0101, 5800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_132A)

    @scena.Lambda('lambda_133F')
    def lambda_133F():
        OP_92(0x000C, 0x0011, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_133F)

    @scena.Lambda('lambda_1354')
    def lambda_1354():
        OP_92(0x000D, 0x0011, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1354)

    @scena.Lambda('lambda_1369')
    def lambda_1369():
        OP_92(0x000E, 0x0011, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1369)

    @scena.Lambda('lambda_137E')
    def lambda_137E():
        OP_92(0x000F, 0x0011, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_137E)

    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000F, 0x0001)

    ExecExpressionWithValue(
        0x0012,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0012,
        0x04,
        (
            (Expr.GetChrWork, 0x102, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrTurnDirection(0x0012, 0x0009, 400)

    ChrTalk(
        0x0012,
        (
            '#0020151219V#013F完全被包围了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0012, 0x03, 0x00, 0x0002)
    OP_62(0x0011, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0010151220V#509F难、难道是判断失误……！？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0013,
        0x01,
        (
            (Expr.GetChrWork, 0x103, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x02,
        (
            (Expr.GetChrWork, 0x103, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x03,
        (
            (Expr.GetChrWork, 0x103, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x04,
        (
            (Expr.GetChrWork, 0x103, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrTurnDirection(0x0013, 0x0009, 400)

    ChrTalk(
        0x0013,
        (
            '#0030151221V#022F待会儿再后悔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151222V既然这样，\n',
            '就只有下决心战斗到底了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0013, 0x03, 0x00, 0x0002)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    CreateThread(0x0009, 0x01, 0x01, 0x0004)
    Sleep(200)

    CreateThread(0x000C, 0x01, 0x01, 0x0005)
    CreateThread(0x0008, 0x01, 0x01, 0x0004)
    Sleep(200)

    CreateThread(0x000F, 0x01, 0x01, 0x0005)
    CreateThread(0x000A, 0x01, 0x01, 0x0004)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x01, 0x0005)
    CreateThread(0x000B, 0x01, 0x01, 0x0004)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x01, 0x0005)
    WaitForThreadExit(0x000C, 0x0001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    Battle(0x000003F1, 0x00000000, 0x01, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_159C'),
        (-1, 'loc_159F'),
    )

    def _loc_159C(): pass

    label('loc_159C')

    OP_B4(0x00)

    Return()

    def _loc_159F(): pass

    label('loc_159F')

    EventBegin(0x00)
    CameraMove(-142180, 2040, 67240, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0103, 0x0080)
    ChrSetPos(0x0101, -142200, 2000, 67300, 0)
    ChrSetPos(0x0103, -143500, 2000, 67900, 0)
    ChrSetPos(0x0102, -141300, 2000, 68600, 0)
    ChrSetPos(0x0135, -143500, 2000, 70600, 0)
    ChrSetPos(0x0135, -142600, 2100, 65700, 345)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0103, 4)
    OP_0D()
    Call(1, 0x0002)

    Return()

# id: 0x0004 offset: 0x1662
@scena.Code('func_04_1662')
def func_04_1662():
    ChrSetChipByIndex(0x00FE, 1)
    ChrWalkTo(0x00FE, -142590, 2050, 69490, 5000, 0x00)
    ChrWalkTo(0x00FE, -143290, 2160, 71690, 5000, 0x00)

    Return()

# id: 0x0005 offset: 0x1690
@scena.Code('func_05_1690')
def func_05_1690():
    ChrSetChipByIndex(0x00FE, 1)
    ChrWalkTo(0x00FE, -145000, 4140, 77940, 5000, 0x00)
    ChrWalkTo(0x00FE, -144500, 3960, 76910, 5000, 0x00)

    Return()

# id: 0x0006 offset: 0x16BE
@scena.Code('func_06_16BE')
def func_06_16BE():
    OP_A6(0x0000)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 1)
    ChrWalkTo(0x0008, -146400, 7800, 62300, 5000, 0x00)
    ChrSetDirection(0x0008, 165, 0)
    ChrSetChipByIndex(0x0008, 0)
    PlaySE(129, 0x00, 0x50)
    ChrJumpTo(0x0008, -145300, 6800, 58100, 2500, 5000)
    ChrSetDirection(0x0008, 75, 0)
    ChrClearFlags(0x0008, 0x0004)
    PlaySE(129, 0x00, 0x5A)
    ChrJumpTo(0x0008, -144000, 2000, 61800, 2500, 5000)
    ChrSetChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_173A')
    def lambda_173A():
        CameraMove(-143500, 2500, 73000, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_173A)

    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0008, -140200, 2000, 67200, 5000, 0x00)
    ChrSetChipByIndex(0x0008, 0)
    CreateThread(0x0008, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x0008, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0007 offset: 0x177C
@scena.Code('func_07_177C')
def func_07_177C():
    OP_A6(0x0001)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetChipByIndex(0x0009, 1)
    ChrWalkTo(0x0009, -146400, 7800, 62300, 5000, 0x00)
    ChrSetDirection(0x0009, 165, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrJumpTo(0x0009, -145300, 6800, 58100, 2500, 5000)
    ChrSetDirection(0x0008, 75, 0)
    ChrClearFlags(0x0009, 0x0004)
    ChrJumpTo(0x0009, -144000, 2000, 61800, 2500, 5000)
    ChrSetChipByIndex(0x0009, 1)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, -142000, 2000, 68000, 5000, 0x00)
    ChrSetChipByIndex(0x0009, 0)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x0009, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0008 offset: 0x1818
@scena.Code('func_08_1818')
def func_08_1818():
    OP_A6(0x0002)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -146400, 7800, 62300, 5000, 0x00)
    ChrSetDirection(0x000A, 165, 0)
    ChrSetChipByIndex(0x000A, 0)
    ChrJumpTo(0x000A, -145300, 6800, 58100, 2500, 5000)
    ChrSetDirection(0x000A, 75, 0)
    ChrClearFlags(0x000A, 0x0004)
    ChrJumpTo(0x000A, -144000, 2000, 61800, 2500, 5000)
    ChrSetChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -143600, 2000, 66700, 5000, 0x00)
    ChrSetChipByIndex(0x000A, 0)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000A, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0009 offset: 0x18AF
@scena.Code('func_09_18AF')
def func_09_18AF():
    OP_A6(0x0003)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 1)
    ChrWalkTo(0x000B, -146400, 7800, 62300, 5000, 0x00)
    ChrSetDirection(0x000B, 165, 0)
    ChrSetChipByIndex(0x000B, 0)
    ChrJumpTo(0x000B, -145300, 6800, 58100, 2500, 5000)
    ChrSetDirection(0x000B, 75, 0)
    ChrClearFlags(0x000B, 0x0004)
    ChrJumpTo(0x000B, -144000, 2000, 61800, 2500, 5000)
    ChrSetChipByIndex(0x000B, 1)
    ChrWalkTo(0x000B, -141600, 2000, 65500, 5000, 0x00)
    ChrSetChipByIndex(0x000B, 0)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000B, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x000A offset: 0x1946
@scena.Code('func_0A_1946')
def func_0A_1946():
    OP_A6(0x0004)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x000C, 1)
    ChrWalkTo(0x000C, -149600, 6900, 82600, 5000, 0x00)
    ChrSetDirection(0x000C, 120, 0)
    ChrSetChipByIndex(0x000C, 0)
    ChrClearFlags(0x000C, 0x0004)
    PlaySE(129, 0x00, 0x50)
    ChrJumpTo(0x000C, -148600, 4000, 80000, 2500, 5000)
    ChrSetChipByIndex(0x000C, 1)

    @scena.Lambda('lambda_199F')
    def lambda_199F():
        CameraMove(-143900, 2800, 74200, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_199F)

    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000C, -143500, 4000, 79900, 5000, 0x00)
    ChrSetChipByIndex(0x000C, 0)
    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000C, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x000B offset: 0x19E1
@scena.Code('func_0B_19E1')
def func_0B_19E1():
    OP_A6(0x0005)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetChipByIndex(0x000D, 1)
    ChrWalkTo(0x000D, -149600, 6900, 82600, 5000, 0x00)
    ChrSetDirection(0x000D, 120, 0)
    ChrSetChipByIndex(0x000D, 0)
    ChrClearFlags(0x000D, 0x0004)
    ChrJumpTo(0x000D, -148600, 4000, 80000, 2500, 5000)
    ChrSetChipByIndex(0x000D, 1)
    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000D, -145600, 4000, 80300, 5000, 0x00)
    ChrSetChipByIndex(0x000D, 0)
    CreateThread(0x000D, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000D, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x000C offset: 0x1A5F
@scena.Code('func_0C_1A5F')
def func_0C_1A5F():
    OP_A6(0x0006)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x000E, 1)
    ChrWalkTo(0x000E, -149600, 6900, 82600, 5000, 0x00)
    ChrSetDirection(0x000E, 120, 0)
    ChrSetChipByIndex(0x000E, 0)
    ChrClearFlags(0x000E, 0x0004)
    ChrJumpTo(0x000E, -148600, 4000, 80000, 2500, 5000)
    ChrSetChipByIndex(0x000E, 1)
    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000E, -146900, 4000, 79900, 5000, 0x00)
    ChrSetChipByIndex(0x000E, 0)
    CreateThread(0x000E, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000E, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Return()

# id: 0x000D offset: 0x1ADD
@scena.Code('func_0D_1ADD')
def func_0D_1ADD():
    OP_A6(0x0007)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 1)
    ChrWalkTo(0x000F, -149600, 6900, 82600, 5000, 0x00)
    ChrSetDirection(0x000F, 120, 0)
    ChrSetChipByIndex(0x000F, 0)
    ChrClearFlags(0x000F, 0x0004)
    ChrJumpTo(0x000F, -148600, 4000, 80000, 2500, 5000)
    ChrSetChipByIndex(0x000F, 1)
    ChrWalkTo(0x000F, -147100, 4000, 78100, 5000, 0x00)
    ChrSetChipByIndex(0x000F, 0)
    CreateThread(0x000F, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000F, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
