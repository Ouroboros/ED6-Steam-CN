import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3102.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH02450._CH', 'ED6_DT07/CH02450P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希德少校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1B2
@scena.Code('Init')
def Init():
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_22E)

    Return()

# id: 0x0001 offset: 0x1BA
@scena.Code('func_01_1BA')
def func_01_1BA():
    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CE',
    )

    OP_28(0x002A, 0x01, 0x4000)

    def _loc_1CE(): pass

    label('loc_1CE')

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x218
@scena.Code('func_02_218')
def func_02_218():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_22D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_218')

    def _loc_22D(): pass

    label('loc_22D')

    Return()

# id: 0x0003 offset: 0x22E
@scena.Code('func_03_22E')
def func_03_22E():
    SetScenaFlags(ScenaFlag(0x00AC, 4, 0x564))
    OP_28(0x0044, 0x01, 0x0002)
    EventBegin(0x00)
    ChrSetPos(0x0008, -15700, 0, 24380, 90)
    ChrSetPos(0x000A, -14780, 0, 25510, 90)
    ChrSetPos(0x000B, -16670, 0, 25510, 90)
    ChrSetPos(0x000C, -14880, 0, 26880, 90)
    ChrSetPos(0x000D, -16680, 0, 27080, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    OP_12(0x0000AFC8, 0x0003D090, 0x00000000)
    OP_13(0x008C)
    CameraMove(-950, 0, 52320, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4460, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_02FA')
    def lambda_02FA():
        OP_6C(50000, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_02FA)

    FadeIn(2000, 0)
    OP_0D()
    CameraMove(-6420, 0, 24580, 6000)
    Fade(1000)
    CameraMove(-4770, 0, 24600, 0)
    CameraSetDistance(3250, 0)
    OP_6C(54000, 0)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, 0, 0, 0, 0)
    ChrSetPos(0x0102, 0, 0, 0, 0)
    ChrSetPos(0x0107, 0, 0, 0, 0)
    ChrSetPos(0x0106, 0, 0, 0, 0)
    ChrSetBattleFlags(0x0009, 0x0020)
    OP_89(0x0009, -2180, 2300, 22900, 270)
    OP_4A(0x0008, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)

    @scena.Lambda('lambda_03CF')
    def lambda_03CF():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_03CF')

    DispatchAsync2(0x0008, 0x0001, lambda_03CF)

    @scena.Lambda('lambda_03E0')
    def lambda_03E0():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_03E0')

    DispatchAsync2(0x000A, 0x0001, lambda_03E0)

    @scena.Lambda('lambda_03F1')
    def lambda_03F1():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_03F1')

    DispatchAsync2(0x000B, 0x0001, lambda_03F1)

    @scena.Lambda('lambda_0402')
    def lambda_0402():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_0402')

    DispatchAsync2(0x000C, 0x0001, lambda_0402)

    @scena.Lambda('lambda_0413')
    def lambda_0413():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_0413')

    DispatchAsync2(0x000D, 0x0001, lambda_0413)

    OP_12(0x0000AFC8, 0x0001FBD0, 0x00000000)
    Sleep(500)

    @scena.Lambda('lambda_0436')
    def lambda_0436():
        CameraMove(-15630, 0, 24380, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0436)

    ChrWalkTo(0x0009, -14950, 0, 23030, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0560090824V#691F哟，希德少校。\n',
            '你们订的货物到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090825V#701F啊，格斯塔夫维修长。\n',
            '要你特地来一趟真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090826V不过，\n',
            '真没想到这么快就能送到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090827V#691F王国军是老主顾嘛，\n',
            '服务质量当然要做好点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090828V话说回来，\n',
            '这次你们要得还真是急哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090829V还有之前警备飞艇的维修，\n',
            '难道发生什么事件了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090830V#702F不，没有……\n',
            '不过军队里也有各种事嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090831V对了……\n',
            '关于中央工房的袭击事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090832V我们刚刚得到了重要的线索，\n',
            '估计近期内就会解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090833V#690F哦哦……那真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090834V被绑架的拉赛尔老爷子\n',
            '可是我的大恩人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090835V希望他不要受什么伤就好了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090836V#701F嗯，那倒不至于……\n',
            '总之请你们中央工房放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090837V#692F哦，知道些什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090838V#703F据说袭击犯把博士挟为人质，\n',
            '想必他们打算要求赎金……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090839V我们已经确认他现在平安无事，\n',
            '你们就先安心等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090840V#691F原来如此啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090841V嗯，好的。\n',
            '交给王国军就没什么好担心的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    ChrSetDirection(0x0009, 45, 400)

    ChrTalk(
        0x0009,
        (
            '#0560090842V#691F那么这次也要检查集装箱吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090843V#701F虽然很信得过你们，\n',
            '但我们也必须例行公事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090844V#702F你们快点开始检查！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2500090845V明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        ChrWalkTo(0x00FE, -13820, 0, 30790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0924)

    ChrTalk(
        0x000C,
        (
            '#2440090846V明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0959')
    def lambda_0959():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0959')

    DispatchAsync2(0x0008, 0x0001, lambda_0959)

    @scena.Lambda('lambda_096A')
    def lambda_096A():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_096A')

    DispatchAsync2(0x000A, 0x0001, lambda_096A)

    @scena.Lambda('lambda_097B')
    def lambda_097B():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_097B')

    DispatchAsync2(0x000B, 0x0001, lambda_097B)

    @scena.Lambda('lambda_098C')
    def lambda_098C():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_098C')

    DispatchAsync2(0x0009, 0x0001, lambda_098C)

    @scena.Lambda('lambda_099D')
    def lambda_099D():
        CameraMove(-9060, 0, 23330, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_099D)

    @scena.Lambda('lambda_09B5')
    def lambda_09B5():
        CameraSetDistance(4710, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09B5)

    @scena.Lambda('lambda_09C5')
    def lambda_09C5():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09C5)

    ChrWalkTo(0x000C, -14050, 0, 25820, 4000, 0x00)

    @scena.Lambda('lambda_09E9')
    def lambda_09E9():
        ChrWalkTo(0x00FE, -13470, 0, 16600, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_09E9)

    WaitForThreadExit(0x000D, 0x0001)
    ChrSetDirection(0x000D, 90, 0)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)

    ChrTalk(
        0x000D,
        (
            '#2500090847V无异常。下一个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x00, func_04_1413)
    ChrSetDirection(0x000C, 90, 0)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2440090848V……ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x01, 0x00, func_05_1547)
    WaitForThreadExit(0x000D, 0x0001)
    PlaySE(171, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    @scena.Lambda('lambda_0A9F')
    def lambda_0A9F():
        CameraMove(-12400, 0, 26810, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A9F)

    @scena.Lambda('lambda_0AB7')
    def lambda_0AB7():
        CameraSetDistance(3250, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0AB7)

    @scena.Lambda('lambda_0AC7')
    def lambda_0AC7():
        OP_6C(62000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0AC7)

    ChrTalk(
        0x000D,
        (
            '#2500090849V感应器有动静！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2500090850V是生命反应！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0620090851V#702F什么……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090852V维修长……这是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090853V#692F喂，喂喂。\n',
            '我可什么都不知道哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090854V是不是装置出了故障啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090855V#703F这怎么可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090856V这可是为王国军特制的生命感应器，\n',
            '中央工房发明的东西应该不会出问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090857V#691F也许是是老鼠什么的吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090858V用不着那么紧张啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090859V#703F……我们也是例行公事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090860V#704F你们几个！\n',
            '把集装箱包围起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, -9980, 0, 18170, 0)
    ChrSetPos(0x000E, -12260, 0, 26290, 180)

    @scena.Lambda('lambda_0D12')
    def lambda_0D12():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D12')

    DispatchAsync2(0x000A, 0x0001, lambda_0D12)

    @scena.Lambda('lambda_0D23')
    def lambda_0D23():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D23')

    DispatchAsync2(0x000B, 0x0001, lambda_0D23)

    @scena.Lambda('lambda_0D34')
    def lambda_0D34():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D34')

    DispatchAsync2(0x000C, 0x0001, lambda_0D34)

    @scena.Lambda('lambda_0D45')
    def lambda_0D45():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D45')

    DispatchAsync2(0x000D, 0x0001, lambda_0D45)

    @scena.Lambda('lambda_0D56')
    def lambda_0D56():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D56')

    DispatchAsync2(0x0008, 0x0001, lambda_0D56)

    @scena.Lambda('lambda_0D67')
    def lambda_0D67():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0D67')

    DispatchAsync2(0x0009, 0x0001, lambda_0D67)

    ChrSetChipByIndex(0x000A, 4)
    ChrSetChipByIndex(0x000B, 4)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x000D, 4)

    @scena.Lambda('lambda_0D8C')
    def lambda_0D8C():
        ChrWalkTo(0x000C, -10470, 0, 24420, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0D8C)

    @scena.Lambda('lambda_0DA7')
    def lambda_0DA7():
        ChrWalkTo(0x000A, -11780, 0, 22820, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0DA7)

    @scena.Lambda('lambda_0DC2')
    def lambda_0DC2():
        ChrWalkTo(0x000B, -14520, 0, 23930, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0DC2)

    @scena.Lambda('lambda_0DDD')
    def lambda_0DDD():
        ChrWalkTo(0x0008, -12990, 0, 22250, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0DDD)

    @scena.Lambda('lambda_0DF8')
    def lambda_0DF8():
        ChrMoveTo(0x0009, -15760, 0, 22230, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0DF8)

    ChrWalkTo(0x000D, -14040, 0, 29210, 4000, 0x00)
    ChrWalkTo(0x000D, -14320, 0, 24870, 4000, 0x00)
    ChrTurnDirection(0x000D, 0x000E, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090861V#700F好……打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000E, 0x0080)
    OP_72(0x0002, 0x0010)
    PlaySE(168, 0x00, 0x64)
    OP_B0(0x0002, 0x78)
    OP_70(0x0002, 120)
    CameraMove(-12850, 0, 23990, 1000)
    OP_73(0x0002)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0620090862V#702F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000E, -12480, 0, 24280, 1000, 0x00)
    ChrTurnDirection(0x000E, 0x000D, 600)
    ChrTurnDirection(0x000E, 0x000C, 600)
    ChrTurnDirection(0x000E, 0x0008, 600)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    Sleep(500)

    ChrWalkTo(0x0009, -13780, 0, 23070, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0560090863V#692F怎么，是安东尼啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090864V你什么时候躲到这里面来了？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000E,
        (
            '#2030090865V喵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090866V#702F这、这只猫是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090867V#691F这家伙叫安东尼，\n',
            '是中央工房养的小猫咪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090868V看来这家伙不小心跑到\n',
            '『莱普尼兹号』上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090869V#703F真是吓了我们一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090870V#701F喂，你啊。\n',
            '还真会引起骚动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0008, 400)

    ChrTalk(
        0x000E,
        (
            '#2030090871V喵呵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0620090872V#701F算了，猫本来就喜怒无常的，\n',
            '跟它说道理也听不懂的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620090873V你要是喜欢的话，\n',
            '以后就干脆住在这里算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0560090874V#692F喂喂。\n',
            '请不要诱惑安东尼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2030090875V呜咪～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2030090876V……喵呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetBattleFlags(0x000E, 0x0020)
    ChrWalkTo(0x000E, -8920, 0, 23030, 5000, 0x00)
    ChrWalkTo(0x000E, -2180, 2300, 22900, 5000, 0x00)
    ChrSetFlags(0x000E, 0x0080)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0009, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0620090877V#703F唔唔……看来我被甩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000A, 2)
    ChrSetChipByIndex(0x000B, 2)
    ChrSetChipByIndex(0x000C, 2)
    ChrSetChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_1278')
    def lambda_1278():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1278)

    @scena.Lambda('lambda_1286')
    def lambda_1286():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1286)

    @scena.Lambda('lambda_1294')
    def lambda_1294():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1294)

    @scena.Lambda('lambda_12A2')
    def lambda_12A2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_12A2)

    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0560090878V#693F哈哈，真可惜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090879V#691F不过话说回来，\n',
            '这个生命感应器还真是厉害的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090880V安东尼差点就这样一直被关着了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090881V#701F啊，的确是啊。\n',
            '真不愧是中央工房发明的机器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000C, 400)

    ChrTalk(
        0x0008,
        (
            '#0620090882V#700F……你们几个。\n',
            '把剩下的集装箱也检查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2440090883V明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    MapSetFlags(0x40000000)
    NewScene('ED6_DT01/C3106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x1413
@scena.Code('func_04_1413')
def func_04_1413():
    ChrWalkTo(0x000D, -14060, 0, 29520, 3000, 0x00)
    ChrWalkTo(0x000D, -12170, 0, 29470, 3000, 0x00)
    ChrWalkTo(0x000D, -12150, 0, 29770, 3000, 0x00)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    Sleep(500)

    ChrMoveTo(0x000D, -12170, 0, 29470, 2000, 0x00)
    ChrWalkTo(0x000D, -9920, 0, 29550, 3000, 0x00)
    ChrWalkTo(0x000D, -9920, 0, 29770, 3000, 0x00)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    Sleep(500)

    ChrMoveTo(0x000D, -9920, 0, 29550, 2000, 0x00)
    ChrWalkTo(0x000D, -8200, 0, 29550, 3000, 0x00)
    ChrWalkTo(0x000D, -8200, 0, 33640, 3000, 0x00)
    ChrSetDirection(0x000D, 270, 400)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    Sleep(500)

    ChrWalkTo(0x000D, -8200, 0, 29500, 3000, 0x00)
    ChrWalkTo(0x000D, -12540, 0, 29500, 3000, 0x00)
    ChrWalkTo(0x000D, -12540, 0, 29130, 3000, 0x00)
    Sleep(500)

    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    Return()

# id: 0x0005 offset: 0x1547
@scena.Code('func_05_1547')
def func_05_1547():
    ChrWalkTo(0x000C, -13450, 0, 16720, 3000, 0x00)
    ChrSetDirection(0x000C, 90, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    ChrWalkTo(0x000C, -13450, 0, 14300, 3000, 0x00)
    ChrSetDirection(0x000C, 90, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    ChrWalkTo(0x000C, -13450, 0, 11980, 3000, 0x00)
    ChrSetDirection(0x000C, 90, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    ChrWalkTo(0x000C, -13450, 0, 9980, 4000, 0x00)
    ChrWalkTo(0x000C, -10960, 0, 7480, 6000, 0x00)
    ChrWalkTo(0x000C, -8740, 0, 7480, 6000, 0x00)
    ChrWalkTo(0x000C, -6800, 0, 9670, 6000, 0x00)
    ChrWalkTo(0x000C, -6800, 0, 11880, 4000, 0x00)
    ChrSetDirection(0x000C, 270, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    ChrWalkTo(0x000C, -6800, 0, 15050, 4000, 0x00)
    ChrSetDirection(0x000C, 270, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    ChrWalkTo(0x000C, -6800, 0, 18080, 4000, 0x00)
    ChrSetDirection(0x000C, 270, 400)
    Sleep(400)

    PlaySE(170, 0x00, 0x64)
    Sleep(400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
