import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5313_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5313_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5313.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C5313._SN', 'ED6_DT21/C5313_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    EventBegin(0x00)
    OP_20(0x000003E8)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    PlayBGM(35)
    Sleep(500)

    OP_72(0x0002, 0x0008)
    OP_6F(0x0002, 280)
    OP_70(0x0002, 300)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 280)
    OP_70(0x0003, 300)
    OP_A1(0x0019, 0x0002)
    OP_A1(0x001A, 0x0003)
    ChrSetPos(0x0019, 7660, 15000, 4860, 245)
    ChrSetPos(0x001A, -7660, 15000, 4860, 105)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_D3(0x21)
    Fade(500)
    LoadChip('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP', 33)
    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 34)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 35)
    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 36)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 37)
    LoadChip('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP', 38)
    LoadChip('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP', 39)
    LoadChip('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP', 40)
    LoadChip('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP', 41)
    LoadChip('ED6_DT27/CH04582._CH', 'ED6_DT27/CH04582P._CP', 0)
    LoadChip('ED6_DT07/CH00292._CH', 'ED6_DT07/CH00292P._CP', 1)
    LoadChip('ED6_DT07/CH00302._CH', 'ED6_DT07/CH00302P._CP', 2)
    LoadChip('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP', 3)
    LoadChip('ED6_DT07/CH00132._CH', 'ED6_DT07/CH00132P._CP', 4)
    LoadChip('ED6_DT27/CH04212._CH', 'ED6_DT27/CH04212P._CP', 8)
    LoadChip('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP', 9)
    LoadChip('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP', 10)
    LoadChip('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP', 27)
    LoadChip('ED6_DT27/CH04082._CH', 'ED6_DT27/CH04082P._CP', 28)
    LoadChip('ED6_DT26/CH20473._CH', 'ED6_DT26/CH20473P._CP', 29)
    LoadChip('ED6_DT27/CH04572._CH', 'ED6_DT27/CH04572P._CP', 31)
    LoadChip('ED6_DT26/CH20475._CH', 'ED6_DT26/CH20475P._CP', 30)
    LoadChip('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP', 32)
    OP_C0(0x17, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    ChrSetChipByIndex(0x001E, 29)
    ChrSetSubChip(0x001E, 32)
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(12200, 0, 9000, 0)
    OP_67(0, 2610, -10000, 0)
    CameraSetDistance(5250, 0)
    OP_6C(45000, 0)
    OP_6E(265, 0)
    ChrSetFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetPos(0x0008, -200, -370, 3500, 0)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 2)
    CreateThread(0x0019, 0x00, 0x01, 0x001B)
    CreateThread(0x0019, 0x03, 0x01, 0x001A)
    WaitForThreadExit(0x0019, 0x0000)
    WaitForThreadExit(0x0019, 0x0003)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_314',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_352')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33B',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_352')

    def _loc_33B(): pass

    label('loc_33B')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_352(): pass

    label('loc_352')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37E',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3BC')

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3BC')

    def _loc_3A5(): pass

    label('loc_3A5')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3BC(): pass

    label('loc_3BC')

    Sleep(1000)

    @scena.Lambda('lambda_03C7')
    def lambda_03C7():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03C7)

    Sleep(50)

    @scena.Lambda('lambda_03DA')
    def lambda_03DA():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_03DA)

    Sleep(50)

    @scena.Lambda('lambda_03ED')
    def lambda_03ED():
        ChrSetDirection(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_03ED)

    WaitForThreadExit(0x00F9, 0x0003)
    Fade(500)
    CameraMove(-12200, 0, 9000, 0)
    OP_67(0, 2610, -10000, 0)
    CameraSetDistance(5250, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    CreateThread(0x001A, 0x00, 0x01, 0x001C)
    WaitForThreadExit(0x001A, 0x0000)

    @scena.Lambda('lambda_044E')
    def lambda_044E():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_044E)

    Sleep(50)

    @scena.Lambda('lambda_0461')
    def lambda_0461():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0461)

    Sleep(80)

    @scena.Lambda('lambda_0474')
    def lambda_0474():
        ChrSetDirection(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_0474)

    WaitForThreadExit(0x00F9, 0x0003)
    Sleep(1000)

    Fade(500)
    CameraMove(0, 0, 7020, 0)
    OP_67(0, 3760, -10000, 0)
    CameraSetDistance(4540, 0)
    OP_6C(0, 0)
    OP_6E(292, 0)
    ChrSetPos(0x0019, 7660, 0, 4860, 225)
    ChrSetPos(0x001A, -7660, 0, 4860, 135)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)

    @scena.Lambda('lambda_04FE')
    def lambda_04FE():
        CameraSetDistance(5000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04FE)

    ChrSetDirection(0x0101, 45, 0)
    ChrSetDirection(0x00F8, 315, 0)
    ChrSetDirection(0x00F9, 45, 0)

    @scena.Lambda('lambda_0523')
    def lambda_0523():
        ChrJumpTo(0x00FE, 1140, -370, -1040, 500, 6000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0523)

    Sleep(50)

    @scena.Lambda('lambda_0546')
    def lambda_0546():
        ChrJumpTo(0x00FE, -920, -370, -920, 500, 6000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0546)

    Sleep(50)

    @scena.Lambda('lambda_0569')
    def lambda_0569():
        ChrJumpTo(0x00FE, 0, -370, 1480, 500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0569)

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 6)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A8',
    )

    ChrSetChipByIndex(0x0103, 11)

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5BB',
    )

    ChrSetChipByIndex(0x0104, 13)

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5CE',
    )

    ChrSetChipByIndex(0x0105, 15)

    def _loc_5CE(): pass

    label('loc_5CE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E1',
    )

    ChrSetChipByIndex(0x0106, 17)

    def _loc_5E1(): pass

    label('loc_5E1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F4',
    )

    ChrSetChipByIndex(0x0107, 19)

    def _loc_5F4(): pass

    label('loc_5F4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_607',
    )

    ChrSetChipByIndex(0x0108, 21)

    def _loc_607(): pass

    label('loc_607')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_61A',
    )

    ChrSetChipByIndex(0x0109, 23)

    def _loc_61A(): pass

    label('loc_61A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_62D',
    )

    ChrSetChipByIndex(0x010B, 25)

    def _loc_62D(): pass

    label('loc_62D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_640',
    )

    ChrSetChipByIndex(0x010F, 36)

    def _loc_640(): pass

    label('loc_640')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_653',
    )

    ChrSetChipByIndex(0x0110, 34)

    def _loc_653(): pass

    label('loc_653')

    WaitForThreadExit(0x00F8, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6B1',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411311V#173F<FIXME>これは……\n',
            'アルセイユを撃墜した……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_6B1(): pass

    label('loc_6B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411312V#065F#6P击、击坠了埃尔赛尤的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_6F6(): pass

    label('loc_6F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_735',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411313V#216F#6P那、那是什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_735(): pass

    label('loc_735')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_77D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411314V#1162F#6P击、击坠了埃尔赛尤号的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7C4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411315V#024F#6P……击坠了埃尔赛尤号的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_7C4(): pass

    label('loc_7C4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_80E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411316V#033F#6P啊……\n',
            '击坠了埃尔赛尤号的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_80E(): pass

    label('loc_80E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_858',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411317V#057F#6P哼……\n',
            '击坠了埃尔赛尤号的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_858(): pass

    label('loc_858')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_89B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411318V#077F#6P击坠了埃尔赛尤号的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E8')

    def _loc_89B(): pass

    label('loc_89B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E8',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411319V#271F<FIXME>む……\n',
            'アルセイユを撃墜した……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E8(): pass

    label('loc_8E8')

    ChrTalk(
        0x0008,
        (
            '#0140411320V#121F#5P#30W『幻想乐曲·德尔基昂』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411321V#124F怀斯曼那家伙……\n',
            '除了我的机体外还准备了其他的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    Sleep(100)

    LoadEffect(0x01, 'map\\\\mp009_00.eff')
    LoadEffect(0x02, 'battle\\\\btgun00.eff')
    LoadEffect(0x03, 'map\\\\mp019_00.eff')
    LoadEffect(0x04, 'monster\\\\ms30800a.eff')
    LoadEffect(0x05, 'monster\\\\ms30800b.eff')
    LoadEffect(0x06, 'monster\\\\ms30800c.eff')

    @scena.Lambda('lambda_09FB')
    def lambda_09FB():
        CameraSetDistance(5360, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09FB)

    CreateThread(0x0019, 0x01, 0x01, 0x0018)
    CreateThread(0x001A, 0x01, 0x01, 0x0019)
    Sleep(5000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A61',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411322V#1063F#6P果、果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_A61(): pass

    label('loc_A61')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AB9',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411323V#271F<FIXME>フン……\n',
            '簡単には通さんというわけか……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_AB9(): pass

    label('loc_AB9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AFD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411324V#072F#6P果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_AFD(): pass

    label('loc_AFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B41',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411325V#057F#6P果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_B41(): pass

    label('loc_B41')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B89',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411326V#032F#6P哟，果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_B89(): pass

    label('loc_B89')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BCD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411327V#022F#6P果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_BCD(): pass

    label('loc_BCD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C16',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411328V#1162F#6P……果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_C16(): pass

    label('loc_C16')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C5E',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411329V#212F#6P果、果然没那么容易\n',
            '过去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C9A')

    def _loc_C5E(): pass

    label('loc_C5E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C9A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411330V#065F<FIXME>は、はうぅ……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C9A(): pass

    label('loc_C9A')

    ChrTalk(
        0x0101,
        (
            '#0010411331V#1020F可恶……\n',
            '得想办法杀出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D34',
    )

    ChrSetPos(0x000B, 2800, 0, -16219, 315)

    NpcTalk(
        0x000B,
        '女性的声音',
        (
            '#0100411332V#5P──不用担心，\n',
            '这里就由我们来抵挡吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E0E')

    def _loc_D34(): pass

    label('loc_D34')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DA0',
    )

    ChrSetPos(0x000A, 2800, 0, -16219, 315)

    NpcTalk(
        0x000A,
        '男の声',
        (
            '#0110411333V#5P<FIXME>──ならば、\n',
            'ここは我々が引き受けよう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E0E')

    def _loc_DA0(): pass

    label('loc_DA0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E0E',
    )

    ChrSetPos(0x0012, 2800, 0, -16219, 315)

    NpcTalk(
        0x0012,
        '娘の声',
        (
            '#0060411334V<FIXME>──エステルさん、\n',
            'ここは私たちが引き受けます！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E0E(): pass

    label('loc_E0E')

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
        'loc_E51',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E8F')

    def _loc_E51(): pass

    label('loc_E51')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E78',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_E8F')

    def _loc_E78(): pass

    label('loc_E78')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_E8F(): pass

    label('loc_E8F')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EBB',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_EF9')

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE2',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_EF9')

    def _loc_EE2(): pass

    label('loc_EE2')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_EF9(): pass

    label('loc_EF9')

    Sleep(1000)

    ChrSetPos(0x0020, 7660, 2720, 3260, 0)
    ChrSetPos(0x0021, -7660, 3940, 3860, 0)
    CreateThread(0x0019, 0x01, 0x01, 0x001D)
    Sleep(300)

    CreateThread(0x001A, 0x01, 0x01, 0x001E)
    WaitForThreadExit(0x0019, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_0F43')
    def lambda_0F43():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F43)

    Sleep(100)

    @scena.Lambda('lambda_0F56')
    def lambda_0F56():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F56)

    @scena.Lambda('lambda_0F64')
    def lambda_0F64():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F64)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010411335V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F9F')
    def lambda_0F9F():
        CameraMove(3180, 0, -4640, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F9F)

    @scena.Lambda('lambda_0FB7')
    def lambda_0FB7():
        OP_67(0, 5090, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FB7)

    @scena.Lambda('lambda_0FCF')
    def lambda_0FCF():
        CameraSetDistance(3040, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FCF)

    @scena.Lambda('lambda_0FDF')
    def lambda_0FDF():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0FDF)

    @scena.Lambda('lambda_0FEF')
    def lambda_0FEF():
        OP_6E(354, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0FEF)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_100E',
    )

    CreateThread(0x000B, 0x01, 0x01, 0x0021)

    def _loc_100E(): pass

    label('loc_100E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1023',
    )

    CreateThread(0x000A, 0x01, 0x01, 0x0027)

    def _loc_1023(): pass

    label('loc_1023')

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_103D',
    )

    CreateThread(0x0014, 0x01, 0x01, 0x0026)

    def _loc_103D(): pass

    label('loc_103D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1052',
    )

    CreateThread(0x000F, 0x01, 0x01, 0x002B)

    def _loc_1052(): pass

    label('loc_1052')

    CreateThread(0x000E, 0x01, 0x01, 0x0028)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1073',
    )

    CreateThread(0x0012, 0x01, 0x01, 0x0023)

    def _loc_1073(): pass

    label('loc_1073')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1088',
    )

    CreateThread(0x0016, 0x01, 0x01, 0x0029)

    def _loc_1088(): pass

    label('loc_1088')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10A2',
    )

    CreateThread(0x0010, 0x01, 0x01, 0x002A)

    def _loc_10A2(): pass

    label('loc_10A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B7',
    )

    CreateThread(0x0015, 0x01, 0x01, 0x0025)

    def _loc_10B7(): pass

    label('loc_10B7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10CC',
    )

    CreateThread(0x0011, 0x01, 0x01, 0x0024)

    def _loc_10CC(): pass

    label('loc_10CC')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10E6',
    )

    CreateThread(0x0013, 0x01, 0x01, 0x002C)

    def _loc_10E6(): pass

    label('loc_10E6')

    CreateThread(0x000D, 0x01, 0x01, 0x0022)
    Sleep(300)

    ChrSetChipByIndex(0x000C, 33)
    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 3430, 0, -21410, 0)

    @scena.Lambda('lambda_1118')
    def lambda_1118():
        ChrWalkTo(0x00FE, 2920, 0, -11310, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1118)

    Sleep(900)

    WaitForThreadExit(0x000C, 0x0003)
    ChrSetDirection(0x000C, 0, 400)
    Sleep(800)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411336V#1164F尤莉亚上尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040411337V#030F<FIXME>ミュラーも……\n',
            'ナイスタイミングだ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411338V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_11F9(): pass

    label('loc_11F9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_136D',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_128B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411339V#1164F尤莉亚上尉！\n',
            '还有穆拉少校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411338V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136A')

    def _loc_128B(): pass

    label('loc_128B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12F5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060411336V#1164F尤莉亚上尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411342V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136A')

    def _loc_12F5(): pass

    label('loc_12F5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_136A',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411343V#173F<FIXME>ミュラー少佐……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411342V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_136A(): pass

    label('loc_136A')

    Jump('loc_1A35')

    def _loc_136D(): pass

    label('loc_136D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14E0',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13FA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411345V#033F啊，穆拉！\n',
            '还有尤莉亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411338V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_13FA(): pass

    label('loc_13FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_146E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411347V#273F<FIXME>……ユリア大尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_146E(): pass

    label('loc_146E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14DD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040411349V#033F啊，吾友！\n',
            '来得正好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F还有大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14DD(): pass

    label('loc_14DD')

    Jump('loc_1A35')

    def _loc_14E0(): pass

    label('loc_14E0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_166D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010411351V#1004F尤莉亚上尉，穆拉少校！\n',
            '而且大家也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1576',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411352V#023F怎、怎么会来到这里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166A')

    def _loc_1576(): pass

    label('loc_1576')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15B8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411353V#070F哈哈，你们竟然来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166A')

    def _loc_15B8(): pass

    label('loc_15B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15F7',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411354V#1064F怎、怎么会来到这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166A')

    def _loc_15F7(): pass

    label('loc_15F7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1633',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411355V#051F喂喂……这是真的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_166A')

    def _loc_1633(): pass

    label('loc_1633')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_166A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411356V#560F连、连爷爷都……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_166A(): pass

    label('loc_166A')

    Jump('loc_1A35')

    def _loc_166D(): pass

    label('loc_166D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16DD',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411347V#273F<FIXME>……ユリア大尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_16DD(): pass

    label('loc_16DD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1751',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411343V#173F<FIXME>ミュラー少佐……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_1751(): pass

    label('loc_1751')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17CA',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411361V#173F<FIXME>で、殿下……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411362V#1004F大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_17CA(): pass

    label('loc_17CA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1845',
    )

    ChrTalk(
        0x0110,
        (
            '#0110411347V#273F<FIXME>……ユリア大尉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_1845(): pass

    label('loc_1845')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18C4',
    )

    ChrTalk(
        0x010F,
        (
            '#0100411343V#173F<FIXME>ミュラー少佐……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411348V#1004F大家……\n',
            '怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_18C4(): pass

    label('loc_18C4')

    ChrTalk(
        0x0101,
        (
            '#0010411351V#1004F尤莉亚上尉，穆拉少校！\n',
            '而且大家也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1941',
    )

    ChrTalk(
        0x0103,
        (
            '#0030411352V#023F怎、怎么会来到这里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_1941(): pass

    label('loc_1941')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1983',
    )

    ChrTalk(
        0x0108,
        (
            '#0080411353V#070F哈哈，你们竟然来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_1983(): pass

    label('loc_1983')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C2',
    )

    ChrTalk(
        0x0109,
        (
            '#0180411354V#1064F怎、怎么会来到这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_19C2(): pass

    label('loc_19C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19FE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050411355V#051F喂喂……这是真的吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A35')

    def _loc_19FE(): pass

    label('loc_19FE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A35',
    )

    ChrTalk(
        0x0107,
        (
            '#0070411356V#560F连、连爷爷都……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A35(): pass

    label('loc_1A35')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A87',
    )

    ChrTalk(
        0x000B,
        (
            '#0100411373V#170F#2P呵呵，因为埃尔赛尤号的修理\n',
            '快要完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B43')

    def _loc_1A87(): pass

    label('loc_1A87')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AEC',
    )

    ChrTalk(
        0x0012,
        (
            '#0060411374V#1168F<FIXME>ふふ、アルセイユの修理が\n',
            'そろそろ完了しそうなので……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B43')

    def _loc_1AEC(): pass

    label('loc_1AEC')

    ChrTalk(
        0x0010,
        (
            '#0030411375V#027F<FIXME>ふふっ、アルセイユの修理も\n',
            'そろそろ終わるって話だからね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B43(): pass

    label('loc_1B43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B91',
    )

    ChrTalk(
        0x000A,
        (
            '#0110411376V#277F#6P我们就召集了\n',
            '能帮忙的人都来帮忙了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2F')

    def _loc_1B91(): pass

    label('loc_1B91')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BEB',
    )

    ChrTalk(
        0x0010,
        (
            '#0030411377V#526F<FIXME>動ける連中を集めて\n',
            '加勢しに来たってワケよ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C2F')

    def _loc_1BEB(): pass

    label('loc_1BEB')

    ChrTalk(
        0x0012,
        (
            '#0060411378V#1168F<FIXME>手の空いた方々で\n',
            '加勢しに来たんです！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C2F(): pass

    label('loc_1C2F')

    ChrTalk(
        0x000C,
        (
            '#0540411379V#103F虽然我们帮不上什么大忙……\n',
            '不过来得似乎正是时候啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D5F',
    )

    ChrTalk(
        0x010B,
        (
            '#0090411380V#213F啊、哥哥！你们……怎么也！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300411381V#191F哦，山猫号的修理也\n',
            '快要完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0290411382V#200F#6P所以为了看看我们可爱的妹妹\n',
            '就跑过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090411383V#415F多伦哥……吉尔哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E28')

    def _loc_1D5F(): pass

    label('loc_1D5F')

    ChrTalk(
        0x0016,
        (
            '#0090411384V#210F哼哼，也别\n',
            '把我们忘了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300411385V#490F反正山猫号的修理也\n',
            '快要完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0290411386V#202F#6P所以想看看你们怎么样了，\n',
            '于是就跑了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010411387V#1025F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E28(): pass

    label('loc_1E28')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E6F',
    )

    ChrTalk(
        0x0015,
        (
            '#0180411388V#1061F不过说起来……\n',
            '还真是正好赶上啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E6F(): pass

    label('loc_1E6F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EB8',
    )

    ChrTalk(
        0x000F,
        (
            '#0050411389V#054F有话以后再说！\n',
            '这里就交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F92')

    def _loc_1EB8(): pass

    label('loc_1EB8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EF7',
    )

    ChrTalk(
        0x0010,
        (
            '#0030411390V#024F总之这里\n',
            '就交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F92')

    def _loc_1EF7(): pass

    label('loc_1EF7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F43',
    )

    ChrTalk(
        0x0014,
        (
            '#0080411391V#076F#2P有话以后再说！\n',
            '这里就交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F92')

    def _loc_1F43(): pass

    label('loc_1F43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F92',
    )

    ChrTalk(
        0x000B,
        (
            '#0100411392V#177F<FIXME>話は後だ！\n',
            'ここは我々に任せてくれ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F92(): pass

    label('loc_1F92')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FDC',
    )

    ChrTalk(
        0x0012,
        (
            '#0060411393V#1162F艾丝蒂尔你们快\n',
            '去约修亚那里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B6')

    def _loc_1FDC(): pass

    label('loc_1FDC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2028',
    )

    ChrTalk(
        0x0013,
        (
            '#0070411394V#062F姐、姐姐你们\n',
            '快点去约修亚哥哥\n',
            '那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B6')

    def _loc_2028(): pass

    label('loc_2028')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2078',
    )

    ChrTalk(
        0x0011,
        (
            '#0040411395V#030F#2P呵呵，艾丝蒂尔你们\n',
            '快点去约修亚那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B6')

    def _loc_2078(): pass

    label('loc_2078')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20B6',
    )

    ChrTalk(
        0x000A,
        (
            '#0110411396V#271F<FIXME>君たちは先へ進め！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B6(): pass

    label('loc_20B6')

    ChrTalk(
        0x0101,
        (
            '#0010411397V#1025F大家……谢谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(2230, -370, 3460, 0)
    OP_67(0, 5090, -10000, 0)
    CameraSetDistance(2160, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140411398V#121F#5P#30W快去……！\n',
            '艾丝蒂尔·布莱特……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140411399V……用你的光芒\n',
            '去救回约修亚吧……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010411400V#1006F#6P……嗯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(3180, 0, -4640, 0)
    OP_67(0, 5090, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_224D',
    )

    ChrTalk(
        0x000B,
        (
            '#0100411401V#177F#2P要上了！各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BF')

    def _loc_224D(): pass

    label('loc_224D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_228F',
    )

    ChrTalk(
        0x0012,
        (
            '#0060411402V#1166F<FIXME>それでは皆さん……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22BF')

    def _loc_228F(): pass

    label('loc_228F')

    ChrTalk(
        0x0010,
        (
            '#0030411403V#024F<FIXME>それじゃ行くわよ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22BF(): pass

    label('loc_22BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22FC',
    )

    ChrTalk(
        0x000A,
        (
            '#0110411404V#271F#6P兵分两路击破它们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2380')

    def _loc_22FC(): pass

    label('loc_22FC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2347',
    )

    ChrTalk(
        0x0010,
        (
            '#0030411405V#024F<FIXME>二手に分かれて撃破するわよ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2380')

    def _loc_2347(): pass

    label('loc_2347')

    ChrTalk(
        0x0012,
        (
            '#0060411406V#1166F<FIXME>二手に分かれて撃破します！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2380(): pass

    label('loc_2380')

    Sleep(500)

    OP_D7(0x00, 0, 0)
    SetMessageWindowPos(390, 260, -1, -1)
    TalkSetChrName('伙伴们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0300411407V#5S噢噢！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()

    @scena.Lambda('lambda_23DC')
    def lambda_23DC():
        CameraMove(2460, 0, 6450, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_23DC)

    @scena.Lambda('lambda_23F4')
    def lambda_23F4():
        OP_67(0, 8050, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23F4)

    @scena.Lambda('lambda_240C')
    def lambda_240C():
        CameraSetDistance(6690, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_240C)

    @scena.Lambda('lambda_241C')
    def lambda_241C():
        OP_6E(292, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_241C)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_243B',
    )

    CreateThread(0x000B, 0x01, 0x01, 0x002D)

    def _loc_243B(): pass

    label('loc_243B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉2'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2450',
    )

    CreateThread(0x000A, 0x01, 0x01, 0x0033)

    def _loc_2450(): pass

    label('loc_2450')

    TerminateThread(0x0019, 0x01)
    CreateThread(0x0019, 0x01, 0x01, 0x001F)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2475',
    )

    CreateThread(0x0014, 0x01, 0x01, 0x0032)

    def _loc_2475(): pass

    label('loc_2475')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_248A',
    )

    CreateThread(0x000F, 0x01, 0x01, 0x0037)

    def _loc_248A(): pass

    label('loc_248A')

    CreateThread(0x000E, 0x01, 0x01, 0x0034)
    TerminateThread(0x001A, 0x01)
    CreateThread(0x001A, 0x01, 0x01, 0x0020)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24B6',
    )

    CreateThread(0x0012, 0x01, 0x01, 0x002F)

    def _loc_24B6(): pass

    label('loc_24B6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24CB',
    )

    CreateThread(0x0016, 0x01, 0x01, 0x0035)

    def _loc_24CB(): pass

    label('loc_24CB')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24E5',
    )

    CreateThread(0x0010, 0x01, 0x01, 0x0036)

    def _loc_24E5(): pass

    label('loc_24E5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24FA',
    )

    CreateThread(0x0011, 0x01, 0x01, 0x0030)

    def _loc_24FA(): pass

    label('loc_24FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_250F',
    )

    CreateThread(0x0015, 0x01, 0x01, 0x0031)

    def _loc_250F(): pass

    label('loc_250F')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2529',
    )

    CreateThread(0x0013, 0x01, 0x01, 0x0038)

    def _loc_2529(): pass

    label('loc_2529')

    CreateThread(0x000D, 0x01, 0x01, 0x002E)
    Sleep(300)

    CreateThread(0x0101, 0x01, 0x01, 0x000F)

    @scena.Lambda('lambda_2542')
    def lambda_2542():
        CameraMove(0, 0, 33380, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2542)

    Sleep(300)

    @scena.Lambda('lambda_255F')
    def lambda_255F():
        OP_99(0x00FE, 0x02, 0x01, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_255F)

    CreateThread(0x00F8, 0x01, 0x01, 0x0010)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x01, 0x0011)
    WaitForThreadExit(0x00F9, 0x0001)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0016, 0x01)
    Fade(500)
    CameraMove(-1090, 4010, 33290, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    PlaySE(200, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 300)
    Sleep(1000)

    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_2617')
    def lambda_2617():
        CameraMove(240, 4010, 34250, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2617)

    @scena.Lambda('lambda_262F')
    def lambda_262F():
        OP_67(0, 17360, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_262F)

    PlaySE(104, 0x00, 0x64)
    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    FormationDelMember(0x01, 0xFF)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5315._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x2667
@scena.Code('func_03_2667')
def func_03_2667():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26B2',
    )

    PlayEffect(0x03, 0xFF, 0x0008, -300, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    Sleep(100)

    Jump('func_03_2667')

    def _loc_26B2(): pass

    label('loc_26B2')

    Return()

# id: 0x0004 offset: 0x26B3
@scena.Code('func_04_26B3')
def func_04_26B3():
    ChrSetChipByIndex(0x00FE, 32)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetPos(0x00FE, 4059, 700, -430, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_26D9')
    def lambda_26D9():
        OP_99(0x00FE, 0x00, 0x07, 3500)
        Yield()

        Jump('lambda_26D9')

    DispatchAsync2(0x00FE, 0x0002, lambda_26D9)

    @scena.Lambda('lambda_26EC')
    def lambda_26EC():
        ChrJumpTo(0x00FE, 8510, 0, -6430, 5000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_26EC)

    Sleep(2000)

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_2713')
    def lambda_2713():
        OP_99(0x00FE, 0x18, 0x20, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2713)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    Return()

# id: 0x0005 offset: 0x272D
@scena.Code('func_05_272D')
def func_05_272D():
    LoadChip('ED6_DT26/CH20473._CH', 'ED6_DT26/CH20473P._CP', 29)
    LoadChip('ED6_DT26/CH20475._CH', 'ED6_DT26/CH20475P._CP', 30)
    ChrSetChipByIndex(0x001E, 29)
    ChrSetSubChip(0x001E, 32)
    ChrSetChipByIndex(0x0008, 30)
    ChrSetSubChip(0x0008, 2)
    ChrSetFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0002)
    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 11)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 12)
    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 13)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 14)
    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 15)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 16)
    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 17)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 18)
    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 19)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 20)
    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 21)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 22)
    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 23)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 24)
    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 25)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 26)
    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 34)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 35)
    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 36)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 37)

    Return()

# id: 0x0006 offset: 0x2828
@scena.Code('func_06_2828')
def func_06_2828():
    LoadChip('ED6_DT27/CH04582._CH', 'ED6_DT27/CH04582P._CP', 0)
    LoadChip('ED6_DT07/CH00292._CH', 'ED6_DT07/CH00292P._CP', 1)
    LoadChip('ED6_DT07/CH00302._CH', 'ED6_DT07/CH00302P._CP', 2)
    LoadChip('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP', 3)
    LoadChip('ED6_DT07/CH00132._CH', 'ED6_DT07/CH00132P._CP', 4)
    LoadChip('ED6_DT27/CH04212._CH', 'ED6_DT27/CH04212P._CP', 8)
    LoadChip('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP', 9)
    LoadChip('ED6_DT07/CH00162._CH', 'ED6_DT07/CH00162P._CP', 10)
    LoadChip('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP', 27)
    LoadChip('ED6_DT27/CH04082._CH', 'ED6_DT27/CH04082P._CP', 28)
    LoadChip('ED6_DT27/CH04572._CH', 'ED6_DT27/CH04572P._CP', 31)
    LoadChip('ED6_DT07/CH00312._CH', 'ED6_DT07/CH00312P._CP', 32)

    Return()

# id: 0x0007 offset: 0x28A1
@scena.Code('func_07_28A1')
def func_07_28A1():
    LoadChip('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP', 33)
    LoadChip('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP', 38)
    LoadChip('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP', 39)
    LoadChip('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP', 40)
    LoadChip('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP', 41)

    Return()

# id: 0x0008 offset: 0x28D4
@scena.Code('func_08_28D4')
def func_08_28D4():
    LoadEffect(0x01, 'map\\\\mp009_00.eff')
    LoadEffect(0x02, 'battle\\\\btgun00.eff')
    LoadEffect(0x03, 'map\\\\mp019_00.eff')
    LoadEffect(0x04, 'monster\\\\ms30800a.eff')
    LoadEffect(0x05, 'monster\\\\ms30800b.eff')

    Return()

# id: 0x0009 offset: 0x2943
@scena.Code('func_09_2943')
def func_09_2943():
    ChrSetDirection(0x00FE, 35, 0)
    ChrMoveTo(0x00FE, 640, -370, 640, 5000, 0x00)

    Return()

# id: 0x000A offset: 0x295F
@scena.Code('func_0A_295F')
def func_0A_295F():
    ChrSetDirection(0x00FE, 35, 0)
    ChrMoveTo(0x00FE, -980, -370, -240, 5000, 0x00)

    Return()

# id: 0x000B offset: 0x297B
@scena.Code('func_0B_297B')
def func_0B_297B():
    ChrSetDirection(0x00FE, 35, 0)
    ChrMoveTo(0x00FE, 520, -370, -800, 5000, 0x00)

    Return()

# id: 0x000C offset: 0x2997
@scena.Code('func_0C_2997')
def func_0C_2997():
    ChrWalkTo(0x00FE, 200, -370, 2160, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000D offset: 0x29B3
@scena.Code('func_0D_29B3')
def func_0D_29B3():
    ChrWalkTo(0x00FE, -720, -370, 600, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000E offset: 0x29CF
@scena.Code('func_0E_29CF')
def func_0E_29CF():
    ChrWalkTo(0x00FE, 690, -370, 810, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x29EB
@scena.Code('func_0F_29EB')
def func_0F_29EB():
    ChrWalkTo(0x00FE, 990, -370, 3430, 6000, 0x00)
    ChrWalkTo(0x00FE, 0, 4010, 34190, 6000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x2A1B
@scena.Code('func_10_2A1B')
def func_10_2A1B():
    ChrWalkTo(0x00FE, -1800, -370, 3200, 6000, 0x00)
    ChrWalkTo(0x00FE, -1080, 4010, 32500, 6000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0011 offset: 0x2A4B
@scena.Code('func_11_2A4B')
def func_11_2A4B():
    ChrWalkTo(0x00FE, -1800, -370, 3650, 6000, 0x00)
    ChrWalkTo(0x00FE, 220, 0, 12700, 6000, 0x00)
    ChrWalkTo(0x00FE, 0, 4010, 25530, 6000, 0x00)
    ChrWalkTo(0x00FE, 1080, 4010, 32500, 6000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x2AA3
@scena.Code('func_12_2AA3')
def func_12_2AA3():
    Sleep(500)

    ChrClearFlags(0x0102, 0x0002)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 29)

    @scena.Lambda('lambda_2AC7')
    def lambda_2AC7():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AC7)

    @scena.Lambda('lambda_2AD7')
    def lambda_2AD7():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2AD7)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2AEC')
    def lambda_2AEC():
        ChrMoveTo(0x00FE, 340, -370, -1670, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AEC)

    ChrMoveTo(0x0102, -410, -370, 2130, 20000, 0x00)
    Sleep(500)

    @scena.Lambda('lambda_2B20')
    def lambda_2B20():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B20')

    DispatchAsync2(0x0102, 0x0003, lambda_2B20)

    @scena.Lambda('lambda_2B31')
    def lambda_2B31():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2B31')

    DispatchAsync2(0x0008, 0x0003, lambda_2B31)

    @scena.Lambda('lambda_2B42')
    def lambda_2B42():
        ChrJumpTo(0x00FE, 2550, -370, 3340, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2B42)

    ChrJumpTo(0x0102, 350, -370, 3400, 500, 10000)
    def _loc_2B71(): pass

    label('loc_2B71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2D95',
    )

    @scena.Lambda('lambda_2B7E')
    def lambda_2B7E():
        OP_99(0x00FE, 0x00, 0x05, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B7E)

    @scena.Lambda('lambda_2B8E')
    def lambda_2B8E():
        OP_99(0x00FE, 0x00, 0x05, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2B8E)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2BA3')
    def lambda_2BA3():
        ChrJumpTo(0x00FE, -1430, -370, -2680, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2BA3)

    ChrJumpTo(0x0102, -240, -370, -2990, 500, 10000)

    @scena.Lambda('lambda_2BD8')
    def lambda_2BD8():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2BD8)

    @scena.Lambda('lambda_2BE8')
    def lambda_2BE8():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2BE8)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2BFD')
    def lambda_2BFD():
        ChrMoveTo(0x00FE, -240, -370, -2990, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2BFD)

    ChrMoveTo(0x0102, -1430, -370, -2680, 20000, 0x00)

    @scena.Lambda('lambda_2C2C')
    def lambda_2C2C():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2C2C)

    @scena.Lambda('lambda_2C3C')
    def lambda_2C3C():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C3C)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2C51')
    def lambda_2C51():
        ChrJumpTo(0x00FE, 1870, -370, -1060, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2C51)

    ChrJumpTo(0x0102, 1930, -370, -1930, 500, 10000)
    Sleep(500)

    @scena.Lambda('lambda_2C8B')
    def lambda_2C8B():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2C8B)

    @scena.Lambda('lambda_2C9B')
    def lambda_2C9B():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C9B)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2CB0')
    def lambda_2CB0():
        ChrMoveTo(0x00FE, -240, -370, -2990, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CB0)

    ChrMoveTo(0x0102, -1430, -370, -2680, 20000, 0x00)

    @scena.Lambda('lambda_2CDF')
    def lambda_2CDF():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2CDF)

    @scena.Lambda('lambda_2CEF')
    def lambda_2CEF():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2CEF)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2D04')
    def lambda_2D04():
        ChrJumpTo(0x00FE, 2180, -370, 1050, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D04)

    ChrJumpTo(0x0102, 960, -370, 1090, 500, 10000)

    @scena.Lambda('lambda_2D39')
    def lambda_2D39():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2D39)

    @scena.Lambda('lambda_2D49')
    def lambda_2D49():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D49)

    PlaySE(214, 0x00, 0x46)

    @scena.Lambda('lambda_2D5E')
    def lambda_2D5E():
        ChrJumpTo(0x00FE, -1890, -370, -480, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D5E)

    ChrJumpTo(0x0102, -2270, -370, 790, 500, 10000)
    Sleep(500)

    Jump('loc_2B71')

    def _loc_2D95(): pass

    label('loc_2D95')

    @scena.Lambda('lambda_2D9B')
    def lambda_2D9B():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2D9B)

    @scena.Lambda('lambda_2DAB')
    def lambda_2DAB():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2DAB)

    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2DC0')
    def lambda_2DC0():
        ChrJumpTo(0x00FE, 1870, -370, -1060, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2DC0)

    ChrJumpTo(0x0102, 1930, -370, -1930, 500, 10000)

    @scena.Lambda('lambda_2DF5')
    def lambda_2DF5():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2DF5)

    @scena.Lambda('lambda_2E05')
    def lambda_2E05():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E05)

    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2E1A')
    def lambda_2E1A():
        ChrJumpTo(0x00FE, 2180, -370, 1050, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E1A)

    ChrJumpTo(0x0102, 960, -370, 1090, 500, 10000)

    @scena.Lambda('lambda_2E4F')
    def lambda_2E4F():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E4F)

    @scena.Lambda('lambda_2E5F')
    def lambda_2E5F():
        OP_99(0x00FE, 0x00, 0x05, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E5F)

    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_2E74')
    def lambda_2E74():
        ChrJumpTo(0x00FE, 2180, -370, 1050, 500, 10000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E74)

    ChrMoveTo(0x0102, -580, -370, 870, 20000, 0x00)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 8)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 28)

    @scena.Lambda('lambda_2EBA')
    def lambda_2EBA():
        ChrJumpTo(0x00FE, -3220, -370, 0, 500, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2EBA)

    ChrJumpTo(0x0008, 3220, -370, 0, 500, 10000)
    Sleep(1000)

    @scena.Lambda('lambda_2EF4')
    def lambda_2EF4():
        ChrMoveTo(0x00FE, 0, -370, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2EF4)

    ChrMoveTo(0x0102, 100, -370, 0, 20000, 0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 3)
    CreateThread(0x0101, 0x02, 0x00, 0x0016)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0013 offset: 0x2F41
@scena.Code('func_13_2F41')
def func_13_2F41():
    ChrSetSubChip(0x001B, 23)
    ChrSetChipByIndex(0x001B, 1)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x001B, -560, -370, 2940, 0)
    ChrMoveTo(0x001B, 340, 0, -3710, 25000, 0x00)
    ChrMoveTo(0x001B, 340, 10000, -3710, 25000, 0x00)
    ChrSetFlags(0x001B, 0x0080)

    Return()

# id: 0x0014 offset: 0x2F8F
@scena.Code('func_14_2F8F')
def func_14_2F8F():
    ChrSetSubChip(0x001C, 23)
    ChrSetChipByIndex(0x001C, 1)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, -560, -370, 2940, 0)
    ChrMoveTo(0x001C, 340, 0, -3710, 25000, 0x00)
    ChrMoveTo(0x001C, 20340, 4000, -3710, 25000, 0x00)
    ChrSetFlags(0x001C, 0x0080)

    Return()

# id: 0x0015 offset: 0x2FDD
@scena.Code('func_15_2FDD')
def func_15_2FDD():
    ChrSetSubChip(0x001D, 23)
    ChrSetChipByIndex(0x001D, 1)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -560, -370, 2940, 0)
    ChrMoveTo(0x001D, 340, 0, -3710, 25000, 0x00)
    ChrMoveTo(0x001D, -20340, 5000, -3710, 25000, 0x00)
    ChrSetFlags(0x001D, 0x0080)

    Return()

# id: 0x0016 offset: 0x302B
@scena.Code('func_16_302B')
def func_16_302B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3040',
    )

    OP_99(0x0008, 0x00, 0x07, 2500)

    Jump('func_16_302B')

    def _loc_3040(): pass

    label('loc_3040')

    Return()

# id: 0x0017 offset: 0x3041
@scena.Code('func_17_3041')
def func_17_3041():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_308D',
    )

    ExecExpressionWithValue(
        0x001F,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_17_3041')

    def _loc_308D(): pass

    label('loc_308D')

    Return()

# id: 0x0018 offset: 0x308E
@scena.Code('func_18_308E')
def func_18_308E():
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 880)
    OP_70(0x0002, 940)
    PlaySE(322, 0x00, 0x64)
    Sleep(2000)

    Play3DEffect(0x04, 0x01, 0x02, 'Frame34_Bone__33_', 0x00000000, 0x00000000, 0x00000000, 0x0037, 0x00BE, 0x00A5, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Sleep(50)

    PlaySE(323, 0x00, 0x64)
    Play3DEffect(0x05, 0x02, 0x02, 'Frame26_Bone__25_', 0x00000000, 0x00000000, 0x00000000, 0x0037, 0x00AA, 0x00A5, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 950)
    OP_70(0x0002, 970)

    Return()

# id: 0x0019 offset: 0x3142
@scena.Code('func_19_3142')
def func_19_3142():
    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 880)
    OP_70(0x0003, 940)
    Sleep(2000)

    Play3DEffect(0x04, 0x03, 0x03, 'Frame34_Bone__33_', 0x00000000, 0x00000000, 0x00000000, 0x013B, 0x00BE, 0x00A5, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Sleep(50)

    Play3DEffect(0x05, 0x04, 0x03, 'Frame26_Bone__25_', 0x00000000, 0x00000000, 0x00000000, 0x013B, 0x00AA, 0x00A5, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    OP_73(0x0003)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 950)
    OP_70(0x0003, 970)

    Return()

# id: 0x001A offset: 0x31EC
@scena.Code('func_1A_31EC')
def func_1A_31EC():
    OP_24(0x0158, 0x55)
    Sleep(100)

    OP_24(0x0158, 0x5A)
    Sleep(100)

    OP_24(0x0158, 0x5F)
    Sleep(100)

    OP_24(0x0158, 0x64)

    Return()

# id: 0x001B offset: 0x320C
@scena.Code('func_1B_320C')
def func_1B_320C():
    @scena.Lambda('lambda_3212')
    def lambda_3212():
        ChrMoveTo(0x00FE, 7660, 0, 4860, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3212)

    WaitForThreadExit(0x0019, 0x0001)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 300)
    OP_70(0x0002, 310)
    Sleep(200)

    PlaySE(136, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    OP_7C(0, 400, 5000, 1500)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 20)

    Return()

# id: 0x001C offset: 0x3276
@scena.Code('func_1C_3276')
def func_1C_3276():
    Sleep(200)

    @scena.Lambda('lambda_3281')
    def lambda_3281():
        ChrMoveTo(0x00FE, -7660, 0, 4860, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_3281)

    WaitForThreadExit(0x001A, 0x0001)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 300)
    OP_70(0x0003, 310)
    Sleep(200)

    OP_23(0x0158)
    PlaySE(136, 0x00, 0x64)
    PlaySE(245, 0x00, 0x64)
    OP_7C(0, 400, 5000, 1500)
    OP_73(0x0003)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 20)

    Return()

# id: 0x001D offset: 0x32E8
@scena.Code('func_1D_32E8')
def func_1D_32E8():
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, 4280, 2240, -14080, 0, 0, 0, 1000, 1000, 1000, 0x0020, 0, 0, 0, 0)
    Sleep(1000)

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 110)
    OP_70(0x0002, 140)
    OP_23(0x0143)
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    OP_73(0x0002)
    Sleep(100)

    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 210)
    OP_70(0x0002, 230)
    ChrSetDirection(0x0019, 195, 50)
    OP_D8(0x02, 0x01F4)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 20)
    PlaySE(236, 0x00, 0x64)

    Return()

