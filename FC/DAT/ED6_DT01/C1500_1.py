import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1500_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1500_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x1A69
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
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
        'loc_69C',
    )

    ClearMapFlags(0x00000001)
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
        'loc_FD',
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

    Jump('loc_182')

    def _loc_FD(): pass

    label('loc_FD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13F',
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

    Jump('loc_182')

    def _loc_13F(): pass

    label('loc_13F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_182',
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

    def _loc_182(): pass

    label('loc_182')

    @scena.Lambda('lambda_0188')
    def lambda_0188():
        CameraMove(-149500, 2000, 60700, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0188)

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
    SetChrPos(0x0101, -143800, 3500, 73400, 165)
    SetChrPos(0x0103, -143590, 2970, 74590, 165)
    SetChrPos(0x0102, -144440, 2820, 73810, 165)
    SetChrPos(0x0135, -144850, 3310, 75450, 165)

    @scena.Lambda('lambda_0273')
    def lambda_0273():
        OP_6C(300000, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_0273)

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

    @scena.Lambda('lambda_02DE')
    def lambda_02DE():
        CameraMove(-146900, 4000, 81700, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_02DE)

    @scena.Lambda('lambda_02F6')
    def lambda_02F6():
        ChrTurnDirection(0x0101, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02F6)

    @scena.Lambda('lambda_0304')
    def lambda_0304():
        ChrTurnDirection(0x0103, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0304)

    Sleep(400)

    @scena.Lambda('lambda_0317')
    def lambda_0317():
        ChrTurnDirection(0x0135, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0135, 0x0001, lambda_0317)

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
    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_692',
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
        (0x00000000, 'loc_538'),
        (0x00000001, 'loc_5BF'),
        (-1, 'loc_68F'),
    )

    def _loc_538(): pass

    label('loc_538')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0101, 0x0080)
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

    Jump('loc_68F')

    def _loc_5BF(): pass

    label('loc_5BF')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0101, 0x0080)
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
    SetChrFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_060C')
    def lambda_060C():
        ChrTurnDirection(0x0135, 0x0011, 0)
        Yield()

        Jump('lambda_060C')

    DispatchAsync2(0x0135, 0x0001, lambda_060C)

    @scena.Lambda('lambda_061D')
    def lambda_061D():
        ChrTurnDirection(0x0103, 0x0011, 0)
        Yield()

        Jump('lambda_061D')

    DispatchAsync2(0x0103, 0x0001, lambda_061D)

    @scena.Lambda('lambda_062E')
    def lambda_062E():
        ChrTurnDirection(0x0102, 0x0011, 0)
        Yield()

        Jump('lambda_062E')

    DispatchAsync2(0x0102, 0x0001, lambda_062E)

    SetChrChipByIndex(0x0011, 5)

    @scena.Lambda('lambda_0644')
    def lambda_0644():
        CameraMove(-144030, 3060, 74750, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0644)

    ChrWalkTo(0x0011, -144370, 3600, 76050, 5000, 0x00)
    SetChrChipByIndex(0x0011, 2)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)
    TerminateThread(0x0135, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0102, 0x01)
    OP_28(0x0010, 0x01, 0x0010)
    Call(1, 0x0003)

    Jump('loc_68F')

    def _loc_68F(): pass

    label('loc_68F')

    Jump('loc_4C8')

    def _loc_692(): pass

    label('loc_692')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_69C(): pass

    label('loc_69C')

    Return()

