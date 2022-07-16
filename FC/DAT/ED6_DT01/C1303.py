import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '吉尔'),
    TXT(0x03, '多伦'),
    TXT(0x04, '罐子'),
    TXT(0x05, '　T'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1303.x'
    header.mapIndex       = 52
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x282F
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
            word_3A         = 52,
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
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP'),
        ('ED6_DT07/CH00290._CH', 'ED6_DT07/CH00290P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH00292._CH', 'ED6_DT07/CH00292P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP'),
        ('ED6_DT07/CH00304._CH', 'ED6_DT07/CH00304P._CP'),
        ('ED6_DT07/CH00294._CH', 'ED6_DT07/CH00294P._CP'),
        ('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT07/CH00291._CH', 'ED6_DT07/CH00291P._CP'),
        ('ED6_DT07/CH00305._CH', 'ED6_DT07/CH00305P._CP'),
        ('ED6_DT06/CH20065._CH', 'ED6_DT06/CH20065P._CP'),
        ('ED6_DT06/CH20066._CH', 'ED6_DT06/CH20066P._CP'),
        ('ED6_DT06/CH20067._CH', 'ED6_DT06/CH20067P._CP'),
    ]

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -36460,
            z                   = 0,
            y                   = -82960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35810,
            z                   = 0,
            y                   = -83940,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -34100,
            z                   = 0,
            y                   = -82100,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -34310,
            z                   = 1000,
            y                   = -83180,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 1000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -22008,
            y           = -3000,
            z           = -168710,
            range       = -26065,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFD625F,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -36040,
            triggerZ            = 0,
            triggerY            = -121030,
            triggerRange        = 800,
            actorX              = -36040,
            actorZ              = 1000,
            actorY              = -121030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -75460,
            triggerZ            = 0,
            triggerY            = -119560,
            triggerRange        = 1000,
            actorX              = -75450,
            actorZ              = 1500,
            actorY              = -118890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x27B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 4, 0x384)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28D',
    )

    OP_6F(0x0002, 0)

    Jump('loc_294')

    def _loc_28D(): pass

    label('loc_28D')

    OP_6F(0x0002, 60)

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AB',
    )

    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)

    Jump('loc_2AF')

    def _loc_2AB(): pass

    label('loc_2AB')

    OP_64(0x00, 0x0001)

    def _loc_2AF(): pass

    label('loc_2AF')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x389),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C4(): pass

    label('loc_2C4')

    Return()

# id: 0x0002 offset: 0x2C5
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2DA(): pass

    label('loc_2DA')

    Return()