# id: 0x001E offset: 0x337D
@scena.Code('func_1E_337D')
def func_1E_337D():
    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x00FF, -3400, 2740, -14080, 0, 0, 0, 1000, 1000, 1000, 0x0021, 0, 0, 0, 0)
    Sleep(1000)

    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 110)
    OP_70(0x0003, 140)
    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    OP_73(0x0003)
    OP_71(0x0003, 0x0020)
    Sleep(100)

    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 240)
    OP_70(0x0003, 260)
    ChrSetDirection(0x001A, 165, 50)
    OP_D8(0x03, 0x01F4)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 20)

    Return()

# id: 0x001F offset: 0x340F
@scena.Code('func_1F_340F')
def func_1F_340F():
    OP_6F(0x0002, 210)
    OP_70(0x0002, 230)
    ChrSetDirection(0x0019, 180, 50)
    OP_D8(0x02, 0x01F4)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 20)
    Sleep(1000)

    def _loc_3440(): pass

    label('loc_3440')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3467',
    )

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 110)
    OP_70(0x0002, 140)
    OP_73(0x0002)
    Sleep(100)

    Jump('loc_3440')

    def _loc_3467(): pass

    label('loc_3467')

    Return()

# id: 0x0020 offset: 0x3468
@scena.Code('func_20_3468')
def func_20_3468():
    OP_6F(0x0003, 240)
    OP_70(0x0003, 260)
    ChrSetDirection(0x001A, 180, 50)
    OP_D8(0x03, 0x01F4)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 20)
    Sleep(1000)

    def _loc_3499(): pass

    label('loc_3499')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34C0',
    )

    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 110)
    OP_70(0x0003, 140)
    OP_73(0x0003)
    Sleep(100)

    Jump('loc_3499')

    def _loc_34C0(): pass

    label('loc_34C0')

    Return()