# id: 0x0001 offset: 0x69D
@scena.Code('Init')
def Init():
    @scena.Lambda('lambda_06A3')
    def lambda_06A3():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06A3)

    @scena.Lambda('lambda_06B1')
    def lambda_06B1():
        ChrTurnDirection(0x0135, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0135, 0x0001, lambda_06B1)

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

    ClearChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0102, 0x0080)
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

    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0103, 0x0080)
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
    SetChrChipByIndex(0x0011, 5)
    SetChrChipByIndex(0x0012, 6)
    SetChrChipByIndex(0x0013, 7)

    @scena.Lambda('lambda_07B5')
    def lambda_07B5():
        CameraMove(-142800, 2000, 69900, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_07B5)

    @scena.Lambda('lambda_07CD')
    def lambda_07CD():
        OP_92(0x0011, 0x0010, 3000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_07CD)

    @scena.Lambda('lambda_07E2')
    def lambda_07E2():
        OP_92(0x0013, 0x0010, 4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_07E2)

    @scena.Lambda('lambda_07F7')
    def lambda_07F7():
        OP_92(0x0012, 0x0010, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_07F7)

    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_081E')
    def lambda_081E():
        OP_92(0x0135, 0x0010, 6000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0135, 0x0002, lambda_081E)

    @scena.Lambda('lambda_0833')
    def lambda_0833():
        OP_92(0x0008, 0x0101, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0833)

    @scena.Lambda('lambda_0848')
    def lambda_0848():
        OP_92(0x0009, 0x0101, 4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0848)

    @scena.Lambda('lambda_085D')
    def lambda_085D():
        OP_92(0x000A, 0x0101, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_085D)

    @scena.Lambda('lambda_0872')
    def lambda_0872():
        OP_92(0x000B, 0x0101, 6000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0872)

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
        (0x00000001, 'loc_8BB'),
        (-1, 'loc_8BE'),
    )

    def _loc_8BB(): pass

    label('loc_8BB')

    OP_B4(0x00)

    Return()

    def _loc_8BE(): pass

    label('loc_8BE')

    EventBegin(0x00)
    CameraMove(-142800, 2000, 69900, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0011, -142200, 2500, 67300, 165)
    SetChrPos(0x0013, -143500, 2500, 67900, 165)
    SetChrPos(0x0012, -141300, 2500, 68600, 165)
    SetChrPos(0x0135, -143500, 2000, 70600, 165)
    SetChrChipByIndex(0x0011, 2)
    SetChrChipByIndex(0x0012, 3)
    SetChrChipByIndex(0x0013, 4)
    CreateThread(0x0011, 0x03, 0x00, 0x0002)
    CreateThread(0x0012, 0x03, 0x00, 0x0002)
    CreateThread(0x0013, 0x03, 0x00, 0x0002)
    SetChrPos(0x000C, -146200, 4000, 79800, 165)
    SetChrPos(0x000D, -146200, 4000, 79800, 165)
    SetChrPos(0x000E, -146200, 4000, 79800, 165)
    SetChrPos(0x000F, -146200, 4000, 79800, 165)
    SetChrChipByIndex(0x000C, 1)
    SetChrChipByIndex(0x000D, 1)
    SetChrChipByIndex(0x000E, 1)
    SetChrChipByIndex(0x000F, 1)
    OP_62(0x0135, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_09BD')
    def lambda_09BD():
        ChrWalkTo(0x0135, -142600, 2100, 65700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0135, 0x0002, lambda_09BD)

    OP_0D()
    SetChrDirection(0x0011, 345, 400)
    SetChrDirection(0x0012, 345, 400)
    SetChrDirection(0x0013, 345, 400)
    Sleep(800)

    SetChrDirection(0x0135, 345, 400)

    ChrTalk(
        0x0013,
        (
            '#0030151214V#022F好了，还剩后面的。\n',
            '集中精神！一鼓作气消灭它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A3B')
    def lambda_0A3B():
        ChrTurnDirection(0x0011, 0x000C, 0)
        Yield()

        Jump('lambda_0A3B')

    DispatchAsync2(0x0011, 0x0001, lambda_0A3B)

    @scena.Lambda('lambda_0A4C')
    def lambda_0A4C():
        ChrTurnDirection(0x0013, 0x000C, 0)
        Yield()

        Jump('lambda_0A4C')

    DispatchAsync2(0x0013, 0x0001, lambda_0A4C)

    @scena.Lambda('lambda_0A5D')
    def lambda_0A5D():
        ChrTurnDirection(0x0012, 0x000C, 0)
        Yield()

        Jump('lambda_0A5D')

    DispatchAsync2(0x0012, 0x0001, lambda_0A5D)

    @scena.Lambda('lambda_0A6E')
    def lambda_0A6E():
        OP_92(0x000C, 0x0010, 1000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0A6E)

    Sleep(400)

    @scena.Lambda('lambda_0A88')
    def lambda_0A88():
        OP_92(0x000D, 0x0010, 2000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0A88)

    Sleep(400)

    @scena.Lambda('lambda_0AA2')
    def lambda_0AA2():
        OP_92(0x000E, 0x0010, 3000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0AA2)

    Sleep(400)

    @scena.Lambda('lambda_0ABC')
    def lambda_0ABC():
        OP_92(0x000F, 0x0010, 4000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0ABC)

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
        (0x00000001, 'loc_B05'),
        (-1, 'loc_B08'),
    )

    def _loc_B05(): pass

    label('loc_B05')

    OP_B4(0x00)

    Return()

    def _loc_B08(): pass

    label('loc_B08')

    EventBegin(0x00)
    CameraMove(-142180, 2040, 67240, 0)
    SetChrPos(0x0101, -142200, 2000, 67300, 0)
    SetChrPos(0x0103, -143500, 2000, 67900, 0)
    SetChrPos(0x0102, -141300, 2000, 68600, 0)
    SetChrPos(0x0135, -143500, 2000, 70600, 0)
    SetChrPos(0x0135, -142600, 2100, 65700, 345)
    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x0103, 4)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0103, 0x0080)
    OP_0D()
    Call(1, 0x0002)

    Return()

