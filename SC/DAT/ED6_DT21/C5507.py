import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5507_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5507   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5507.x'
    header.mapIndex       = 1
    header.bgm            = 21
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
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00264._CH', 'ED6_DT07/CH00264P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT27/CH03095._CH', 'ED6_DT27/CH03095P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH04640._CH', 'ED6_DT27/CH04640P._CP'),
        ('ED6_DT27/CH04641._CH', 'ED6_DT27/CH04641P._CP'),
        ('ED6_DT27/CH04642._CH', 'ED6_DT27/CH04642P._CP'),
        ('ED6_DT27/CH04644._CH', 'ED6_DT27/CH04644P._CP'),
        ('ED6_DT26/CH20265._CH', 'ED6_DT26/CH20265P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '女猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '发烟筒用目标角色',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1900552,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
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
    )

# id: 0x10002 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x17A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2500,
            y           = -100,
            z           = 28500,
            range       = 8500,
            dword_10    = 0x0000076C,
            dword_14    = 0x00007724,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -3520,
            y           = 0,
            z           = -11140,
            range       = 8109,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE17E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10004 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 5300,
            triggerZ            = 0,
            triggerY            = 9990,
            triggerRange        = 800,
            actorX              = 5300,
            actorZ              = 1000,
            actorY              = 9990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1EC',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_05_115D)

    def _loc_1EC(): pass

    label('loc_1EC')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_200',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 1, 0x1011)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_200',
    )

    def _loc_200(): pass

    label('loc_200')

    Return()

# id: 0x0001 offset: 0x201
@scena.Code('func_01_201')
def func_01_201():
    Return()

# id: 0x0002 offset: 0x202
@scena.Code('func_02_202')
def func_02_202():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 1, 0x1011)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_211',
    )

    Call(0, 0x0003)

    Jump('loc_211')

    def _loc_211(): pass

    label('loc_211')

    Return()