# id: 0x0021 offset: 0x34C1
@scena.Code('func_21_34C1')
def func_21_34C1():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x000B, 37)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 2800, 0, -16219, 315)
    ChrWalkTo(0x000B, 2860, 0, -6430, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x000B, 36)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0022 offset: 0x350C
@scena.Code('func_22_350C')
def func_22_350C():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x000D, 39)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 1290, 0, -21350, 315)
    ChrWalkTo(0x000D, 390, 0, -11310, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x000D, 38)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0023 offset: 0x3557
@scena.Code('func_23_3557')
def func_23_3557():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0012, 16)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 4710, 0, -17770, 315)
    ChrWalkTo(0x0012, 4070, 0, -7560, 5000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    ChrSetChipByIndex(0x0012, 15)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0024 offset: 0x35A2
@scena.Code('func_24_35A2')
def func_24_35A2():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0011, 14)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 6070, 0, -19890, 315)
    ChrWalkTo(0x0011, 5950, 0, -7380, 5000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)
    ChrSetChipByIndex(0x0011, 13)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0025 offset: 0x35ED
@scena.Code('func_25_35ED')
def func_25_35ED():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0015, 24)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 5800, 0, -18920, 315)
    ChrWalkTo(0x0015, 3420, 0, -9420, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0015, 23)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0026 offset: 0x3638
