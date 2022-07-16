import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2103   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '戴尔蒙市长'),
    TXT(0x02, ' '),
    TXT(0x03, ' '),
    TXT(0x04, ' '),
    TXT(0x05, ' '),
    TXT(0x06, ' '),
    TXT(0x07, ''),
]

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

# id: 0xFFFF offset: 0x26B4
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
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

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1A2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    Return()

# id: 0x0001 offset: 0x1B3
@scena.Code('Init')
def Init():
    PlaySE(452, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1B9
@scena.Code('ReInit')
def ReInit():
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
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0102, 0x0020)
    SetChrFlags(0x0105, 0x0020)
    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0102, 3)
    SetChrChipByIndex(0x0105, 4)
    OP_89(0x0101, 6290, -2000, -10, 270)
    OP_89(0x0102, 8650, -2000, -420, 270)
    OP_89(0x0105, 7180, -2000, 320, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0004)
    SetChrBattleFlags(0x0008, 0x0020)
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
    SetChrPos(0x000A, 0, -2950, 0, 90)
    SetChrPos(0x0009, 27900, -2990, 4040, 90)

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

    @scena.Lambda('lambda_0559')
    def lambda_0559():
        SetChrDirection(0x0008, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0559)

    @scena.Lambda('lambda_0567')
    def lambda_0567():
        CameraMove(6770, -2990, 290, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0567)

    @scena.Lambda('lambda_057F')
    def lambda_057F():
        OP_6C(122000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_057F)

    Sleep(1000)

    SetChrChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_0599')
    def lambda_0599():
        ChrWalkTo(0x0008, 1610, -2830, 180, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0599)

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
    SetChrChipByIndex(0x0101, 65535)
    Sleep(100)

    SetChrChipByIndex(0x0101, 6)
    Sleep(100)

    SetChrChipByIndex(0x0101, 5)
    PlaySE(126, 0x01, 0x64)

    @scena.Lambda('lambda_062E')
    def lambda_062E():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_062E')

    DispatchAsync2(0x0101, 0x0000, lambda_062E)

    SetChrPos(0x000D, 9550, -1900, 1300, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)

    @scena.Lambda('lambda_0687')
    def lambda_0687():
        CameraMove(10040, -2600, 1040, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0687)

    @scena.Lambda('lambda_069F')
    def lambda_069F():
        OP_6C(102000, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_069F)

    Sleep(250)

    SetChrPos(0x000D, 9550, -1300, 1000, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(250)

    Sleep(300)

    SetChrPos(0x000D, 9550, -1500, 1600, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(200)

    SetChrPos(0x000D, 9550, -1900, 1300, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(300)

    @scena.Lambda('lambda_079A')
    def lambda_079A():
        OP_6C(225000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_079A)

    SetChrPos(0x000D, 9550, -1300, 1000, 0)
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

    SetChrPos(0x000D, 9550, -1500, 1600, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000D, 0, 0, 0, 0)
    Sleep(700)

    @scena.Lambda('lambda_0870')
    def lambda_0870():
        CameraMove(6660, -2990, 520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0870)

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

    SetChrChipByIndex(0x0101, 6)

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

    @scena.Lambda('lambda_092E')
    def lambda_092E():
        OP_94(0x01, 0x000A, 0x00B4, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_092E)

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

    @scena.Lambda('lambda_0972')
    def lambda_0972():
        CameraMove(4890, -2990, 200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0972)

    PlaySE(150, 0x00, 0x64)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_098F)

    Sleep(250)

    @scena.Lambda('lambda_09AA')
    def lambda_09AA():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09AA)

    Sleep(250)

    OP_B0(0x0000, 0x64)

    @scena.Lambda('lambda_09C9')
    def lambda_09C9():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09C9)

    @scena.Lambda('lambda_09DF')
    def lambda_09DF():
        OP_94(0x01, 0x0009, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09DF)

    Sleep(200)

    @scena.Lambda('lambda_09FA')
    def lambda_09FA():
        OP_94(0x01, 0x0009, 0x00B4, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09FA)

    @scena.Lambda('lambda_0A10')
    def lambda_0A10():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A10)

    Sleep(300)

    @scena.Lambda('lambda_0A2B')
    def lambda_0A2B():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A2B)

    Sleep(200)

    @scena.Lambda('lambda_0A46')
    def lambda_0A46():
        OP_94(0x01, 0x000A, 0x00B4, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A46)

    Sleep(200)

    @scena.Lambda('lambda_0A61')
    def lambda_0A61():
        OP_94(0x01, 0x000A, 0x00B4, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A61)

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
    SetChrChipByIndex(0x0008, 0)

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

    @scena.Lambda('lambda_0B7E')
    def lambda_0B7E():
        SetChrDirection(0x0008, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B7E)

    OP_B0(0x0000, 0x1E)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 240)
    OP_70(0x0000, 300)

    @scena.Lambda('lambda_0BA3')
    def lambda_0BA3():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BA3)

    Sleep(200)

    @scena.Lambda('lambda_0BBE')
    def lambda_0BBE():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BBE)

    Sleep(300)

    @scena.Lambda('lambda_0BD9')
    def lambda_0BD9():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BD9)

    Sleep(300)

    @scena.Lambda('lambda_0BF4')
    def lambda_0BF4():
        OP_94(0x01, 0x000A, 0x00B4, 0x00007530, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BF4)

    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 301)
    OP_70(0x0000, 360)

    @scena.Lambda('lambda_0C20')
    def lambda_0C20():
        OP_94(0x01, 0x000A, 0x00B4, 0x00004E20, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C20)

    Sleep(300)

    @scena.Lambda('lambda_0C3B')
    def lambda_0C3B():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C3B)

    Sleep(300)

    @scena.Lambda('lambda_0C56')
    def lambda_0C56():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C56)

    Sleep(300)

    @scena.Lambda('lambda_0C71')
    def lambda_0C71():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x00002EE0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C71)

    Sleep(300)

    @scena.Lambda('lambda_0C8C')
    def lambda_0C8C():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x000032C8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C8C)

    Sleep(300)

    @scena.Lambda('lambda_0CA7')
    def lambda_0CA7():
        OP_94(0x01, 0x000A, 0x00B4, 0x00009C40, 0x000036B0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CA7)

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

    @scena.Lambda('lambda_0D6A')
    def lambda_0D6A():
        CameraMove(11720, -2900, 1060, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D6A)

    SetChrPos(0x000B, 60000, 2950, 2000, 270)
    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x000B, 800)
    Sleep(500)

    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x000B, 800)
    SetChrChipByIndex(0x0105, 65535)
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

    @scena.Lambda('lambda_0DFB')
    def lambda_0DFB():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0DFB')

    DispatchAsync2(0x0101, 0x0001, lambda_0DFB)

    @scena.Lambda('lambda_0E0C')
    def lambda_0E0C():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E0C')

    DispatchAsync2(0x0102, 0x0001, lambda_0E0C)

    @scena.Lambda('lambda_0E1D')
    def lambda_0E1D():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0E1D')

    DispatchAsync2(0x0105, 0x0001, lambda_0E1D)

    OP_72(0x0002, 0x0004)
    OP_A1(0x000B, 0x0002)
    SetChrPos(0x000B, 60000, 2950, 2000, 270)
    PlaySE(219, 0x00, 0x64)

    @scena.Lambda('lambda_0E4E')
    def lambda_0E4E():
        OP_94(0x01, 0x000B, 0x0000, 0x000186A0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0E4E)

    @scena.Lambda('lambda_0E64')
    def lambda_0E64():
        CameraSetDistance(2300, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E64)

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
    SetChrPos(0x000A, -33030, -2950, 110, 90)
    TerminateThread(0x000B, 0xFF)
    SetChrPos(0x000B, 34720, 0, 18480, 270)
    SetChrPos(0x000C, 34720, 30000, 18480, 270)
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
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000B, 0x0040)

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

    @scena.Lambda('lambda_10BF')
    def lambda_10BF():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_10BF')

    DispatchAsync2(0x0008, 0x0001, lambda_10BF)

    SetChrPos(0x000B, 28720, 0, 18000, 270)
    SetChrPos(0x000C, 34720, 15000, 18000, 270)
    SetChrPos(0x0009, 300000, 300000, 300000, 0)

    @scena.Lambda('lambda_1103')
    def lambda_1103():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1103)

    @scena.Lambda('lambda_111E')
    def lambda_111E():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_111E)

    @scena.Lambda('lambda_1139')
    def lambda_1139():
        CameraMove(-31420, -2990, 9180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1139)

    @scena.Lambda('lambda_1151')
    def lambda_1151():
        OP_67(0, 11900, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1151)

    @scena.Lambda('lambda_1169')
    def lambda_1169():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1169)

    @scena.Lambda('lambda_1179')
    def lambda_1179():
        CameraSetDistance(3210, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1179)

    Sleep(2200)

    @scena.Lambda('lambda_118E')
    def lambda_118E():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_118E)

    @scena.Lambda('lambda_11A9')
    def lambda_11A9():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11A9)

    Sleep(300)

    @scena.Lambda('lambda_11C9')
    def lambda_11C9():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_11C9)

    @scena.Lambda('lambda_11E4')
    def lambda_11E4():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_11E4)

    Sleep(300)

    @scena.Lambda('lambda_1204')
    def lambda_1204():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1204)

    @scena.Lambda('lambda_121F')
    def lambda_121F():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_121F)

    Sleep(300)

    @scena.Lambda('lambda_123F')
    def lambda_123F():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_123F)

    @scena.Lambda('lambda_125A')
    def lambda_125A():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_125A)

    Sleep(300)

    @scena.Lambda('lambda_127A')
    def lambda_127A():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_127A)

    @scena.Lambda('lambda_1295')
    def lambda_1295():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1295)

    Sleep(300)

    @scena.Lambda('lambda_12B5')
    def lambda_12B5():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12B5)

    @scena.Lambda('lambda_12D0')
    def lambda_12D0():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12D0)

    Sleep(300)

    @scena.Lambda('lambda_12F0')
    def lambda_12F0():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_12F0)

    @scena.Lambda('lambda_130B')
    def lambda_130B():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_130B)

    Sleep(300)

    @scena.Lambda('lambda_132B')
    def lambda_132B():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_132B)

    @scena.Lambda('lambda_1346')
    def lambda_1346():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1346)

    Sleep(300)

    @scena.Lambda('lambda_1366')
    def lambda_1366():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1366)

    @scena.Lambda('lambda_1381')
    def lambda_1381():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1381)

    Sleep(300)

    @scena.Lambda('lambda_13A1')
    def lambda_13A1():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13A1)

    @scena.Lambda('lambda_13BC')
    def lambda_13BC():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13BC)

    Sleep(300)

    @scena.Lambda('lambda_13DC')
    def lambda_13DC():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13DC)

    @scena.Lambda('lambda_13F7')
    def lambda_13F7():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_13F7)

    Sleep(300)

    @scena.Lambda('lambda_1417')
    def lambda_1417():
        ChrMoveTo(0x000B, -19000, -2900, 18000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1417)

    @scena.Lambda('lambda_1432')
    def lambda_1432():
        ChrMoveTo(0x000C, -13000, 15000, 18000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1432)

    ChrTalk(
        0x0008,
        (
            '#0490061770V#668F#3S什、什、什么————！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_148B')
    def lambda_148B():
        CameraMove(-39220, -2900, 9180, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_148B)

    @scena.Lambda('lambda_14A3')
    def lambda_14A3():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_14A3)

    @scena.Lambda('lambda_14BE')
    def lambda_14BE():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14BE)

    Sleep(300)

    @scena.Lambda('lambda_14DE')
    def lambda_14DE():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_14DE)

    @scena.Lambda('lambda_14F9')
    def lambda_14F9():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_14F9)

    OP_72(0x0003, 0x0020)
    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1300)
    OP_70(0x0003, 1540)
    Sleep(300)

    @scena.Lambda('lambda_1530')
    def lambda_1530():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1530)

    @scena.Lambda('lambda_154B')
    def lambda_154B():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_154B)

    Sleep(300)

    @scena.Lambda('lambda_156B')
    def lambda_156B():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_156B)

    @scena.Lambda('lambda_1586')
    def lambda_1586():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1586)

    Sleep(300)

    @scena.Lambda('lambda_15A6')
    def lambda_15A6():
        ChrMoveTo(0x000B, -35520, -2900, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_15A6)

    @scena.Lambda('lambda_15C1')
    def lambda_15C1():
        ChrMoveTo(0x000C, -33520, 10000, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_15C1)

    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_15E1')
    def lambda_15E1():
        OP_67(0, 7250, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15E1)

    @scena.Lambda('lambda_15F9')
    def lambda_15F9():
        CameraMove(-35670, 4660, 3490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15F9)

    @scena.Lambda('lambda_1611')
    def lambda_1611():
        OP_6C(179000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1611)

    @scena.Lambda('lambda_1621')
    def lambda_1621():
        SetChrDirection(0x00FE, 180, 2)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1621)

    @scena.Lambda('lambda_162F')
    def lambda_162F():
        SetChrDirection(0x00FE, 180, 2)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_162F)

    @scena.Lambda('lambda_163D')
    def lambda_163D():
        OP_97(0x000B, -35520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_163D)

    @scena.Lambda('lambda_1659')
    def lambda_1659():
        OP_97(0x000C, -33520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1659)

    @scena.Lambda('lambda_1675')
    def lambda_1675():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1675)

    Sleep(150)

    @scena.Lambda('lambda_1690')
    def lambda_1690():
        SetChrDirection(0x00FE, 180, 7)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1690)

    @scena.Lambda('lambda_169E')
    def lambda_169E():
        SetChrDirection(0x00FE, 180, 7)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_169E)

    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1540)
    OP_70(0x0003, 1600)
    Sleep(150)

    @scena.Lambda('lambda_16C3')
    def lambda_16C3():
        SetChrDirection(0x00FE, 180, 11)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_16C3)

    @scena.Lambda('lambda_16D1')
    def lambda_16D1():
        SetChrDirection(0x00FE, 180, 11)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_16D1)

    @scena.Lambda('lambda_16DF')
    def lambda_16DF():
        OP_97(0x000B, -35520, 0, -90000, 7000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_16DF)

    @scena.Lambda('lambda_16FB')
    def lambda_16FB():
        OP_97(0x000C, -33520, 0, -90000, 7000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_16FB)

    @scena.Lambda('lambda_1717')
    def lambda_1717():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1717)

    Sleep(200)

    @scena.Lambda('lambda_1732')
    def lambda_1732():
        SetChrDirection(0x00FE, 180, 16)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1732)

    @scena.Lambda('lambda_1740')
    def lambda_1740():
        SetChrDirection(0x00FE, 180, 16)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1740)

    Sleep(200)

    @scena.Lambda('lambda_1753')
    def lambda_1753():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1753)

    @scena.Lambda('lambda_1761')
    def lambda_1761():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1761)

    @scena.Lambda('lambda_176F')
    def lambda_176F():
        OP_97(0x000B, -35520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_176F)

    @scena.Lambda('lambda_178B')
    def lambda_178B():
        OP_97(0x000C, -33520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_178B)

    @scena.Lambda('lambda_17A7')
    def lambda_17A7():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_17A7)

    Sleep(400)

    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 1595)
    OP_70(0x0003, 1600)

    @scena.Lambda('lambda_17D5')
    def lambda_17D5():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17D5)

    @scena.Lambda('lambda_17E3')
    def lambda_17E3():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_17E3)

    @scena.Lambda('lambda_17F1')
    def lambda_17F1():
        OP_97(0x000B, -35520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17F1)

    @scena.Lambda('lambda_180D')
    def lambda_180D():
        OP_97(0x000C, -33520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_180D)

    @scena.Lambda('lambda_1829')
    def lambda_1829():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1829)

    Sleep(400)

    @scena.Lambda('lambda_1844')
    def lambda_1844():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1844)

    @scena.Lambda('lambda_1852')
    def lambda_1852():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1852)

    @scena.Lambda('lambda_1860')
    def lambda_1860():
        OP_97(0x000B, -35520, 0, -90000, 10000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1860)

    @scena.Lambda('lambda_187C')
    def lambda_187C():
        OP_97(0x000C, -33520, 0, -90000, 10000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_187C)

    @scena.Lambda('lambda_1898')
    def lambda_1898():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1898)

    Sleep(400)

    @scena.Lambda('lambda_18B3')
    def lambda_18B3():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_18B3)

    @scena.Lambda('lambda_18C1')
    def lambda_18C1():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_18C1)

    @scena.Lambda('lambda_18CF')
    def lambda_18CF():
        OP_97(0x000B, -35520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_18CF)

    @scena.Lambda('lambda_18EB')
    def lambda_18EB():
        OP_97(0x000C, -33520, 0, -90000, 9000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_18EB)

    @scena.Lambda('lambda_1907')
    def lambda_1907():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1907)

    Sleep(400)

    @scena.Lambda('lambda_1922')
    def lambda_1922():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1922)

    @scena.Lambda('lambda_1930')
    def lambda_1930():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1930)

    @scena.Lambda('lambda_193E')
    def lambda_193E():
        OP_97(0x000B, -35520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_193E)

    @scena.Lambda('lambda_195A')
    def lambda_195A():
        OP_97(0x000C, -33520, 0, -90000, 8000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_195A)

    @scena.Lambda('lambda_1976')
    def lambda_1976():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1976)

    Sleep(400)

    @scena.Lambda('lambda_1991')
    def lambda_1991():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1991)

    @scena.Lambda('lambda_199F')
    def lambda_199F():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_199F)

    @scena.Lambda('lambda_19AD')
    def lambda_19AD():
        OP_97(0x000B, -35520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_19AD)

    @scena.Lambda('lambda_19C9')
    def lambda_19C9():
        OP_97(0x000C, -33520, 0, -90000, 6000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_19C9)

    @scena.Lambda('lambda_19E5')
    def lambda_19E5():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_19E5)

    Sleep(300)

    @scena.Lambda('lambda_1A00')
    def lambda_1A00():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1A00)

    @scena.Lambda('lambda_1A0E')
    def lambda_1A0E():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1A0E)

    @scena.Lambda('lambda_1A1C')
    def lambda_1A1C():
        OP_97(0x000B, -35520, 0, -90000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A1C)

    @scena.Lambda('lambda_1A38')
    def lambda_1A38():
        OP_97(0x000C, -33520, 0, -90000, 5000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1A38)

    @scena.Lambda('lambda_1A54')
    def lambda_1A54():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1A54)

    Sleep(200)

    @scena.Lambda('lambda_1A6F')
    def lambda_1A6F():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1A6F)

    @scena.Lambda('lambda_1A7D')
    def lambda_1A7D():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1A7D)

    @scena.Lambda('lambda_1A8B')
    def lambda_1A8B():
        OP_97(0x000B, -35520, 0, -90000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A8B)

    @scena.Lambda('lambda_1AA7')
    def lambda_1AA7():
        OP_97(0x000C, -33520, 0, -90000, 4000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1AA7)

    @scena.Lambda('lambda_1AC3')
    def lambda_1AC3():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1AC3)

    Sleep(100)

    @scena.Lambda('lambda_1ADE')
    def lambda_1ADE():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1ADE)

    @scena.Lambda('lambda_1AEC')
    def lambda_1AEC():
        SetChrDirection(0x00FE, 180, 22)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1AEC)

    @scena.Lambda('lambda_1AFA')
    def lambda_1AFA():
        OP_97(0x000B, -35520, 0, -90000, 3000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1AFA)

    @scena.Lambda('lambda_1B16')
    def lambda_1B16():
        OP_97(0x000C, -33520, 0, -90000, 3000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B16)

    @scena.Lambda('lambda_1B32')
    def lambda_1B32():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B32)

    Sleep(100)

    @scena.Lambda('lambda_1B4D')
    def lambda_1B4D():
        OP_97(0x000B, -35520, 0, -90000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B4D)

    @scena.Lambda('lambda_1B69')
    def lambda_1B69():
        OP_97(0x000C, -33520, 0, -90000, 2000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B69)

    @scena.Lambda('lambda_1B85')
    def lambda_1B85():
        OP_94(0x01, 0x000A, 0x0000, 0x00001388, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B85)

    Sleep(100)

    @scena.Lambda('lambda_1BA0')
    def lambda_1BA0():
        OP_97(0x000B, -35520, 0, -90000, 1000, 0x0000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1BA0)

    @scena.Lambda('lambda_1BBC')
    def lambda_1BBC():
        OP_97(0x000C, -33520, 0, -90000, 1000, 0x0000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1BBC)

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

    @scena.Lambda('lambda_1C23')
    def lambda_1C23():
        CameraMove(46000, -2990, -4059, 8100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C23)

    @scena.Lambda('lambda_1C3B')
    def lambda_1C3B():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 300, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1C3B)

    @scena.Lambda('lambda_1C56')
    def lambda_1C56():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1C56)

    @scena.Lambda('lambda_1C71')
    def lambda_1C71():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1C71)

    Sleep(200)

    @scena.Lambda('lambda_1C91')
    def lambda_1C91():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1C91)

    @scena.Lambda('lambda_1CAC')
    def lambda_1CAC():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1CAC)

    @scena.Lambda('lambda_1CC7')
    def lambda_1CC7():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1CC7)

    Sleep(200)

    @scena.Lambda('lambda_1CE7')
    def lambda_1CE7():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1CE7)

    @scena.Lambda('lambda_1D02')
    def lambda_1D02():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1D02)

    @scena.Lambda('lambda_1D1D')
    def lambda_1D1D():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1D1D)

    Sleep(200)

    @scena.Lambda('lambda_1D3D')
    def lambda_1D3D():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1D3D)

    @scena.Lambda('lambda_1D58')
    def lambda_1D58():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1D58)

    @scena.Lambda('lambda_1D73')
    def lambda_1D73():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1D73)

    Sleep(200)

    @scena.Lambda('lambda_1D93')
    def lambda_1D93():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1D93)

    @scena.Lambda('lambda_1DAE')
    def lambda_1DAE():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1DAE)

    @scena.Lambda('lambda_1DC9')
    def lambda_1DC9():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1DC9)

    Sleep(200)

    @scena.Lambda('lambda_1DE9')
    def lambda_1DE9():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 2800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1DE9)

    @scena.Lambda('lambda_1E04')
    def lambda_1E04():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1E04)

    @scena.Lambda('lambda_1E1F')
    def lambda_1E1F():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1E1F)

    Sleep(200)

    @scena.Lambda('lambda_1E3F')
    def lambda_1E3F():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 3733, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1E3F)

    @scena.Lambda('lambda_1E5A')
    def lambda_1E5A():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1E5A)

    @scena.Lambda('lambda_1E75')
    def lambda_1E75():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1E75)

    Sleep(200)

    @scena.Lambda('lambda_1E95')
    def lambda_1E95():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1E95)

    @scena.Lambda('lambda_1EB0')
    def lambda_1EB0():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1EB0)

    @scena.Lambda('lambda_1ECB')
    def lambda_1ECB():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1ECB)

    Sleep(200)

    @scena.Lambda('lambda_1EEB')
    def lambda_1EEB():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1EEB)

    @scena.Lambda('lambda_1F06')
    def lambda_1F06():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1F06)

    Sleep(200)

    @scena.Lambda('lambda_1F26')
    def lambda_1F26():
        ChrMoveToRelativeAsync(0x00FE, 30000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1F26)

    @scena.Lambda('lambda_1F41')
    def lambda_1F41():
        ChrMoveToRelativeAsync(0x00FE, 30000, -10000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1F41)

    OP_B0(0x0003, 0x1E)
    OP_6F(0x0003, 1670)
    OP_70(0x0003, 1800)

    @scena.Lambda('lambda_1F6E')
    def lambda_1F6E():
        SetChrDirection(0x00FE, 180, 33)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1F6E)

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
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    Sleep(500)

    @scena.Lambda('lambda_2586')
    def lambda_2586():
        ChrMoveToRelativeAsync(0x00FE, 300000, -30000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_2586)

    @scena.Lambda('lambda_25A1')
    def lambda_25A1():
        ChrMoveToRelativeAsync(0x00FE, 300000, -30000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_25A1)

    @scena.Lambda('lambda_25BC')
    def lambda_25BC():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 19500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_25BC)

    Sleep(150)

    @scena.Lambda('lambda_25DC')
    def lambda_25DC():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 19000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_25DC)

    Sleep(150)

    @scena.Lambda('lambda_25FC')
    def lambda_25FC():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_25FC)

    Sleep(150)

    @scena.Lambda('lambda_261C')
    def lambda_261C():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 17000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_261C)

    Sleep(150)

    @scena.Lambda('lambda_263C')
    def lambda_263C():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_263C)

    Sleep(150)

    @scena.Lambda('lambda_265C')
    def lambda_265C():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_265C)

    Sleep(150)

    @scena.Lambda('lambda_267C')
    def lambda_267C():
        ChrMoveToRelativeAsync(0x00FE, 300000, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_267C)

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