# id: 0x0002 offset: 0xBB7
@scena.Code('ReInit')
def ReInit():
    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151223V#007F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151224V#014F总算是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0103, 65535)
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

    @scena.Lambda('lambda_0C74')
    def lambda_0C74():
        ChrTurnDirection(0x0102, 0x0135, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C74)

    SetChrDirection(0x0101, 165, 400)

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
    SetChrDirection(0x0101, 300, 2000)
    SetChrDirection(0x0101, 75, 2000)
    SetChrDirection(0x0101, 165, 2000)
    SetChrChipByIndex(0x0101, 2)
    CreateThread(0x0101, 0x00, 0x00, 0x0002)
    ChrTurnDirection(0x0103, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_F48',
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

    SetChrChipByIndex(0x0101, 65535)
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

    Jump('loc_FC1')

    def _loc_F48(): pass

    label('loc_F48')

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

    def _loc_FC1(): pass

    label('loc_FC1')

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
        'loc_10BC',
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

    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151246V#007F嘁，知道啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10BC(): pass

    label('loc_10BC')

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

# id: 0x0003 offset: 0x1129
@scena.Code('func_03_1129')
def func_03_1129():
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

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        OP_92(0x0008, 0x0101, 4800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_11F6)

    @scena.Lambda('lambda_120B')
    def lambda_120B():
        OP_92(0x0009, 0x0101, 3800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_120B)

    @scena.Lambda('lambda_1220')
    def lambda_1220():
        OP_92(0x000A, 0x0101, 4800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1220)

    @scena.Lambda('lambda_1235')
    def lambda_1235():
        OP_92(0x000B, 0x0101, 5800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1235)

    @scena.Lambda('lambda_124A')
    def lambda_124A():
        OP_92(0x000C, 0x0011, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_124A)

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        OP_92(0x000D, 0x0011, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_125F)

    @scena.Lambda('lambda_1274')
    def lambda_1274():
        OP_92(0x000E, 0x0011, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1274)

    @scena.Lambda('lambda_1289')
    def lambda_1289():
        OP_92(0x000F, 0x0011, 3000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1289)

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

    ClearChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0102, 0x0080)
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

    ClearChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0103, 0x0080)
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
        (0x00000001, 'loc_1493'),
        (-1, 'loc_1496'),
    )

    def _loc_1493(): pass

    label('loc_1493')

    OP_B4(0x00)

    Return()

    def _loc_1496(): pass

    label('loc_1496')

    EventBegin(0x00)
    CameraMove(-142180, 2040, 67240, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0103, 0x0080)
    SetChrPos(0x0101, -142200, 2000, 67300, 0)
    SetChrPos(0x0103, -143500, 2000, 67900, 0)
    SetChrPos(0x0102, -141300, 2000, 68600, 0)
    SetChrPos(0x0135, -143500, 2000, 70600, 0)
    SetChrPos(0x0135, -142600, 2100, 65700, 345)
    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x0103, 4)
    OP_0D()
    Call(1, 0x0002)

    Return()