@scena.Code('func_26_3638')
def func_26_3638():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0014, 22)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, 3830, 0, -16930, 315)
    ChrWalkTo(0x0014, 4830, 0, -6110, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0014, 21)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0027 offset: 0x367E
@scena.Code('func_27_367E')
def func_27_367E():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x000A, 0x1000)
    ChrSetChipByIndex(0x000A, 35)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -100, 0, -17210, 0)
    ChrWalkTo(0x000A, -100, 0, -7210, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x000A, 34)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0028 offset: 0x36CE
@scena.Code('func_28_36CE')
def func_28_36CE():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x000E, 41)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 30, 0, -18260, 0)
    ChrWalkTo(0x000E, -1420, 0, -9290, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x000E, 40)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0029 offset: 0x3719
@scena.Code('func_29_3719')
def func_29_3719():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0016, 26)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, 20, 0, -19250, 0)
    ChrWalkTo(0x0016, 20, 0, -9250, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0016, 25)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x002A offset: 0x3764
@scena.Code('func_2A_3764')
def func_2A_3764():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0010, 12)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 1370, 0, -20350, 0)
    ChrWalkTo(0x0010, 1720, 0, -9620, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0010, 11)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x002B offset: 0x37AF
@scena.Code('func_2B_37AF')
def func_2B_37AF():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x000F, 18)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 590, 0, -20100, 0)
    ChrWalkTo(0x000F, 1350, 0, -8420, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x000F, 17)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x002C offset: 0x37FA