# id: 0x0003 offset: 0x2DB
@scena.Code('func_03_2DB')
def func_03_2DB():
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有熟悉的声音传出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010031541V#002F这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031542V#012F嗯……\n',
            '这里应该就是首领的房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【看准机会冲进去】\n'),
            TXT(0x01, '【还是算了】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_3D7'),
        (0x00000000, 'loc_3DC'),
        (-1, 'loc_24BE'),
    )

    def _loc_3D7(): pass

    label('loc_3D7')

    EventEnd(0x01)

    Jump('loc_24BE')

    def _loc_3DC(): pass

    label('loc_3DC')

    OP_20(0x000005DC)
    Fade(1000)
    CameraMove(-34780, 0, -82570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, -34290, 500, -83750, 45)
    SetMapFlags(0x00400000)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000B, 0x0002)
    SetChrSubChip(0x000B, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)
    SetChrDirection(0x000A, 225, 0)

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    OP_21()
    PlayBGM(87)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0300031543V#193F哼哼哼……\n',
            '女王打算出赎金了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031544V这下总算和贫穷的生活说再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031545V#200F大哥，现在还不能大意。\n',
            '拿到赎金之后才能完全放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031546V#211F嗯嗯，要不我们先\n',
            '计划一下怎么释放人质吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031547V#193F释放人质？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031548V喂喂，\n',
            '为啥我们非要干\n',
            '那么拖泥带水的事不可呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031549V#213F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031550V#193F米拉到手后\n',
            '把他们杀光不就了事了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031551V没必要留活口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031552V#216F多、多伦大哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031553V#201F你、你在开玩笑吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031554V#193F那些人质肯定\n',
            '记得我们的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031555V就算我们逃出了利贝尔，\n',
            '也难保日后没有后顾之忧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031556V#214F但、但人质里面\n',
            '还有老人和小孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031557V你真的打算杀了他们吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031558V#193F哼！混了这么久，\n',
            '你们的思维还是这么单纯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031559V我们可不是在玩过家家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031560V#215F怎、怎么会……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031561V#203F大哥……\n',
            '不好意思，我反对这样做。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031562V要是真的这样做的话，\n',
            '空之女神也不会原谅我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031563V#200F而且……\n',
            '我也不想把染血的米拉带回故乡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031564V#193F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031565V吉尔，你小子……\n',
            '啥时候变得这么伟大了呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031566V#200F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031567V#195F少给我说废话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 180, 400)
    SetChrChipByIndex(0x000A, 22)
    SetChrSubChip(0x000A, 0)
    Sleep(150)

    ChrTurnDirection(0x000A, 0x0009, 0)
    SetChrChipByIndex(0x000B, 23)

    @scena.Lambda('lambda_0913')
    def lambda_0913():
        OP_99(0x00FE, 0x00, 0x07, 1700)
        Yield()

        Jump('lambda_0913')

    DispatchAsync2(0x000B, 0x0001, lambda_0913)

    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000B, 0x0080)
    PlaySE(132, 0x00, 0x64)
    SetChrSubChip(0x000A, 1)
    Sleep(150)

    SetChrSubChip(0x000A, 2)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -34270, 980, -81780, 225)
    ChrJumpTo(0x000B, -35900, 400, -83710, 1000, 6000)

    @scena.Lambda('lambda_0971')
    def lambda_0971():
        ChrJumpToRelative(0x000B, 0, -1000, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0971)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_098F)

    PlaySE(555, 0x00, 0x64)
    PlaySE(248, 0x00, 0x64)
    OP_7C(0, 100, 3000, 50)
    TerminateThread(0x0009, 0xFF)
    ChrJumpTo(0x0009, -36790, 0, -85000, 500, 5000)
    SetChrChipByIndex(0x0009, 16)
    SetChrSubChip(0x0009, 3)
    SetChrChipByIndex(0x000A, 5)

    ChrTalk(
        0x0009,
        (
            '#0290031568V#205F啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000B, 0x0080)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0090031569V#216F吉尔哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0004)
    OP_92(0x0008, 0x0009, 700, 3000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0300031570V#194F嘎哈哈，什么故乡呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031571V好不容易才得到那么一大笔钱，\n',
            '难道你还打算浪费掉，\n',
            '去买回那种不值钱的土地吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031572V哈，我可是决定要去\n',
            '南方的度假别墅享受一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031573V#201F什么……可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031574V#193F要是米拉花完了，\n',
            '再干一票抢夺定期船的买卖不就搞定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031575V这就是今后\n',
            '『卡普亚空贼团』要干的大事呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0300031576V#194F#5S嘎哇～哈哈哈！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0090031577V#215F多伦大哥……\n',
            '你真的要那样……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031578V#214F难道你真的要那样做吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 7)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x0101, -35150, 0, -91730, 0)
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010031579V#1P在这种时候突然插话\n',
            '真不好意思呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031580V兄妹吵架可以放到以后吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0CEF')
    def lambda_0CEF():
        CameraMove(-34550, 0, -85900, 1500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0CEF)

    SetChrChipByIndex(0x0102, 9)
    SetChrChipByIndex(0x0104, 11)
    SetChrChipByIndex(0x0103, 13)

    @scena.Lambda('lambda_0D16')
    def lambda_0D16():
        SetChrDirection(0x000A, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0D16)

    @scena.Lambda('lambda_0D24')
    def lambda_0D24():
        SetChrDirection(0x0008, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D24)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_0D37')
    def lambda_0D37():
        ChrWalkTo(0x00FE, -35190, 0, -87630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D37)

    Sleep(200)

    SetChrPos(0x0103, -35150, 0, -91730, 0)

    @scena.Lambda('lambda_0D68')
    def lambda_0D68():
        ChrWalkTo(0x00FE, -33970, 0, -87930, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0D68)

    Sleep(200)

    SetChrFlags(0x0102, 0x0004)
    SetChrPos(0x0102, -35150, 0, -91730, 0)

    @scena.Lambda('lambda_0D9E')
    def lambda_0D9E():
        ChrWalkTo(0x00FE, -36590, 0, -88240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D9E)

    Sleep(200)

    SetChrPos(0x0104, -35150, 0, -91730, 0)

    @scena.Lambda('lambda_0DCF')
    def lambda_0DCF():
        ChrWalkTo(0x00FE, -35260, 0, -89070, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0DCF)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0103, 0x0001)
    ClearChrFlags(0x0102, 0x0004)

    ChrTalk(
        0x0008,
        (
            '#0090031581V#213F你、你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpTo(0x0009, -37630, 0, -84940, 300, 3000)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)

    @scena.Lambda('lambda_0E42')
    def lambda_0E42():
        SetChrDirection(0x0009, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E42)

    ChrTalk(
        0x0009,
        (
            '#0290031582V#201F游击士！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031583V怎、怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031584V#035F呵呵……\n',
            '别说如此薄情的话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031585V不正是你们用那艘飞艇\n',
            '将我们送过来的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031586V#201F混、混帐……\n',
            '你在开什么玩笑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031587V…………难道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031588V#006F你们不记得\n',
            '在琥珀之塔前面停过飞艇吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031589V我们趁着空隙\n',
            '巧妙地藏到了船舱里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031590V#001F也就是偷渡啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031591V#214F很、很厉害嘛！\n',
            '你这个没大脑的女人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031592V#509F谁、谁没大脑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031593V你这个傲慢的男人婆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0090031594V#214F你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031595V单纯女！暴力女！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031596V#005F你、你竟敢这么说～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031597V#017F好了好了。\n',
            '求你们别再吵了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031598V#012F……人质已经被释放了，\n',
            '其他的空贼成员也都被打倒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031599V现在只剩下你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031600V#027F基于游击士协会的规定，\n',
            '现以协会的名义将你们逮捕归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031601V劝你们放弃无谓的抵抗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031602V#201F唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031603V#212F混蛋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11DD')
    def lambda_11DD():
        CameraMove(-34330, 0, -83800, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11DD)

    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0300031604V#193F#5P吉尔，乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031605V这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031606V#203F对、对不起，大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031607V#215F对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031608V#193F#5P哼，算了。\n',
            '这次就先饶了你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031609V只要把这些家伙\n',
            '通通杀光就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031610V#005F你、你说什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031611V#194F#5P嘎哈哈，愚蠢的家伙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031612V就凭你们几个人\n',
            '也想逮捕我多伦·卡普亚吗？\n',
            '你们也想得太美了吧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0004)
    ChrJumpTo(0x000A, -34360, 1000, -83540, 1500, 5000)
    PlaySE(142, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 6)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    @scena.Lambda('lambda_13B3')
    def lambda_13B3():
        CameraMove(-34220, 0, -85300, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_13B3)

    Sleep(1000)

    @scena.Lambda('lambda_13D0')
    def lambda_13D0():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13D0)

    Sleep(200)

    PlaySE(506, 0x00, 0x64)
    LoadEffect(0x02, 'map\\\\mp019_00.eff')
    SetChrPos(0x000C, -35030, 0, -87040, 0)
    PlayEffect(0x02, 0xFF, 0x000A, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    Sleep(1000)

    @scena.Lambda('lambda_1449')
    def lambda_1449():
        ChrJumpTo(0x00FE, -36180, 0, -88040, 500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1449)

    @scena.Lambda('lambda_1467')
    def lambda_1467():
        ChrJumpTo(0x00FE, -34210, 0, -88070, 500, 6000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1467)

    @scena.Lambda('lambda_1485')
    def lambda_1485():
        ChrJumpTo(0x00FE, -37290, 0, -89210, 500, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1485)

    @scena.Lambda('lambda_14A3')
    def lambda_14A3():
        ChrJumpTo(0x00FE, -33700, 0, -89380, 500, 6000)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_14A3)

    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp019_01.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, -35030, 0, -87040, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CameraSetDistance(3100, 0)
    CameraSetDistance(3000, 80)
    ChrTurnDirection(0x0103, 0x000A, 0)
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x0102, 0x0009, 0)
    ChrTurnDirection(0x0104, 0x000A, 0)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010031613V#504F呀啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031614V#016F轻型导力炮……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 225, 0)

    ChrTalk(
        0x000A,
        (
            '#0300031615V#195F#6P吉尔，乔丝特！\n',
            '快点给我上！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031616V把这些家伙炸成炮灰！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 180, 0)
    Sleep(100)

    SetChrChipByIndex(0x0008, 18)
    Sleep(100)

    SetChrChipByIndex(0x0009, 19)
    Sleep(500)

    SetChrChipByIndex(0x000A, 20)
    SetChrSubChip(0x000A, 0)

    @scena.Lambda('lambda_15FE')
    def lambda_15FE():
        ChrJumpTo(0x00FE, -35190, 0, -86950, 1500, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_15FE)

    Sleep(100)

    @scena.Lambda('lambda_1621')
    def lambda_1621():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1621)

    Sleep(100)

    @scena.Lambda('lambda_163B')
    def lambda_163B():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_163B)

    Sleep(200)

    Battle(0x00000389, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1668'),
        (-1, 'loc_166B'),
    )

    def _loc_1668(): pass

    label('loc_1668')

    OP_B4(0x00)

    Return()

    def _loc_166B(): pass

    label('loc_166B')

    EventBegin(0x00)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrChipByIndex(0x0008, 3)
    SetChrChipByIndex(0x0009, 4)
    SetChrChipByIndex(0x000A, 17)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0008, -36430, 0, -82700, 225)
    SetChrPos(0x0009, -38890, 0, -82380, 135)
    SetChrPos(0x000A, -37360, 0, -81500, 180)
    SetChrPos(0x0101, -38990, 0, -84930, 0)
    SetChrPos(0x0102, -38900, 0, -86070, 0)
    SetChrPos(0x0104, -37640, 0, -86250, 0)
    SetChrPos(0x0103, -37780, 0, -84870, 0)
    CameraMove(-37600, 0, -82870, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0290031617V#203F太、太强了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031618V这就是游击士的实力吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031619V#215F可、可恶～……\n',
            '竟然输给了这个女人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031620V#502F哼哼，这是当然的啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031621V#027F好了，胜负已分。\n',
            '你们老老实实地投降吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031622V#021F要是再敢抵抗的话，\n',
            '……后果你应该很明白的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德一边抽着鞭子一边向乔丝特微笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0090031623V#216F呀……\n',
            '不要，饶了我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031624V#203F呜呜……\n',
            '大势已去了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031625V………唔……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-37530, 0, -82040, 1000)
    OP_99(0x000A, 0x03, 0x00, 600)

    ChrTalk(
        0x000A,
        (
            '#0300031626V#197F痛痛痛……\n',
            '到底怎么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031627V身体到处都在疼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    SetChrChipByIndex(0x000A, 5)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0300031628V#192F我怎么……\n',
            '拿着这个导力炮啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031629V…………咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000A, 400)

    ChrTalk(
        0x0009,
        (
            '#0290031630V#201F大哥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0090031631V#212F多伦大哥？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031632V#191F哦哦，乔丝特！\n',
            '从洛连特回来了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031633V这么快就回来了，\n',
            '果然还是失手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031634V#213F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031635V#191F嘎哈哈，别想骗我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031636V算了，只要你能接受教训就行了。\n',
            '以后这些要蛮力的差事还是交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031637V虽然这样赚得少点，\n',
            '不过只要慢慢积累就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031638V#216F多、多伦大哥，你在说什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031639V#201F大哥，振作点！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031640V乔丝特她老早\n',
            '就从洛连特回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031641V袭击了定期船后，\n',
            '我不是还去迎接过你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031642V#192F啥？\n',
            '袭击定期船？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031643V老弟你在说什么梦话呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031644V那么危险的事，\n',
            '只有白痴才会去做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031645V#201F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031646V#213F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031647V#002F（这家伙在说什么呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031648V#012F（嗯……\n',
            '　不像是故意开脱罪行的样子……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031649V#190F刚才就注意到了，\n',
            '这些奇怪的家伙是谁啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031650V难道是新来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031651V#020F很遗憾不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031652V我们是游击士协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0300031653V#192F#5S啥！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031654V#192F为、为啥\n',
            '游击士会在这里的啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031655V#007F这么说……\n',
            '他好像突然失忆了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031656V#031F哈·哈·哈。\n',
            '看来剧情变得越来越有趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031657V#022F就算你突然失忆了，\n',
            '我们也还是要将你逮捕归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031658V抢夺定期船、监禁人质、\n',
            '要求赎金等案件都是既定的嫌疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2300, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0300031659V#192F抢夺定期船……\n',
            '监禁人质……要求赎金！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300031660V吉尔！乔丝特！\n',
            '这、这开的是啥玩笑呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031661V#215F多伦大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031662V#204F我们也想知道是怎么回事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031663V#201F不过，多亏了大哥，\n',
            '……这下有机会了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 21)
    SetChrDirection(0x0009, 180, 400)
    Sleep(200)

    OP_99(0x0009, 0x04, 0x05, 800)
    LoadEffect(0x00, 'map\\\\mp004_00.eff')
    SetChrPos(0x000C, -38180, -3000, -85370, 0)
    PlayEffect(0x00, 0xFF, 0x0009, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x000C, 0, 0, 0, 0)
    SetChrChipByIndex(0x0009, 1)
    Sleep(1300)

    PlaySE(127, 0x00, 0x64)
    FadeOut(500, 16777215, -1)
    OP_0D()
    SetChrPos(0x0009, -35240, 0, -89190, 0)
    SetChrPos(0x0008, -35240, 0, -89190, 0)
    SetChrPos(0x000A, -35240, 0, -89190, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010031664V#004F#1P啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031665V#024F#1P糟了！\n',
            '又是这招……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300031666V#192F喂、喂……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090031667V#213F吉尔哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031668V#201F有话以后再说吧！\n',
            '现在还是先逃为妙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031669V#034F#5P咳咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031670V呛、呛到烟了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031671V#016F#5P赶快离开这个房间！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    CameraMove(-35986, 0, -121600, 0)
    OP_6F(0x0000, 20)
    Sleep(500)

    FadeIn(1000, 16777215)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    CreateThread(0x0103, 0x01, 0x00, 0x0006)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010031672V#005F那些家伙～\n',
            '跑到哪里去了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031673V#016F在上面……\n',
            '他们打算坐空贼飞艇逃走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031674V#580F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031675V#024F#5P现在追还来得及，\n',
            '绝对不能再让他们逃掉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031676V全力追击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031677V#002F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031678V#012F明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x01, 0x00, 0x0007)
    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0104,
        (
            '#0040031679V#034F咳咳……救、救命……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031680V啊，真是悲剧！\n',
            '我精致完美的鼻腔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23D3')
    def lambda_23D3():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_23D3)

    @scena.Lambda('lambda_23E1')
    def lambda_23E1():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_23E1)

    ChrTurnDirection(0x0101, 0x0104, 400)
    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010031681V#005F喂，奥利维尔！\n',
            '再不快点就丢下你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0104,
        (
            '#0040031682V#036F哇哇……\n',
            '等、等一下嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x000005DC)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2493',
    )

    ChrWalkTo(0x0104, -36000, 0, -122180, 3000, 0x00)

    def _loc_2493(): pass

    label('loc_2493')

    SetScenaFlags(ScenaFlag(0x006B, 0, 0x358))
    OP_28(0x0039, 0x01, 0x0040)
    OP_28(0x0039, 0x01, 0x0080)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)
    OP_70(0x0000, 0)
    OP_71(0x0000, 0x0010)
    OP_64(0x00, 0x0001)
    OP_21()
    OP_1E()

    Jump('loc_24BE')

    def _loc_24BE(): pass

    label('loc_24BE')

    Return()

# id: 0x0004 offset: 0x24BF
@scena.Code('func_04_24BF')
def func_04_24BF():
    SetChrPos(0x00FE, -36050, 0, -119700, 0)
    ChrWalkTo(0x00FE, -36250, 0, -122380, 5000, 0x00)
    ChrWalkTo(0x00FE, -37200, 0, -123790, 5000, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    Sleep(200)

    SetChrDirection(0x00FE, 265, 400)
    Sleep(200)

    SetChrDirection(0x00FE, 180, 400)

    Return()

# id: 0x0005 offset: 0x2518
@scena.Code('func_05_2518')
def func_05_2518():
    Sleep(800)

    SetChrPos(0x00FE, -36050, 0, -119700, 0)
    ChrWalkTo(0x00FE, -36250, 0, -122380, 5000, 0x00)
    ChrWalkTo(0x00FE, -35450, 0, -123460, 5000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x255E
@scena.Code('func_06_255E')
def func_06_255E():
    Sleep(1600)

    SetChrPos(0x00FE, -36050, 0, -119700, 0)
    ChrWalkTo(0x00FE, -36250, 0, -122380, 5000, 0x00)

    Return()

# id: 0x0007 offset: 0x2589
@scena.Code('func_07_2589')
def func_07_2589():
    SetChrPos(0x00FE, -36050, 0, -119700, 0)
    ChrWalkTo(0x00FE, -35960, 0, -120920, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0x25AF
@scena.Code('func_08_25AF')
def func_08_25AF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 7, 0x357)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26EC',
    )

    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '道路的尽头是一面岩壁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010031530V#505F这里不能走了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031531V#012F不……\n',
            '前面好像有什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031532V试着推推看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【推岩壁】\n'),
            TXT(0x01, '【不推】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_26BF'),
        (0x00000001, 'loc_26CE'),
        (-1, 'loc_26EC'),
    )

    def _loc_26BF(): pass

    label('loc_26BF')

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C1401._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_26EC')

    def _loc_26CE(): pass

    label('loc_26CE')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_26EC')

    def _loc_26EC(): pass

    label('loc_26EC')

    Return()

# id: 0x0009 offset: 0x26ED
@scena.Code('func_09_26ED')
def func_09_26ED():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0070, 4, 0x384)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27D7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FC, 1)"),
            Expr.Return,
        ),
        'loc_2761',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0070, 4, 0x384))

    Jump('loc_27D4')

    def _loc_2761(): pass

    label('loc_2761')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_27D4(): pass

    label('loc_27D4')

    Jump('loc_280D')

    def _loc_27D7(): pass

    label('loc_27D7')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x0F)
    def _loc_280D(): pass

    label('loc_280D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