# id: 0x0004 offset: 0x1559
@scena.Code('func_04_1559')
def func_04_1559():
    SetChrChipByIndex(0x00FE, 1)
    ChrWalkTo(0x00FE, -142590, 2050, 69490, 5000, 0x00)
    ChrWalkTo(0x00FE, -143290, 2160, 71690, 5000, 0x00)

    Return()

# id: 0x0005 offset: 0x1587
@scena.Code('func_05_1587')
def func_05_1587():
    SetChrChipByIndex(0x00FE, 1)
    ChrWalkTo(0x00FE, -145000, 4140, 77940, 5000, 0x00)
    ChrWalkTo(0x00FE, -144500, 3960, 76910, 5000, 0x00)

    Return()

# id: 0x0006 offset: 0x15B5
@scena.Code('func_06_15B5')
def func_06_15B5():
    OP_A6(0x0000)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 1)
    ChrWalkTo(0x0008, -146400, 7800, 62300, 5000, 0x00)
    SetChrDirection(0x0008, 165, 0)
    SetChrChipByIndex(0x0008, 0)
    PlaySE(129, 0x00, 0x50)
    ChrJumpTo(0x0008, -145300, 6800, 58100, 2500, 5000)
    SetChrDirection(0x0008, 75, 0)
    ClearChrFlags(0x0008, 0x0004)
    PlaySE(129, 0x00, 0x5A)
    ChrJumpTo(0x0008, -144000, 2000, 61800, 2500, 5000)
    SetChrChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_1631')
    def lambda_1631():
        CameraMove(-143500, 2500, 73000, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1631)

    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0008, -140200, 2000, 67200, 5000, 0x00)
    SetChrChipByIndex(0x0008, 0)
    CreateThread(0x0008, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x0008, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0007 offset: 0x1673
@scena.Code('func_07_1673')
def func_07_1673():
    OP_A6(0x0001)
    ClearChrFlags(0x0009, 0x0080)
    SetChrChipByIndex(0x0009, 1)
    ChrWalkTo(0x0009, -146400, 7800, 62300, 5000, 0x00)
    SetChrDirection(0x0009, 165, 0)
    SetChrChipByIndex(0x0008, 0)
    ChrJumpTo(0x0009, -145300, 6800, 58100, 2500, 5000)
    SetChrDirection(0x0008, 75, 0)
    ClearChrFlags(0x0009, 0x0004)
    ChrJumpTo(0x0009, -144000, 2000, 61800, 2500, 5000)
    SetChrChipByIndex(0x0009, 1)
    PlaySE(129, 0x00, 0x64)
    ChrWalkTo(0x0009, -142000, 2000, 68000, 5000, 0x00)
    SetChrChipByIndex(0x0009, 0)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x0009, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0008 offset: 0x170F
@scena.Code('func_08_170F')
def func_08_170F():
    OP_A6(0x0002)
    ClearChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -146400, 7800, 62300, 5000, 0x00)
    SetChrDirection(0x000A, 165, 0)
    SetChrChipByIndex(0x000A, 0)
    ChrJumpTo(0x000A, -145300, 6800, 58100, 2500, 5000)
    SetChrDirection(0x000A, 75, 0)
    ClearChrFlags(0x000A, 0x0004)
    ChrJumpTo(0x000A, -144000, 2000, 61800, 2500, 5000)
    SetChrChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -143600, 2000, 66700, 5000, 0x00)
    SetChrChipByIndex(0x000A, 0)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000A, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0009 offset: 0x17A6