@scena.Code('func_2C_37FA')
def func_2C_37FA():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetChipByIndex(0x0013, 20)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 5950, 0, -19260, 0)
    ChrWalkTo(0x0013, 5050, 0, -9520, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrSetChipByIndex(0x0013, 19)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x002D offset: 0x3845
@scena.Code('func_2D_3845')
def func_2D_3845():
    ChrSetChipByIndex(0x000B, 37)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x000B, 7470, 0, 3320, 7000, 0x00)
    ChrSetDirection(0x000B, 0, 0)
    ChrSetChipByIndex(0x000B, 0)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3874(): pass

    label('loc_3874')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_388C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3874')

    def _loc_388C(): pass

    label('loc_388C')

    Return()

# id: 0x002E offset: 0x388D
@scena.Code('func_2E_388D')
def func_2E_388D():
    ChrSetChipByIndex(0x000D, 39)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x000D, -6210, 0, -2250, 7000, 0x00)
    ChrSetDirection(0x000D, 0, 0)
    ChrSetChipByIndex(0x000D, 1)
    ChrSetSubChip(0x00FE, 0)
    def _loc_38BC(): pass

    label('loc_38BC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3910',
    )

    PlaySE(506, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x000D, 1000, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x001A, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(3000)

    Jump('loc_38BC')

    def _loc_3910(): pass

    label('loc_3910')

    Return()

# id: 0x002F offset: 0x3911
@scena.Code('func_2F_3911')
def func_2F_3911():
    ChrSetChipByIndex(0x0012, 16)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0012, 5910, -110, 2260, 7000, 0x00)
    ChrSetDirection(0x0012, 0, 0)
    ChrSetChipByIndex(0x0012, 8)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3940(): pass

    label('loc_3940')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3958',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3940')

    def _loc_3958(): pass

    label('loc_3958')

    Return()

