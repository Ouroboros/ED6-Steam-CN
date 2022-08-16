import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2103.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT06/CH20083._CH', 'ED6_DT06/CH20083P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
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
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_1B9)

    Return()

# id: 0x0001 offset: 0x1B3
@scena.Code('func_01_1B3')
def func_01_1B3():
    PlaySE(452, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1B9
@scena.Code('func_02_1B9')
def func_02_1B9():
    EventBegin(0x00)
    PlaySE(218, 0x01, 0x64)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x04, 0x000A, 0, 50, 2700, 180, 0, 0, 2500, 500, 10000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x0009, 0, 50, 2400, 180, 0, 0, 1600, 500, 10000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0xFF, 0x000A, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0xFF, 0x0009, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CameraMove(27900, -2990, 4040, 0)
    OP_67(0, 5630, -10000, 0)
    CameraSetDistance(1410, 0)
    OP_6C(270000, 0)
    OP_6E(713, 0)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetFlags(0x0105, 0x0020)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0102, 3)
    ChrSetChipByIndex(0x0105, 4)
    OP_89(0x0101, 6290, -2000, -10, 270)
    OP_89(0x0102, 8650, -2000, -420, 270)
    OP_89(0x0105, 7180, -2000, 320, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetBattleFlags(0x0008, 0x0020)
    OP_89(0x0008, -180, -2000, 370, 270)
    OP_72(0x0000, 0x0002)
    OP_71(0x0000, 0x0020)
    OP_71(0x0000, 0x0040)
    OP_6F(0x0000, 301)
    OP_70(0x0000, 360)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0020)
    OP_71(0x0001, 0x0040)
    OP_6F(0x0001, 301)
    OP_70(0x0001, 360)
    OP_A1(0x000A, 0x0000)
    OP_A1(0x0009, 0x0001)
    ChrSetPos(0x000A, 0, -2950, 0, 90)
    ChrSetPos(0x0009, 27900, -2990, 4040, 90)

    @scena.Lambda('lambda_03D6')
    def lambda_03D6():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_03D6)

    @scena.Lambda('lambda_03F1')
    def lambda_03F1():
        CameraMove(6770, -2990, 360, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03F1)

    @scena.Lambda('lambda_0409')
    def lambda_0409():
        OP_6C(225000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0409)

    Sleep(4600)

    @scena.Lambda('lambda_041E')
    def lambda_041E():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_041E)

    Sleep(200)

    @scena.Lambda('lambda_043E')
    def lambda_043E():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_043E)

    Sleep(180)

    @scena.Lambda('lambda_045E')
    def lambda_045E():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_045E)

    Sleep(160)

    @scena.Lambda('lambda_047E')
    def lambda_047E():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 1400, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_047E)

    Sleep(140)

    @scena.Lambda('lambda_049E')
    def lambda_049E():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_049E)

    Sleep(120)

    @scena.Lambda('lambda_04BE')
    def lambda_04BE():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_04BE)

    Sleep(100)

    @scena.Lambda('lambda_04DE')
    def lambda_04DE():
        ChrMoveTo(0x00FE, 12030, -2990, 960, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_04DE)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010061746V#508F好～了，终于追上了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061747V#040F因为我们坐的是小型艇，\n',
            '船体比较轻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0563')
    def lambda_0563():
        ChrSetDirection(0x0008, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0563)

    @scena.Lambda('lambda_0571')
    def lambda_0571():
        CameraMove(6770, -2990, 290, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0571)

    @scena.Lambda('lambda_0589')
    def lambda_0589():
        OP_6C(122000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0589)

    Sleep(1000)

    ChrSetChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_05A3')
    def lambda_05A3():
        ChrWalkTo(0x0008, 1610, -2830, 180, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05A3)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0490061748V#666F呜……\n',
            '真是缠人的家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061749V#665F尝尝这个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x02, 'map\\\\mp008_00.eff')
    ChrSetChipByIndex(0x0101, 65535)
    Sleep(100)

    ChrSetChipByIndex(0x0101, 6)
    Sleep(100)

    ChrSetChipByIndex(0x0101, 5)
    PlaySE(126, 0x01, 0x64)

    @scena.Lambda('lambda_0642')
    def lambda_0642():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_0642')

    DispatchAsync2(0x0101, 0x0000, lambda_0642)

    ChrSetPos(0x000D, 9550, -1900, 1300, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)

    @scena.Lambda('lambda_069B')
    def lambda_069B():
        CameraMove(10040, -2600, 1040, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_069B)

    @scena.Lambda('lambda_06B3')
    def lambda_06B3():
        OP_6C(102000, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06B3)

    Sleep(250)

    ChrSetPos(0x000D, 9550, -1300, 1000, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(250)

    Sleep(300)

    ChrSetPos(0x000D, 9550, -1500, 1600, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(200)

    ChrSetPos(0x000D, 9550, -1900, 1300, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(300)

    @scena.Lambda('lambda_07AE')
    def lambda_07AE():
        OP_6C(225000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07AE)

    ChrSetPos(0x000D, 9550, -1300, 1000, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010061750V#005F#20A#3S喝啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(300)

    ChrSetPos(0x000D, 9550, -1500, 1600, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(700)

    @scena.Lambda('lambda_0889')
    def lambda_0889():
        CameraMove(6660, -2990, 520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0889)

    TerminateThread(0x0101, 0x00)
    OP_23(0x007E)
    OP_99(0x0101, 0x00, 0x13, 3000)
    Sleep(500)

    OP_99(0x0101, 0x13, 0x08, 3000)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 6)

    ChrTalk(
        0x0008,
        (
            '#0490061751V#668F什、什么！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061752V#502F嘿嘿～\n',
            '市长你太小看游击士了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061753V#005F约修亚，\n',
            '就这样从右边靠上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0956')
    def lambda_0956():
        OP_94(0x01, 0x000A, 0x00B4, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0956)

    ChrTalk(
        0x0102,
        (
            '#0020061754V#012F明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061755V#014F……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09A4')
    def lambda_09A4():
        CameraMove(4890, -2990, 200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09A4)

    PlaySE(150, 0x00, 0x64)

    @scena.Lambda('lambda_09C1')
    def lambda_09C1():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09C1)

    Sleep(250)

    @scena.Lambda('lambda_09DC')
    def lambda_09DC():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09DC)

    Sleep(250)

    OP_B0(0x0000, 0x64)

    @scena.Lambda('lambda_09FB')
    def lambda_09FB():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09FB)

    @scena.Lambda('lambda_0A11')
    def lambda_0A11():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A11)

    Sleep(200)

    @scena.Lambda('lambda_0A2C')
    def lambda_0A2C():
        OP_94(0x01, 0x0009, 0x00B4, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A2C)

    @scena.Lambda('lambda_0A42')
    def lambda_0A42():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A42)

    Sleep(300)

    @scena.Lambda('lambda_0A5D')
    def lambda_0A5D():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A5D)

    Sleep(200)

    @scena.Lambda('lambda_0A78')
    def lambda_0A78():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A78)

    Sleep(200)

    @scena.Lambda('lambda_0A93')
    def lambda_0A93():
        OP_94(0x01, 0x000A, 0x00B4, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A93)

    ChrTalk(
        0x0101,
        (
            '#0010061756V#580F怎、怎么忽然变快了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061757V#042F这是……\n',
            '从海岸吹来的海风！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061758V#012F糟了，\n',
            '这下帆船就大占优势了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061759V#005F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0490061760V#667F哇哈哈！！\n',
            '看来女神也向我这边微笑了啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061761V那么再见了，小丫头们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BCE')
    def lambda_0BCE():
        ChrSetDirection(0x0008, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BCE)

    OP_B0(0x0000, 0x1E)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 240)
    OP_70(0x0000, 300)

    @scena.Lambda('lambda_0BF3')
    def lambda_0BF3():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BF3)

    Sleep(200)

    @scena.Lambda('lambda_0C0E')
    def lambda_0C0E():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C0E)

    Sleep(300)

    @scena.Lambda('lambda_0C29')
    def lambda_0C29():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C29)

    Sleep(300)

    @scena.Lambda('lambda_0C44')
    def lambda_0C44():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C44)

    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 301)
    OP_70(0x0000, 360)

    @scena.Lambda('lambda_0C70')
    def lambda_0C70():
        OP_94(0x01, 0x000A, 0x00B4, 0x00004E20, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C70)

    Sleep(300)

    @scena.Lambda('lambda_0C8B')
    def lambda_0C8B():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C8B)

    Sleep(300)

    @scena.Lambda('lambda_0CA6')
    def lambda_0CA6():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CA6)

    Sleep(300)

    @scena.Lambda('lambda_0CC1')
    def lambda_0CC1():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002EE0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CC1)

    Sleep(300)

    @scena.Lambda('lambda_0CDC')
    def lambda_0CDC():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x000032C8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CDC)

    Sleep(300)

    @scena.Lambda('lambda_0CF7')
    def lambda_0CF7():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x000036B0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CF7)

    ChrTalk(
        0x0101,
        (
            '#0010061762V#005F开什么玩笑！\n',
            '就只差那么一步了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061763V#013F这样下去恐怕只能\n',
            '眼睁睁地看他远走高飞了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061764V要是还有什么办法的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0DC9')
    def lambda_0DC9():
        CameraMove(11720, -2900, 1060, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DC9)

    ChrSetPos(0x000B, 60000, 2950, 2000, 270)
    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x000B, 800)
    Sleep(500)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x000B, 800)
    ChrSetChipByIndex(0x0105, 65535)
    ChrTurnDirection(0x0105, 0x000B, 800)

    ChrTalk(
        0x0101,
        (
            '#0010061765V#580F什、什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061766V#047F#1S……来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E64')
    def lambda_0E64():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E64')

    DispatchAsync2(0x0101, 0x0001, lambda_0E64)

    @scena.Lambda('lambda_0E75')
    def lambda_0E75():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E75')

    DispatchAsync2(0x0102, 0x0001, lambda_0E75)

    @scena.Lambda('lambda_0E86')
    def lambda_0E86():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E86')

    DispatchAsync2(0x0105, 0x0001, lambda_0E86)

    OP_72(0x0002, 0x0004)
    OP_A1(0x000B, 0x0002)
    ChrSetPos(0x000B, 60000, 2950, 2000, 270)
    PlaySE(219, 0x00, 0x64)

    @scena.Lambda('lambda_0EB7')
    def lambda_0EB7():
        OP_94(0x01, 0x000B, 0x0000, 0x000186A0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0EB7)

    @scena.Lambda('lambda_0ECD')
    def lambda_0ECD():
        CameraSetDistance(2300, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0ECD)

    Sleep(3000)

    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    OP_24(0x00DA, 0x5F)
    Sleep(200)

    OP_24(0x00DA, 0x5A)
    Sleep(200)

    OP_24(0x00DA, 0x55)
    Sleep(200)

    OP_24(0x00DA, 0x50)
    Sleep(200)

    OP_24(0x00DA, 0x4B)
    Sleep(200)

    OP_24(0x00DA, 0x46)
    Sleep(200)

    OP_24(0x00DA, 0x41)
    Sleep(200)

    OP_23(0x00DA)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    FadeIn(1000, 0)
    CameraMove(-33030, -2950, 110, 0)
    OP_67(0, 7310, -10000, 0)
    CameraSetDistance(2280, 0)
    OP_6C(315000, 0)
    OP_6E(710, 0)
    StopEffect(0x03, 0x00)
    TerminateThread(0x000A, 0xFF)
    ChrSetPos(0x000A, -33030, -2950, 110, 90)
    TerminateThread(0x000B, 0xFF)
    ChrSetPos(0x000B, 34720, 0, 18480, 270)
    ChrSetPos(0x000C, 34720, 30000, 18480, 270)
    PlaySE(218, 0x01, 0x64)
    OP_24(0x00DA, 0x41)
    Sleep(100)

    OP_24(0x00DA, 0x46)
    Sleep(100)

    OP_24(0x00DA, 0x4B)
    Sleep(100)

    OP_24(0x00DA, 0x50)
    Sleep(100)

    OP_24(0x00DA, 0x55)
    Sleep(100)

    OP_24(0x00DA, 0x5A)
    Sleep(100)

    OP_24(0x00DA, 0x5F)
    Sleep(100)

    OP_24(0x00DA, 0x64)
    OP_0D()
    OP_B0(0x0003, 0x1E)
    OP_72(0x0003, 0x0004)
    OP_A1(0x000C, 0x0003)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 900)
    OP_70(0x0003, 1300)
    OP_B0(0x0003, 0x3C)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0040)

    ChrTalk(
        0x0008,
        (
            '#0490061767V#664F呀，总算逃出来了。\n',
            '不过从今往后该怎么办呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061768V果然，唯有在军队插手之前，\n',
            '尽早逃到帝国去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490061769V#667F算了，只要稍微忍耐一阵，\n',
            '『他』肯定会帮我想办法的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000B, 400)
    PlaySE(121, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(101)

    @scena.Lambda('lambda_1137')
    def lambda_1137():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1137')

    DispatchAsync2(0x0008, 0x0001, lambda_1137)

    ChrSetPos(0x000B, 28720, 0, 18000, 270)
    ChrSetPos(0x000C, 34720, 15000, 18000, 270)
    ChrSetPos(0x0009, 300000, 300000, 300000, 0)

    @scena.Lambda('lambda_117B')
    def lambda_117B():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_117B)

    @scena.Lambda('lambda_1196')
    def lambda_1196():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1196)

    @scena.Lambda('lambda_11B1')
    def lambda_11B1():
        CameraMove(-31420, -2990, 9180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11B1)

    @scena.Lambda('lambda_11C9')
    def lambda_11C9():
        OP_67(0, 11900, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11C9)

    @scena.Lambda('lambda_11E1')
    def lambda_11E1():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11E1)

    @scena.Lambda('lambda_11F1')
    def lambda_11F1():
        CameraSetDistance(3210, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11F1)

    Sleep(2200)

    @scena.Lambda('lambda_1206')
    def lambda_1206():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1206)

    @scena.Lambda('lambda_1221')
    def lambda_1221():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1221)

    Sleep(300)

    @scena.Lambda('lambda_1241')
    def lambda_1241():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1241)

    @scena.Lambda('lambda_125C')
    def lambda_125C():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_125C)

    Sleep(300)

    @scena.Lambda('lambda_127C')
    def lambda_127C():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_127C)

    @scena.Lambda('lambda_1297')
    def lambda_1297():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1297)

    Sleep(300)

    @scena.Lambda('lambda_12B7')
    def lambda_12B7():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12B7)

    @scena.Lambda('lambda_12D2')
    def lambda_12D2():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12D2)

    Sleep(300)

    @scena.Lambda('lambda_12F2')
    def lambda_12F2():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12F2)

    @scena.Lambda('lambda_130D')
    def lambda_130D():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_130D)

    Sleep(300)

    @scena.Lambda('lambda_132D')
    def lambda_132D():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_132D)

    @scena.Lambda('lambda_1348')
    def lambda_1348():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1348)

    Sleep(300)

    @scena.Lambda('lambda_1368')
    def lambda_1368():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1368)

    @scena.Lambda('lambda_1383')
    def lambda_1383():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1383)

    Sleep(300)

    @scena.Lambda('lambda_13A3')
    def lambda_13A3():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13A3)

    @scena.Lambda('lambda_13BE')
    def lambda_13BE():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13BE)

    Sleep(300)

    @scena.Lambda('lambda_13DE')
    def lambda_13DE():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13DE)

    @scena.Lambda('lambda_13F9')
    def lambda_13F9():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13F9)

    Sleep(300)

    @scena.Lambda('lambda_1419')
    def lambda_1419():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1419)

    @scena.Lambda('lambda_1434')
    def lambda_1434():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1434)

    Sleep(300)

    @scena.Lambda('lambda_1454')
    def lambda_1454():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1454)

    @scena.Lambda('lambda_146F')
    def lambda_146F():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_146F)

    Sleep(300)

    @scena.Lambda('lambda_148F')
    def lambda_148F():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_148F)

    @scena.Lambda('lambda_14AA')
    def lambda_14AA():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14AA)

    ChrTalk(
        0x0008,
        (
            '#0490061770V#668F#3S什、什、什么————！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1508')
    def lambda_1508():
        CameraMove(-39220, -2900, 9180, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1508)

    @scena.Lambda('lambda_1520')
    def lambda_1520():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1520)

    @scena.Lambda('lambda_153B')
    def lambda_153B():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_153B)

    Sleep(300)

    @scena.Lambda('lambda_155B')
    def lambda_155B():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_155B)

    @scena.Lambda('lambda_1576')
    def lambda_1576():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1576)

    OP_72(0x0003, 0x0020)
    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1300)
    OP_70(0x0003, 1540)
    Sleep(300)

    @scena.Lambda('lambda_15AD')
    def lambda_15AD():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_15AD)

    @scena.Lambda('lambda_15C8')
    def lambda_15C8():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_15C8)

    Sleep(300)

    @scena.Lambda('lambda_15E8')
    def lambda_15E8():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_15E8)

    @scena.Lambda('lambda_1603')
    def lambda_1603():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1603)

    Sleep(300)

    @scena.Lambda('lambda_1623')
    def lambda_1623():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1623)

    @scena.Lambda('lambda_163E')
    def lambda_163E():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_163E)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_165E')
    def lambda_165E():
        OP_67(0, 7250, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_165E)

    @scena.Lambda('lambda_1676')
    def lambda_1676():
        CameraMove(-35670, 4660, 3490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1676)

    @scena.Lambda('lambda_168E')
    def lambda_168E():
        OP_6C(179000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_168E)

    @scena.Lambda('lambda_169E')
    def lambda_169E():
        ChrSetDirection(0x00FE, 180, 2)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_169E)

    @scena.Lambda('lambda_16AC')
    def lambda_16AC():
        ChrSetDirection(0x00FE, 180, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_16AC)

    @scena.Lambda('lambda_16BA')
    def lambda_16BA():
        OP_97(0x000B, -35520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_16BA)

    @scena.Lambda('lambda_16D6')
    def lambda_16D6():
        OP_97(0x000C, -33520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_16D6)

    @scena.Lambda('lambda_16F2')
    def lambda_16F2():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16F2)

    Sleep(150)

    @scena.Lambda('lambda_170D')
    def lambda_170D():
        ChrSetDirection(0x00FE, 180, 7)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_170D)

    @scena.Lambda('lambda_171B')
    def lambda_171B():
        ChrSetDirection(0x00FE, 180, 7)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_171B)

    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1540)
    OP_70(0x0003, 1600)
    Sleep(150)

    @scena.Lambda('lambda_1740')
    def lambda_1740():
        ChrSetDirection(0x00FE, 180, 11)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1740)

    @scena.Lambda('lambda_174E')
    def lambda_174E():
        ChrSetDirection(0x00FE, 180, 11)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_174E)

    @scena.Lambda('lambda_175C')
    def lambda_175C():
        OP_97(0x000B, -35520, 0, -90000, 7000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_175C)

    @scena.Lambda('lambda_1778')
    def lambda_1778():
        OP_97(0x000C, -33520, 0, -90000, 7000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1778)

    @scena.Lambda('lambda_1794')
    def lambda_1794():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1794)

    Sleep(200)

    @scena.Lambda('lambda_17AF')
    def lambda_17AF():
        ChrSetDirection(0x00FE, 180, 16)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17AF)

    @scena.Lambda('lambda_17BD')
    def lambda_17BD():
        ChrSetDirection(0x00FE, 180, 16)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_17BD)

    Sleep(200)

    @scena.Lambda('lambda_17D0')
    def lambda_17D0():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17D0)

    @scena.Lambda('lambda_17DE')
    def lambda_17DE():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_17DE)

    @scena.Lambda('lambda_17EC')
    def lambda_17EC():
        OP_97(0x000B, -35520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17EC)

    @scena.Lambda('lambda_1808')
    def lambda_1808():
        OP_97(0x000C, -33520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1808)

    @scena.Lambda('lambda_1824')
    def lambda_1824():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1824)

    Sleep(400)

    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 1595)
    OP_70(0x0003, 1600)

    @scena.Lambda('lambda_1852')
    def lambda_1852():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1852)

    @scena.Lambda('lambda_1860')
    def lambda_1860():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1860)

    @scena.Lambda('lambda_186E')
    def lambda_186E():
        OP_97(0x000B, -35520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_186E)

    @scena.Lambda('lambda_188A')
    def lambda_188A():
        OP_97(0x000C, -33520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_188A)

    @scena.Lambda('lambda_18A6')
    def lambda_18A6():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_18A6)

    Sleep(400)

    @scena.Lambda('lambda_18C1')
    def lambda_18C1():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_18C1)

    @scena.Lambda('lambda_18CF')
    def lambda_18CF():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_18CF)

    @scena.Lambda('lambda_18DD')
    def lambda_18DD():
        OP_97(0x000B, -35520, 0, -90000, 10000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_18DD)

    @scena.Lambda('lambda_18F9')
    def lambda_18F9():
        OP_97(0x000C, -33520, 0, -90000, 10000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_18F9)

    @scena.Lambda('lambda_1915')
    def lambda_1915():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1915)

    Sleep(400)

    @scena.Lambda('lambda_1930')
    def lambda_1930():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1930)

    @scena.Lambda('lambda_193E')
    def lambda_193E():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_193E)

    @scena.Lambda('lambda_194C')
    def lambda_194C():
        OP_97(0x000B, -35520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_194C)

    @scena.Lambda('lambda_1968')
    def lambda_1968():
        OP_97(0x000C, -33520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1968)

    @scena.Lambda('lambda_1984')
    def lambda_1984():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1984)

    Sleep(400)

    @scena.Lambda('lambda_199F')
    def lambda_199F():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_199F)

    @scena.Lambda('lambda_19AD')
    def lambda_19AD():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_19AD)

    @scena.Lambda('lambda_19BB')
    def lambda_19BB():
        OP_97(0x000B, -35520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_19BB)

    @scena.Lambda('lambda_19D7')
    def lambda_19D7():
        OP_97(0x000C, -33520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_19D7)

    @scena.Lambda('lambda_19F3')
    def lambda_19F3():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_19F3)

    Sleep(400)

    @scena.Lambda('lambda_1A0E')
    def lambda_1A0E():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1A0E)

    @scena.Lambda('lambda_1A1C')
    def lambda_1A1C():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1A1C)

    @scena.Lambda('lambda_1A2A')
    def lambda_1A2A():
        OP_97(0x000B, -35520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A2A)

    @scena.Lambda('lambda_1A46')
    def lambda_1A46():
        OP_97(0x000C, -33520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1A46)

    @scena.Lambda('lambda_1A62')
    def lambda_1A62():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1A62)

    Sleep(300)

    @scena.Lambda('lambda_1A7D')
    def lambda_1A7D():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1A7D)

    @scena.Lambda('lambda_1A8B')
    def lambda_1A8B():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1A8B)

    @scena.Lambda('lambda_1A99')
    def lambda_1A99():
        OP_97(0x000B, -35520, 0, -90000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A99)

    @scena.Lambda('lambda_1AB5')
    def lambda_1AB5():
        OP_97(0x000C, -33520, 0, -90000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1AB5)

    @scena.Lambda('lambda_1AD1')
    def lambda_1AD1():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1AD1)

    Sleep(200)

    @scena.Lambda('lambda_1AEC')
    def lambda_1AEC():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1AEC)

    @scena.Lambda('lambda_1AFA')
    def lambda_1AFA():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1AFA)

    @scena.Lambda('lambda_1B08')
    def lambda_1B08():
        OP_97(0x000B, -35520, 0, -90000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B08)

    @scena.Lambda('lambda_1B24')
    def lambda_1B24():
        OP_97(0x000C, -33520, 0, -90000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B24)

    @scena.Lambda('lambda_1B40')
    def lambda_1B40():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B40)

    Sleep(100)

    @scena.Lambda('lambda_1B5B')
    def lambda_1B5B():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1B5B)

    @scena.Lambda('lambda_1B69')
    def lambda_1B69():
        ChrSetDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1B69)

    @scena.Lambda('lambda_1B77')
    def lambda_1B77():
        OP_97(0x000B, -35520, 0, -90000, 3000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B77)

    @scena.Lambda('lambda_1B93')
    def lambda_1B93():
        OP_97(0x000C, -33520, 0, -90000, 3000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B93)

    @scena.Lambda('lambda_1BAF')
    def lambda_1BAF():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1BAF)

    Sleep(100)

    @scena.Lambda('lambda_1BCA')
    def lambda_1BCA():
        OP_97(0x000B, -35520, 0, -90000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1BCA)

    @scena.Lambda('lambda_1BE6')
    def lambda_1BE6():
        OP_97(0x000C, -33520, 0, -90000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1BE6)

    @scena.Lambda('lambda_1C02')
    def lambda_1C02():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C02)

    Sleep(100)

    @scena.Lambda('lambda_1C1D')
    def lambda_1C1D():
        OP_97(0x000B, -35520, 0, -90000, 1000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C1D)

    @scena.Lambda('lambda_1C39')
    def lambda_1C39():
        OP_97(0x000C, -33520, 0, -90000, 1000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C39)

    Sleep(200)

    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 1600)
    OP_70(0x0003, 1670)

    ChrTalk(
        0x0008,
        (
            '#0490061771V#668F#10A#5P什、什、什……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_1CA5')
    def lambda_1CA5():
        CameraMove(46000, -2990, -4059, 8100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CA5)

    @scena.Lambda('lambda_1CBD')
    def lambda_1CBD():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 300, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1CBD)

    @scena.Lambda('lambda_1CD8')
    def lambda_1CD8():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1CD8)

    @scena.Lambda('lambda_1CF3')
    def lambda_1CF3():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1CF3)

    Sleep(200)

    @scena.Lambda('lambda_1D13')
    def lambda_1D13():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1D13)

    @scena.Lambda('lambda_1D2E')
    def lambda_1D2E():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1D2E)

    @scena.Lambda('lambda_1D49')
    def lambda_1D49():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1D49)

    Sleep(200)

    @scena.Lambda('lambda_1D69')
    def lambda_1D69():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1D69)

    @scena.Lambda('lambda_1D84')
    def lambda_1D84():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1D84)

    @scena.Lambda('lambda_1D9F')
    def lambda_1D9F():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1D9F)

    Sleep(200)

    @scena.Lambda('lambda_1DBF')
    def lambda_1DBF():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1DBF)

    @scena.Lambda('lambda_1DDA')
    def lambda_1DDA():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1DDA)

    @scena.Lambda('lambda_1DF5')
    def lambda_1DF5():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1DF5)

    Sleep(200)

    @scena.Lambda('lambda_1E15')
    def lambda_1E15():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1E15)

    @scena.Lambda('lambda_1E30')
    def lambda_1E30():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1E30)

    @scena.Lambda('lambda_1E4B')
    def lambda_1E4B():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1E4B)

    Sleep(200)

    @scena.Lambda('lambda_1E6B')
    def lambda_1E6B():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1E6B)

    @scena.Lambda('lambda_1E86')
    def lambda_1E86():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1E86)

    @scena.Lambda('lambda_1EA1')
    def lambda_1EA1():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1EA1)

    Sleep(200)

    @scena.Lambda('lambda_1EC1')
    def lambda_1EC1():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 3733, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1EC1)

    @scena.Lambda('lambda_1EDC')
    def lambda_1EDC():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1EDC)

    @scena.Lambda('lambda_1EF7')
    def lambda_1EF7():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1EF7)

    Sleep(200)

    @scena.Lambda('lambda_1F17')
    def lambda_1F17():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1F17)

    @scena.Lambda('lambda_1F32')
    def lambda_1F32():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1F32)

    @scena.Lambda('lambda_1F4D')
    def lambda_1F4D():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1F4D)

    Sleep(200)

    @scena.Lambda('lambda_1F6D')
    def lambda_1F6D():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1F6D)

    @scena.Lambda('lambda_1F88')
    def lambda_1F88():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1F88)

    Sleep(200)

    @scena.Lambda('lambda_1FA8')
    def lambda_1FA8():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1FA8)

    @scena.Lambda('lambda_1FC3')
    def lambda_1FC3():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1FC3)

    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1670)
    OP_70(0x0003, 1800)

    @scena.Lambda('lambda_1FF0')
    def lambda_1FF0():
        ChrSetDirection(0x00FE, 180, 33)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1FF0)

    StopEffect(0x04, 0x02)
    PlayEffect(0x04, 0x05, 0x000A, 0, 0, 2300, 180, 0, 0, 2000, 100, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0490061772V#668F#10A#5P呜哇啊啊啊啊！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_B0(0x0000, 0xC8)
    OP_23(0x00DA)
    OP_23(0x00DC)
    PlaySE(220, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mpsibuk.eff')
    PlayEffect(0x00, 0xFF, 0x000C, 3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, 5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x000C, -5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 300, 5000, 2000)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    Sleep(500)

    @scena.Lambda('lambda_260D')
    def lambda_260D():
        ChrMoveToRelativeAsync(0x00FE, 300000, -30000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_260D)

    @scena.Lambda('lambda_2628')
    def lambda_2628():
        ChrMoveToRelativeAsync(0x00FE, 300000, -30000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_2628)

    @scena.Lambda('lambda_2643')
    def lambda_2643():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 19500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2643)

    Sleep(150)

    @scena.Lambda('lambda_2663')
    def lambda_2663():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 19000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2663)

    Sleep(150)

    @scena.Lambda('lambda_2683')
    def lambda_2683():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2683)

    Sleep(150)

    @scena.Lambda('lambda_26A3')
    def lambda_26A3():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 17000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_26A3)

    Sleep(150)

    @scena.Lambda('lambda_26C3')
    def lambda_26C3():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_26C3)

    Sleep(150)

    @scena.Lambda('lambda_26E3')
    def lambda_26E3():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_26E3)

    Sleep(150)

    @scena.Lambda('lambda_2703')
    def lambda_2703():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2703)

    Sleep(900)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2104._SN', 0, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