@scena.Code('func_09_17A6')
def func_09_17A6():
    OP_A6(0x0003)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x000B, 1)
    ChrWalkTo(0x000B, -146400, 7800, 62300, 5000, 0x00)
    SetChrDirection(0x000B, 165, 0)
    SetChrChipByIndex(0x000B, 0)
    ChrJumpTo(0x000B, -145300, 6800, 58100, 2500, 5000)
    SetChrDirection(0x000B, 75, 0)
    ClearChrFlags(0x000B, 0x0004)
    ChrJumpTo(0x000B, -144000, 2000, 61800, 2500, 5000)
    SetChrChipByIndex(0x000B, 1)
    ChrWalkTo(0x000B, -141600, 2000, 65500, 5000, 0x00)
    SetChrChipByIndex(0x000B, 0)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000B, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x000A offset: 0x183D
@scena.Code('func_0A_183D')
def func_0A_183D():
    OP_A6(0x0004)
    ClearChrFlags(0x000C, 0x0080)
    SetChrChipByIndex(0x000C, 1)
    ChrWalkTo(0x000C, -149600, 6900, 82600, 5000, 0x00)
    SetChrDirection(0x000C, 120, 0)
    SetChrChipByIndex(0x000C, 0)
    ClearChrFlags(0x000C, 0x0004)
    PlaySE(129, 0x00, 0x50)
    ChrJumpTo(0x000C, -148600, 4000, 80000, 2500, 5000)
    SetChrChipByIndex(0x000C, 1)

    @scena.Lambda('lambda_1896')
    def lambda_1896():
        CameraMove(-143900, 2800, 74200, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1896)

    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000C, -143500, 4000, 79900, 5000, 0x00)
    SetChrChipByIndex(0x000C, 0)
    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000C, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x000B offset: 0x18D8
@scena.Code('func_0B_18D8')
def func_0B_18D8():
    OP_A6(0x0005)
    ClearChrFlags(0x000D, 0x0080)
    SetChrChipByIndex(0x000D, 1)
    ChrWalkTo(0x000D, -149600, 6900, 82600, 5000, 0x00)
    SetChrDirection(0x000D, 120, 0)
    SetChrChipByIndex(0x000D, 0)
    ClearChrFlags(0x000D, 0x0004)
    ChrJumpTo(0x000D, -148600, 4000, 80000, 2500, 5000)
    SetChrChipByIndex(0x000D, 1)
    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000D, -145600, 4000, 80300, 5000, 0x00)
    SetChrChipByIndex(0x000D, 0)
    CreateThread(0x000D, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000D, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x000C offset: 0x1956
@scena.Code('func_0C_1956')
def func_0C_1956():
    OP_A6(0x0006)
    ClearChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000E, 1)
    ChrWalkTo(0x000E, -149600, 6900, 82600, 5000, 0x00)
    SetChrDirection(0x000E, 120, 0)
    SetChrChipByIndex(0x000E, 0)
    ClearChrFlags(0x000E, 0x0004)
    ChrJumpTo(0x000E, -148600, 4000, 80000, 2500, 5000)
    SetChrChipByIndex(0x000E, 1)
    PlaySE(129, 0x00, 0x5A)
    ChrWalkTo(0x000E, -146900, 4000, 79900, 5000, 0x00)
    SetChrChipByIndex(0x000E, 0)
    CreateThread(0x000E, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000E, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Return()

# id: 0x000D offset: 0x19D4
@scena.Code('func_0D_19D4')
def func_0D_19D4():
    OP_A6(0x0007)
    ClearChrFlags(0x000F, 0x0080)
    SetChrChipByIndex(0x000F, 1)
    ChrWalkTo(0x000F, -149600, 6900, 82600, 5000, 0x00)
    SetChrDirection(0x000F, 120, 0)
    SetChrChipByIndex(0x000F, 0)
    ClearChrFlags(0x000F, 0x0004)
    ChrJumpTo(0x000F, -148600, 4000, 80000, 2500, 5000)
    SetChrChipByIndex(0x000F, 1)
    ChrWalkTo(0x000F, -147100, 4000, 78100, 5000, 0x00)
    SetChrChipByIndex(0x000F, 0)
    CreateThread(0x000F, 0x03, 0x00, 0x0002)
    ChrTurnDirection(0x000F, 0x0000, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