# id: 0x0030 offset: 0x3959
@scena.Code('func_30_3959')
def func_30_3959():
    ChrSetChipByIndex(0x0011, 14)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0011, 8270, 0, -3130, 7000, 0x00)
    ChrSetDirection(0x0011, 0, 0)
    ChrSetChipByIndex(0x0011, 4)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3988(): pass

    label('loc_3988')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39DA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(500)

    Jump('loc_3988')

    def _loc_39DA(): pass

    label('loc_39DA')

    Return()

# id: 0x0031 offset: 0x39DB
@scena.Code('func_31_39DB')
def func_31_39DB():
    ChrSetChipByIndex(0x0015, 24)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x0015, 0x0080)
    ChrWalkTo(0x0015, 7490, 0, -4480, 7000, 0x00)
    ChrSetDirection(0x0015, 0, 0)
    ChrSetChipByIndex(0x0015, 28)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3A0F(): pass

    label('loc_3A0F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A2C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(500)

    Jump('loc_3A0F')

    def _loc_3A2C(): pass

    label('loc_3A2C')

    Return()

# id: 0x0032 offset: 0x3A2D
@scena.Code('func_32_3A2D')
def func_32_3A2D():
    ChrSetChipByIndex(0x0014, 22)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0014, 9300, 0, 2260, 7000, 0x00)
    ChrSetDirection(0x0014, 0, 0)
    ChrSetChipByIndex(0x0014, 27)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3A5C(): pass

    label('loc_3A5C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A74',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3A5C')

    def _loc_3A74(): pass

    label('loc_3A74')

    Return()

# id: 0x0033 offset: 0x3A75
@scena.Code('func_33_3A75')
def func_33_3A75():
    ChrSetChipByIndex(0x000A, 35)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x000A, -7710, 0, 2870, 7000, 0x00)
    ChrSetDirection(0x000A, 0, 0)
    ChrSetChipByIndex(0x000A, 31)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3AA4(): pass

    label('loc_3AA4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AF1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    PlayEffect(0x01, 0xFF, 0x00FE, 0, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3AA4')

    def _loc_3AF1(): pass

    label('loc_3AF1')

    Return()

