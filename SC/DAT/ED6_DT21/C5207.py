import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5207_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5207   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5207.x'
    header.mapIndex       = 1
    header.bgm            = 66
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
            name                = 'Dummy约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '地震控制用假人',
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

# id: 0x10002 offset: 0x108
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x108
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x108
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x108
@scena.Code('Init')
def Init():
    Event(0, func_02_124)

    Return()

# id: 0x0001 offset: 0x10D
@scena.Code('func_01_10D')
def func_01_10D():
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_6F(0x0003, 1)
    PlaySE(451, 0x01, 0x46)

    Return()

# id: 0x0002 offset: 0x124
@scena.Code('func_02_124')
def func_02_124():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT26/CH20487._CH', 'ED6_DT26/CH20487P._CP', 0)
    LoadChip('ED6_DT26/CH20270._CH', 'ED6_DT26/CH20270P._CP', 1)
    ChrSetPos(0x0101, 940, -8000, 46490, 0)
    ChrSetPos(0x0102, 940, -8000, 46490, 0)
    CameraMove(1120, -7920, 44810, 0)
    OP_67(0, 5990, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(349, 0)
    OP_C4(0x00, 0x00000002)
    OP_7E(1100, 1100, -120, 10, 1)
    CreateThread(0x000A, 0x03, 0x00, func_03_EA3)
    PlaySE(133, 0x01, 0x46)
    FadeIn(2000, 0)
    OP_0D()
    OP_72(0x0000, 0x0010)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)

    @scena.Lambda('lambda_01EC')
    def lambda_01EC():
        CameraMove(1070, -8000, 14420, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_01EC)

    @scena.Lambda('lambda_0204')
    def lambda_0204():
        ChrWalkTo(0x00FE, 380, -8000, 14120, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0204)

    Sleep(300)

    @scena.Lambda('lambda_0224')
    def lambda_0224():
        ChrWalkTo(0x00FE, 1930, -8000, 14120, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0224)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    PlaySE(136, 0x00, 0x64)
    OP_7C(1000, 0, 1000, 500)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1014F#5P#1K呀……！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0102,
        (
            '#0020421099V#1047F#6P#1K……唔……！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Sleep(100)

    Fade(500)
    TerminateThread(0x0008, 0x01)
    CameraMove(-80, -8000, 4540, 0)
    OP_67(0, 6040, -10000, 0)
    CameraSetDistance(3870, 0)
    OP_6C(315000, 0)
    OP_6E(387, 0)
    OP_0D()
    Sleep(500)

    PlaySE(599, 0x00, 0x64)
    OP_6F(0x0003, 1)
    OP_70(0x0003, 6)
    OP_73(0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421100V#1004F#6P……啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421101V#1046F#6P糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0394')
    def lambda_0394():
        ChrWalkTo(0x00FE, 380, -8000, 9160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0394)

    Sleep(60)

    @scena.Lambda('lambda_03B4')
    def lambda_03B4():
        ChrWalkTo(0x00FE, 1930, -8000, 9160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03B4)

    Sleep(200)

    PlaySE(601, 0x00, 0x64)
    Sleep(300)

    OP_6F(0x0003, 5)
    OP_70(0x0003, 400)
    Sleep(1000)

    Fade(500)
    CameraMove(520, -8000, 9150, 0)
    OP_67(0, 6580, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(315000, 0)
    OP_6E(276, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010421102V#1020F#5P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 270, 600)

    ChrTalk(
        0x0102,
        (
            '#0020421103V#1046F快回去，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_048D')
    def lambda_048D():
        CameraMove(770, -8000, 13840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_048D)

    ChrSetDirection(0x0101, 0, 600)

    @scena.Lambda('lambda_04AC')
    def lambda_04AC():
        ChrWalkTo(0x00FE, 430, -8000, 15300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04AC)

    Sleep(50)

    ChrSetDirection(0x0102, 0, 600)

    @scena.Lambda('lambda_04D3')
    def lambda_04D3():
        ChrWalkTo(0x00FE, 2120, -8000, 15300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04D3)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x02)
    PlaySE(136, 0x00, 0x64)
    OP_7C(1000, 0, 1000, 500)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(-40, -8000, 21740, 0)
    OP_67(0, 7000, -10000, 0)
    CameraSetDistance(6500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0x00000BB8)
    PlaySE(601, 0x00, 0x64)
    OP_6F(0x0003, 400)
    OP_70(0x0003, 590)
    Sleep(1000)

    OP_73(0x0003)
    Fade(500)
    CameraMove(0, -8000, 17970, 0)
    OP_67(0, 4800, -10000, 0)
    CameraSetDistance(3290, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421104V#1026F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(80)
    OP_24(0x0085, 0x3C)
    Sleep(100)

    OP_24(0x0085, 0x32)
    Sleep(400)

    @scena.Lambda('lambda_063A')
    def lambda_063A():
        CameraMove(1360, -8000, 19520, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_063A)

    @scena.Lambda('lambda_0652')
    def lambda_0652():
        OP_67(0, 6370, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0652)

    @scena.Lambda('lambda_066A')
    def lambda_066A():
        ChrMoveTo(0x00FE, 1490, -8000, 17680, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_066A)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421105V#1003F#5P好像…回不……去了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421106V#1043F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421107V#1035F大概是下面的细梁\n',
            '支撑不住这里了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421108V#1025F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421109V#1043F#6P对不起，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421110V要是我那时候\n',
            '没有拖累你的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_079C')
    def lambda_079C():
        CameraMove(790, -8000, 17650, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_079C)

    ChrSetDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010421111V#1007F#2P别说这种话啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421112V#1006F当时要不是约修亚救我，\n',
            '恐怕我都已经被落下的岩石\n',
            '砸中了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421113V#1043F#6P但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421114V#1016F#2P嘿嘿……为什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421115V在这样的状况下，\n',
            '却一点儿也不害怕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421116V#1008F约修亚呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421117V#1044F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421118V#1053F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421119V#1054F我也完全不觉得恐惧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(7350, -18890, 23200, 0)
    OP_67(0, 6770, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(315000, 0)
    OP_6E(359, 0)
    OP_0D()
    PlaySE(340, 0x00, 0x64)
    OP_6F(0x0003, 590)
    OP_70(0x0003, 600)
    OP_73(0x0003)
    Sleep(1000)

    @scena.Lambda('lambda_09A2')
    def lambda_09A2():
        CameraMove(790, -8000, 17650, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09A2)

    @scena.Lambda('lambda_09BA')
    def lambda_09BA():
        OP_67(0, 4800, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09BA)

    @scena.Lambda('lambda_09D2')
    def lambda_09D2():
        CameraSetDistance(3290, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09D2)

    @scena.Lambda('lambda_09E2')
    def lambda_09E2():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_09E2)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421120V#1013F#2P那个……约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421121V能不能拜托你两件事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421122V#1040F#6P可以啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421123V#1012F#2P第一件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421124V#1017F能不能，\n',
            '紧紧抱住我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421125V#1049F#6P非常乐意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AE1')
    def lambda_0AE1():
        CameraMove(770, -8000, 18200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AE1)

    @scena.Lambda('lambda_0AF9')
    def lambda_0AF9():
        CameraSetDistance(3100, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AF9)

    ChrWalkTo(0x0102, 1500, -8000, 17080, 1500, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0102, 0x0080)
    OP_99(0x0101, 0x00, 0x04, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010421126V#1008F#2P嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421127V#1040F#6P……还有呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x24),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x25),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421128V#1013F#2P嗯，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421129V这么说的话不知道\n',
            '会不会被你讨厌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421130V但我还是……\n',
            '不想留下遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020421131V#1035F#6P……对不起。\n',
            '还是让我先说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421132V#1041F艾丝蒂尔……\n',
            '可以吻你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010421133V#1004F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x24),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010421134V#1017F#2P……嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(133)
    Sleep(500)

    OP_99(0x0101, 0x04, 0x06, 1000)
    Sleep(500)

    @scena.Lambda('lambda_0D33')
    def lambda_0D33():
        CameraSetDistance(2900, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D33)

    OP_99(0x0101, 0x06, 0x08, 1000)
    Sleep(2000)

    @scena.Lambda('lambda_0D51')
    def lambda_0D51():
        OP_99(0x00FE, 0x08, 0x0A, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D51)

    @scena.Lambda('lambda_0D61')
    def lambda_0D61():
        OP_67(0, 10670, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D61)

    @scena.Lambda('lambda_0D79')
    def lambda_0D79():
        OP_6E(378, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D79)

    Sleep(1000)

    PlaySE(601, 0x00, 0x64)
    OP_B0(0x0003, 0x28)
    OP_6F(0x0003, 600)
    OP_70(0x0003, 1000)

    @scena.Lambda('lambda_0DA5')
    def lambda_0DA5():
        OP_67(0, 14670, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DA5)

    @scena.Lambda('lambda_0DBD')
    def lambda_0DBD():
        CameraMove(770, -20000, 18200, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DBD)

    @scena.Lambda('lambda_0DD5')
    def lambda_0DD5():
        CameraSetDistance(1000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DD5)

    OP_C4(0x01, 0x00000002)
    ChrClearFlags(0x0101, 0x0001)
    OP_99(0x0101, 0x0A, 0x0C, 1200)
    CreateThread(0x0102, 0x03, 0x00, func_04_EC6)
    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_24(0x0085, 0x28)
    Sleep(200)

    OP_24(0x0085, 0x1E)
    Sleep(200)

    OP_24(0x0085, 0x14)
    Sleep(200)

    OP_24(0x0085, 0x0A)
    Sleep(200)

    OP_23(0x0085)
    MapClearFlags(0x00100000)
    OP_C4(0x00, 0x00000010)
    Yield()
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT46.dat', 0x0000, 0x0001)
    def _loc_E59(): pass

    label('loc_E59')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E73',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_E70',
    )

    Jump('loc_E73')

    def _loc_E70(): pass

    label('loc_E70')

    Jump('loc_E59')

    def _loc_E73(): pass

    label('loc_E73')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(500)

    OP_C4(0x01, 0x00000010)
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0110._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0xEA3
@scena.Code('func_03_EA3')
def func_03_EA3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EC5',
    )

    OP_7C(30, 30, 1000, 900)
    Sleep(1000)

    Jump('func_03_EA3')

    def _loc_EC5(): pass

    label('loc_EC5')

    Return()

# id: 0x0004 offset: 0xEC6
@scena.Code('func_04_EC6')
def func_04_EC6():
    ChrSetPos(0x0101, 1500, -8500, 17200, 0)
    ChrSetFlags(0x0101, 0x0020)

    @scena.Lambda('lambda_0EE2')
    def lambda_0EE2():
        ChrMoveToRelativeAsync(0x00FE, 0, -50000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EE2)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0xD),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(300)

    @scena.Lambda('lambda_0F0D')
    def lambda_0F0D():
        OP_99(0x0101, 0x0E, 0x1D, 1500)
        Yield()

        Jump('lambda_0F0D')

    DispatchAsync2(0x0102, 0x0002, lambda_0F0D)

    Return()

# id: 0x0005 offset: 0xF1B
@scena.Code('func_05_F1B')
def func_05_F1B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F67',
    )

    ExecExpressionWithValue(
        0x0008,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x102, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x102, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x102, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_05_F1B')

    def _loc_F67(): pass

    label('loc_F67')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