# id: 0x0003 offset: 0x212
@scena.Code('func_03_212')
def func_03_212():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0202, 1, 0x1011))
    Fade(1000)
    CameraMove(2510, 0, -9490, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4140, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2310, 0, -8920, 339)
    ChrSetPos(0x010A, 3870, 0, -9500, 1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_339',
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
            TXT(0x00, '【◇回收６个装备】\n'),
            TXT(0x01, '【◇装备１个也不回收】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_311',
    )

    SetScenaFlags(ScenaFlag(0x0224, 0, 0x1120))
    SetScenaFlags(ScenaFlag(0x0224, 1, 0x1121))
    SetScenaFlags(ScenaFlag(0x0224, 2, 0x1122))
    SetScenaFlags(ScenaFlag(0x0226, 0, 0x1130))
    SetScenaFlags(ScenaFlag(0x0226, 2, 0x1132))
    SetScenaFlags(ScenaFlag(0x0226, 3, 0x1133))

    Jump('loc_330')

    def _loc_311(): pass

    label('loc_311')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_330',
    )

    ClearScenaFlags(ScenaFlag(0x0224, 0, 0x1120))
    ClearScenaFlags(ScenaFlag(0x0224, 1, 0x1121))
    ClearScenaFlags(ScenaFlag(0x0224, 2, 0x1122))
    ClearScenaFlags(ScenaFlag(0x0226, 0, 0x1130))
    ClearScenaFlags(ScenaFlag(0x0226, 2, 0x1132))
    ClearScenaFlags(ScenaFlag(0x0226, 3, 0x1133))

    def _loc_330(): pass

    label('loc_330')

    FadeIn(300, 0)

    def _loc_339(): pass

    label('loc_339')

    @scena.Lambda('lambda_033F')
    def lambda_033F():
        ChrWalkTo(0x0101, 1300, 0, 2830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_033F)

    Sleep(100)

    @scena.Lambda('lambda_035F')
    def lambda_035F():
        ChrWalkTo(0x010A, 2500, 0, 2830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_035F)

    @scena.Lambda('lambda_037A')
    def lambda_037A():
        CameraMove(2090, 0, 22590, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_037A)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    @scena.Lambda('lambda_039C')
    def lambda_039C():
        CameraMove(2150, 0, 2820, 3000)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_039C)

    @scena.Lambda('lambda_03B4')
    def lambda_03B4():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_03B4)

    @scena.Lambda('lambda_03CC')
    def lambda_03CC():
        CameraSetDistance(3220, 3000)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_03CC)

    WaitForThreadExit(0x010A, 0x0000)
    WaitForThreadExit(0x010A, 0x0001)
    WaitForThreadExit(0x010A, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x010A, 500)
    Sleep(100)

    ChrTurnDirection(0x010A, 0x0101, 500)

    ChrTalk(
        0x0101,
        (
            '#0010191249V#1018F#6P亚妮拉丝！\n',
            '那里好像是出口！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191250V#2P#819F呼～……\n',
            '总算能松一口气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, 70, 0, 18120, 180)
    ChrTurnDirection(0x0008, 0x0101, 1000)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 3)

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0320191251V哎呀哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0320191252V稍微转移一下视线\n',
            '就趁机逃跑的坏孩子们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_053F')
    def lambda_053F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_053F)

    @scena.Lambda('lambda_054D')
    def lambda_054D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_054D)

    Sleep(300)

    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 440, 1000, 10570, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1180, 1000, 8170, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 820, 1000, 5160, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0627')
    def lambda_0627():
        ChrJumpTo(0x00FE, 0, 0, 1500, 600, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0627)

    Sleep(50)

    @scena.Lambda('lambda_064A')
    def lambda_064A():
        ChrJumpTo(0x00FE, 2700, 0, 1340, 600, 6000)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_064A)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1740, 1000, 1930, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetSubChip(0x010A, 0)
    ChrSetChipByIndex(0x010A, 7)
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1680, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 2000, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#6P#1021F#1K呀……！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x010A,
        (
            '#0120191254V#5P#1312F#1K呜……！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    OP_56(0x01)
    OP_59()
    PlayBGM(86)
    Sleep(500)

    OP_69(0x0008, 2000)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x010A, 0)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 10)

    @scena.Lambda('lambda_07EA')
    def lambda_07EA():
        ChrWalkTo(0x00FE, 130, 0, 8260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07EA)

    @scena.Lambda('lambda_0805')
    def lambda_0805():
        CameraMove(900, 0, 4900, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0805)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 9)
    WaitForThreadExit(0x0008, 0x0002)

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191255V#5P呵呵……\n',
            '欢迎来到我的猎场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191256V#1004F#6P女、女人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191257V#815F#2P艾丝蒂尔，小心！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191258V这个人……相当强哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191259V#5P哎呀……\n',
            '观察力很有一套啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191260V#5P而且，吸了那种气体后\n',
            '居然这么快就醒来，真令人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191261V#5P不愧是游击士。\n',
            '看来不只是体力过人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191262V#1005F#6P你、你们这些人！\n',
            '到底有什么目的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191263V为什么要袭击训练场！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191264V#5P呵呵……\n',
            '我没有义务回答你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191265V#5P你们的选择只有两个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191266V#5P乖乖地投降，\n',
            '或是就这样成为我的猎物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 0, 0x1120)),
            Expr.Return,
        ),
        'loc_AC1',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AC1(): pass

    label('loc_AC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 1, 0x1121)),
            Expr.Return,
        ),
        'loc_AD2',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AD2(): pass

    label('loc_AD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 2, 0x1122)),
            Expr.Return,
        ),
        'loc_AE3',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AE3(): pass

    label('loc_AE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 0, 0x1130)),
            Expr.Return,
        ),
        'loc_AF4',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_AF4(): pass

    label('loc_AF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 2, 0x1132)),
            Expr.Return,
        ),
        'loc_B05',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_B05(): pass

    label('loc_B05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0226, 3, 0x1133)),
            Expr.Return,
        ),
        'loc_B16',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_B16(): pass

    label('loc_B16')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_B80',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191267V#1002F#6P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191268V（用回收来的装备\n',
            '  好歹可以应战吧……！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BDC')

    def _loc_B80(): pass

    label('loc_B80')

    ChrTalk(
        0x0101,
        (
            '#0010191269V#1003F#6P呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191270V（要跟这个人战斗，\n',
            '  装备实在太贫乏了……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDC(): pass

    label('loc_BDC')

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
            TXT(0x00, '【暂且撤退】\n'),
            TXT(0x01, '【就这样挑战】\n'),
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
        'loc_FC1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191271V#1005F#6P……亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191272V#815F#2P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x010A, 0)
    ChrSetChipByIndex(0x010A, 65535)

    @scena.Lambda('lambda_0CA0')
    def lambda_0CA0():
        ChrSetDirection(0x00FE, 180, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CA0)

    Sleep(200)

    @scena.Lambda('lambda_0CB3')
    def lambda_0CB3():
        ChrSetDirection(0x00FE, 180, 800)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0CB3)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0CC6')
    def lambda_0CC6():
        ChrWalkTo(0x00FE, 2000, 0, -16180, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CC6)

    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_0CE6')
    def lambda_0CE6():
        ChrWalkTo(0x00FE, 2000, 0, -16180, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_0CE6)

    @scena.Lambda('lambda_0D01')
    def lambda_0D01():
        CameraMove(2970, 0, -7130, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D01)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 3)
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    LoadEffect(0x01, 'monster\\\\msc0310.eff')
    Sleep(200)

    CreateThread(0x0008, 0x03, 0x00, func_04_10AB)
    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1280, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 900, 1000, -3630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1300, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1000, 1000, -5760, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1300, 1000, -6630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 1960, 1000, -7810, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Sleep(500)

    @scena.Lambda('lambda_0F34')
    def lambda_0F34():
        OP_69(0x0008, 2000)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_0F34)

    WaitForThreadExit(0x010A, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 9)

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191273V也罢。\n',
            '反正出口只有这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191274V就让我慢慢狩猎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5512._SN', 102, 0, 0)
    IdleLoop()

    Jump('loc_10A6')

    def _loc_FC1(): pass

    label('loc_FC1')

    ChrTalk(
        0x0101,
        (
            '#0010191275V#1005F#6P亚妮拉丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191276V#815F#2P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 1)
    Sleep(100)

    ChrSetSubChip(0x010A, 0)
    ChrSetChipByIndex(0x010A, 3)
    Sleep(500)

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191277V#5P呵呵……\n',
            '好吧，小猫咪们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191278V#5P就让我尽情狩猎吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

    def _loc_10A6(): pass

    label('loc_10A6')

    Call(0, 0x0006)

    Return()

# id: 0x0004 offset: 0x10AB
@scena.Code('func_04_10AB')
def func_04_10AB():
    PlayEffect(0x01, 0x00, 0x00FF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x01, 0x00, 0x00FF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x01, 0x00, 0x00FF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    StopEffect(0x00, 0x02)

    Return()

# id: 0x0005 offset: 0x115D
@scena.Code('func_05_115D')
def func_05_115D():
    EventBegin(0x00)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, 0, 0, 10770, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x010A, 3)
    ChrSetPos(0x0101, 1370, 0, -36430, 0)
    ChrSetPos(0x010A, 3490, 0, -37430, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_11DC')
    def lambda_11DC():
        ChrWalkTo(0x0101, -1470, 0, 7500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11DC)

    @scena.Lambda('lambda_11F7')
    def lambda_11F7():
        ChrWalkTo(0x010A, 1470, 0, 7500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_11F7)

    Sleep(1000)

    OP_0D()
    Fade(500)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    ChrSetPos(0x0101, -470, 0, -3500, 0)
    ChrSetPos(0x010A, 1320, 0, -4500, 0)

    @scena.Lambda('lambda_1247')
    def lambda_1247():
        ChrWalkTo(0x0101, -470, 0, 4590, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1247)

    @scena.Lambda('lambda_1262')
    def lambda_1262():
        ChrWalkTo(0x010A, 1320, 0, 4520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1262)

    CameraMove(390, 0, 7240, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010191287V#1005F#6P让你久等了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191288V#815F#2P我们这次一定要\n',
            '通过那里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191277V#5P呵呵……\n',
            '好吧，小猫咪们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191278V#5P就让我尽情狩猎吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    Battle(0x00000394, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x13B4
@scena.Code('func_06_13B4')
def func_06_13B4():
    MapClearFlags(0x00000001)
    CameraMove(730, 0, 7340, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3260, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, 0, 0, 10770, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 12)
    ChrSetSubChip(0x0008, 3)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x010A, 3)
    ChrSetPos(0x0101, -580, 0, 5380, 6)
    ChrSetPos(0x010A, 2060, 0, 5380, 343)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191291V#5P唔……\n',
            '有点小看你们了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191292V#1005F#6P呼呼……\n',
            '可别小看游击士哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191293V#812F#2P被我们两个小丫头羞辱，\n',
            '你的好运也到此为止了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女猎兵',
        (
            '#0320191294V#5P呵呵，好勇敢的\n',
            '小猫咪们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetChipByIndex(0x0008, 13)
    ChrSetFlags(0x0008, 0x0002)
    LoadEffect(0x00, 'map\\\\mp004_00.eff')
    ChrSetPos(0x0009, 70, 0, 6150, 28)

    @scena.Lambda('lambda_1571')
    def lambda_1571():
        OP_99(0x00FE, 0x00, 0x09, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1571)

    Sleep(800)

    PlayEffect(0x00, 0xFF, 0x0008, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0x0009, 0, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010191295V#6P#1020F#10A……又来了！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1200)

    PlaySE(127, 0x00, 0x64)

    ChrTalk(
        0x010A,
        (
            '#0120191296V#815F#2P#12A艾丝蒂尔，摒住呼吸！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1700)

    ChrSetDirection(0x0101, 45, 0)
    ChrSetDirection(0x0101, 315, 0)

    @scena.Lambda('lambda_1635')
    def lambda_1635():
        ChrJumpTo(0x00FE, -2860, 0, 5030, 600, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1635)

    @scena.Lambda('lambda_1653')
    def lambda_1653():
        ChrJumpTo(0x00FE, 2300, 0, 5380, 600, 6000)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1653)

    Sleep(100)

    ChrTurnDirection(0x0101, 0x0008, 1000)
    ChrTurnDirection(0x010A, 0x0008, 1000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x010A, 0x0001)
    Sleep(300)

    FadeOut(500, 16777215, -1)
    OP_0D()
    Sleep(2000)

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0320191297V方术使已经被抓住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0320191298V小猫咪们没有同伴了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0320191299V赶快死心投降吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 10)

    @scena.Lambda('lambda_173C')
    def lambda_173C():
        ChrWalkTo(0x00FE, -50, 0, 21870, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_173C)

    FadeOut(2000, 16777215, -1)
    OP_0D()
    TerminateThread(0x0008, 0x01)
    OP_20(0x000007D0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetDirection(0x0101, 0, 0)
    ChrSetDirection(0x0101, 0, 0)
    FadeIn(2000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191300V#1007F#6P逃掉了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    Sleep(100)

    ChrSetSubChip(0x010A, 0)
    ChrSetChipByIndex(0x010A, 65535)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x010A, 500)

    @scena.Lambda('lambda_17E4')
    def lambda_17E4():
        ChrWalkTo(0x00FE, -700, 0, 5210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17E4)

    @scena.Lambda('lambda_17FF')
    def lambda_17FF():
        CameraMove(-100, 0, 5180, 1200)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_17FF)

    @scena.Lambda('lambda_1817')
    def lambda_1817():
        ChrTurnDirection(0x010A, 0x0101, 500)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_1817)

    WaitForThreadExit(0x010A, 0x0001)

    @scena.Lambda('lambda_182A')
    def lambda_182A():
        ChrWalkTo(0x00FE, 600, 0, 5130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_182A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x010A, 0x0001)
    WaitForThreadExit(0x010A, 0x0003)
    Sleep(150)

    ChrTalk(
        0x0101,
        (
            '#0010191301V#1002F#6P亚妮拉丝。\n',
            '我们还是别追击比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191302V#812F是啊……\n',
            '而且也有被伏击的危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191303V#813F对了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191304V刚才那人说\n',
            '『方术使被抓住』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191305V#1026F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191306V#1003F嗯……\n',
            '我想指的应该是克鲁茨前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191307V#813F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191308V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191309V#1018F#6P没、没问题的啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191310V即使真的被抓住，\n',
            '克鲁茨前辈也一定会没事的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191311V#1006F而且……这种时候才\n',
            '更应该活用训练中学到的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191312V#814F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191313V非常时期的行动、确保安全、\n',
            '还有反恐技术……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191314V#816F嗯……确实如此！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191315V我们必须活用所学到的东西\n',
            '救出克鲁茨前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191316V#1001F#6P嗯嗯，就是这种气势！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191317V#1006F对了，亚妮拉丝。\n',
            '我们要不要先回宿舍一趟？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191318V我想最好去确认一下\n',
            '是否已经被敌人占领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191319V#810F嗯，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191320V那么就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0202, 2, 0x1012))
    OP_28(0x007F, 0x01, 0x2000)
    OP_28(0x007F, 0x01, 0x4000)
    OP_28(0x007F, 0x01, 0x8000)
    OP_28(0x0080, 0x04, 0x02)
    OP_28(0x0080, 0x04, 0x08)
    PlayBGM(21)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1C0F
@scena.Code('func_07_1C0F')
def func_07_1C0F():
    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_1C2D',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1C3E')

    def _loc_1C2D(): pass

    label('loc_1C2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Return,
        ),
        'loc_1C3E',
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C3E(): pass

    label('loc_1C3E')

    MapSetFlags(0x00000080)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS137._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CAF(): pass

    label('loc_1CAF')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FCC',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x4),
            Expr.Return,
        ),
        (0x00000000, 'loc_1CDA'),
        (0x00000001, 'loc_1D06'),
        (0x00000002, 'loc_1D43'),
        (-1, 'loc_1D95'),
    )

    def _loc_1CDA(): pass

    label('loc_1CDA')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
        ),
    )

    Jump('loc_1D95')

    def _loc_1D06(): pass

    label('loc_1D06')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
        ),
    )

    Jump('loc_1D95')

    def _loc_1D43(): pass

    label('loc_1D43')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
            TXT(0x03, '【格林姆瑟尔小要塞】\n'),
        ),
    )

    Jump('loc_1D95')

    def _loc_1D95(): pass

    label('loc_1D95')

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
        (0x00000000, 'loc_1DBF'),
        (0x00000001, 'loc_1E3F'),
        (0x00000002, 'loc_1EC1'),
        (0x00000003, 'loc_1F43'),
        (-1, 'loc_1FC9'),
    )

    def _loc_1DBF(): pass

    label('loc_1DBF')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【训练场宿舍】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E2C'),
        (0x00000001, 'loc_1E39'),
        (-1, 'loc_1E3C'),
    )

    def _loc_1E2C(): pass

    label('loc_1E2C')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1E3C')

    def _loc_1E39(): pass

    label('loc_1E39')

    Jump('loc_1E3C')

    def _loc_1E3C(): pass

    label('loc_1E3C')

    Jump('loc_1FC9')

    def _loc_1E3F(): pass

    label('loc_1E3F')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【巴斯塔尔水道】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1EAE'),
        (0x00000001, 'loc_1EBB'),
        (-1, 'loc_1EBE'),
    )

    def _loc_1EAE(): pass

    label('loc_1EAE')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1EBE')

    def _loc_1EBB(): pass

    label('loc_1EBB')

    Jump('loc_1EBE')

    def _loc_1EBE(): pass

    label('loc_1EBE')

    Jump('loc_1FC9')

    def _loc_1EC1(): pass

    label('loc_1EC1')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【圣科洛瓦森林】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1F30'),
        (0x00000001, 'loc_1F3D'),
        (-1, 'loc_1F40'),
    )

    def _loc_1F30(): pass

    label('loc_1F30')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F40')

    def _loc_1F3D(): pass

    label('loc_1F3D')

    Jump('loc_1F40')

    def _loc_1F40(): pass

    label('loc_1F40')

    Jump('loc_1FC9')

    def _loc_1F43(): pass

    label('loc_1F43')

    TalkSetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【格林姆瑟尔小要塞】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FB6'),
        (0x00000001, 'loc_1FC3'),
        (-1, 'loc_1FC6'),
    )

    def _loc_1FB6(): pass

    label('loc_1FB6')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1FC6')

    def _loc_1FC3(): pass

    label('loc_1FC3')

    Jump('loc_1FC6')

    def _loc_1FC6(): pass

    label('loc_1FC6')

    Jump('loc_1FC9')

    def _loc_1FC9(): pass

    label('loc_1FC9')

    Jump('loc_1CAF')

    def _loc_1FCC(): pass

    label('loc_1FCC')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FE5'),
        (0x00000001, 'loc_2019'),
        (0x00000002, 'loc_204D'),
        (0x00000003, 'loc_2081'),
        (-1, 'loc_20B5'),
    )

    def _loc_1FE5(): pass

    label('loc_1FE5')

    OP_C6(0x00, 0x00, -640000, 0, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_20B5')

    def _loc_2019(): pass

    label('loc_2019')

    OP_C6(0x00, 0x00, -358000, -37000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_20B5')

    def _loc_204D(): pass

    label('loc_204D')

    OP_C6(0x00, 0x00, -362000, -266000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_20B5')

    def _loc_2081(): pass

    label('loc_2081')

    OP_C6(0x00, 0x00, -64000, -340000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_20B5')

    def _loc_20B5(): pass

    label('loc_20B5')

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_20E6'),
        (0x00000001, 'loc_20F2'),
        (0x00000002, 'loc_20FE'),
        (0x00000003, 'loc_210A'),
        (-1, 'loc_2116'),
    )

    def _loc_20E6(): pass

    label('loc_20E6')

    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2116')

    def _loc_20F2(): pass

    label('loc_20F2')

    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2116')

    def _loc_20FE(): pass

    label('loc_20FE')

    NewScene('ED6_DT21/C5507._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_2116')

    def _loc_210A(): pass

    label('loc_210A')

    NewScene('ED6_DT21/C5508._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_2116')

    def _loc_2116(): pass

    label('loc_2116')

    Return()

# id: 0x0008 offset: 0x2117
@scena.Code('func_08_2117')
def func_08_2117():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【圣科洛瓦森林】',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '除了巡逻训练之外，\n',
            '也推荐进行生存训练等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