# id: 0x0034 offset: 0x3AF2
@scena.Code('func_34_3AF2')
def func_34_3AF2():
    ChrSetChipByIndex(0x000E, 41)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x000E, -9370, 0, 2220, 7000, 0x00)
    ChrSetDirection(0x000E, 0, 0)
    ChrSetChipByIndex(0x000E, 2)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3B21(): pass

    label('loc_3B21')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B39',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3B21')

    def _loc_3B39(): pass

    label('loc_3B39')

    Return()

# id: 0x0035 offset: 0x3B3A
@scena.Code('func_35_3B3A')
def func_35_3B3A():
    ChrSetChipByIndex(0x0016, 26)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0016, -7510, 0, -1760, 7000, 0x00)
    ChrSetDirection(0x0016, 0, 0)
    ChrSetChipByIndex(0x0016, 32)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3B69(): pass

    label('loc_3B69')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BBB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    PlayEffect(0x02, 0xFF, 0x00FE, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(500)

    Jump('loc_3B69')

    def _loc_3BBB(): pass

    label('loc_3BBB')

    Return()

# id: 0x0036 offset: 0x3BBC
@scena.Code('func_36_3BBC')
def func_36_3BBC():
    ChrSetChipByIndex(0x0010, 12)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0010, -8320, 0, 1990, 7000, 0x00)
    ChrSetDirection(0x0010, 0, 0)
    ChrSetChipByIndex(0x0010, 3)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3BEB(): pass

    label('loc_3BEB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C03',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3BEB')

    def _loc_3C03(): pass

    label('loc_3C03')

    Return()

# id: 0x0037 offset: 0x3C04
@scena.Code('func_37_3C04')
def func_37_3C04():
    ChrSetChipByIndex(0x000F, 18)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x000F, -5650, -60, 3020, 7000, 0x00)
    ChrSetDirection(0x000F, 0, 0)
    ChrSetChipByIndex(0x000F, 9)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3C33(): pass

    label('loc_3C33')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C80',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    PlayEffect(0x01, 0xFF, 0x00FE, 0, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_3C33')

    def _loc_3C80(): pass

    label('loc_3C80')

    Return()

# id: 0x0038 offset: 0x3C81
@scena.Code('func_38_3C81')
def func_38_3C81():
    ChrSetChipByIndex(0x0013, 20)
    ChrSetSubChip(0x00FE, 0)
    ChrWalkTo(0x0013, 10190, 0, -3960, 7000, 0x00)
    ChrSetDirection(0x0013, 0, 0)
    ChrSetChipByIndex(0x0013, 10)
    ChrSetSubChip(0x00FE, 0)
    def _loc_3CB0(): pass

    label('loc_3CB0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D02',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    PlayEffect(0x03, 0xFF, 0x0013, 1000, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x0019, 0, 0, 0, 0)
    OP_99(0x00FE, 0x00, 0x07, 2000)
    Sleep(3000)

    Jump('loc_3CB0')

    def _loc_3D02(): pass

    label('loc_3D02')

    Return()

# id: 0x0039 offset: 0x3D03
@scena.Code('func_39_3D03')
def func_39_3D03():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3D1B',
    )

    PlaySE(506, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_3D1B(): pass

    label('loc_3D1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_3D2A',
    )

    PlaySE(505, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_3D2A(): pass

    label('loc_3D2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3D39',
    )

    PlaySE(502, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_3D39(): pass

    label('loc_3D39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3D48',
    )

    PlaySE(503, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_3D48(): pass

    label('loc_3D48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3D57',
    )

    PlaySE(508, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_3D57(): pass

    label('loc_3D57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3D66',
    )

    PlaySE(507, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_3D66(): pass

    label('loc_3D66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3D75',
    )

    PlaySE(504, 0x00, 0x64)
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_3D75(): pass

    label('loc_3D75')

    Yield()

    Jump('func_39_3D03')

    def _loc_3D79(): pass

    label('loc_3D79')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
