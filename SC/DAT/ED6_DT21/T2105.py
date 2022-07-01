import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2105   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '怪盗布卢布兰'),
    TXT(0x02, '银发的青年'),
    TXT(0x03, '迪恩'),
    TXT(0x04, '雷斯'),
    TXT(0x05, '洛克'),
    TXT(0x06, '凯文神父'),
    TXT(0x07, '中型福音'),
    TXT(0x08, '阿伊纳街道方向'),
    TXT(0x09, '卢安市·北街区'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2105.x'
    header.mapIndex       = 1
    header.bgm            = 0
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1644
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
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH04530._CH', 'ED6_DT27/CH04530P._CP'),
        ('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH04087._CH', 'ED6_DT27/CH04087P._CP'),
        ('ED6_DT26/CH20243._CH', 'ED6_DT26/CH20243P._CP'),
        ('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP'),
        ('ED6_DT26/CH20283._CH', 'ED6_DT26/CH20283P._CP'),
        ('ED6_DT26/CH20278._CH', 'ED6_DT26/CH20278P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 73210,
            z                   = 0,
            y                   = -16650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 50980,
            z                   = 400,
            y                   = 77990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 31200,
            y           = 0,
            z           = 25340,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = 77280,
            y           = 0,
            z           = 22060,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x272
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x272
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    Return()

# id: 0x0001 offset: 0x280
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEA840, 0xFFFE7960, 0x00230048)
    OP_22(0x01C5, 0x00, 0x64)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x001F, 0x0004)

    Return()

# id: 0x0002 offset: 0x2C0
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0000, 23440, 7780, 1910, 0)
    SetChrPos(0x0001, 23440, 7780, 1910, 0)
    SetChrPos(0x0002, 23440, 7780, 1910, 0)
    SetChrPos(0x0003, 23440, 7780, 1910, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0040)
    SetChrPos(0x0008, 23460, 8800, 3630, 0)
    OP_6D(47110, 7780, 30010, 0)
    OP_67(0, 8050, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(31000, 0)
    OP_6E(505, 0)

    @scena.Lambda('lambda_037D')
    def lambda_037D():
        OP_6D(25710, 8800, 4920, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_037D)

    @scena.Lambda('lambda_0395')
    def lambda_0395():
        OP_67(0, 14180, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0395)

    @scena.Lambda('lambda_03AD')
    def lambda_03AD():
        OP_6C(142000, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_03AD)

    @scena.Lambda('lambda_03BD')
    def lambda_03BD():
        OP_6E(241, 9000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_03BD)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(8000)

    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0000, 0x02)
    TerminateThread(0x0000, 0x03)
    TerminateThread(0x0001, 0x01)
    Fade(1000)
    OP_6D(24530, 6120, 8189, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(487, 0)
    OP_0D()
    SetChrPos(0x0009, 31670, 7800, 110, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170220001V#231F──就这样宴会终于结束，\n',
            '留在热气中我们只有困惑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220002V苍凉的月影和跨海的凉风\n',
            '静静等待着灼热血潮的冷却……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0140220003V#1P……久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_050B')
    def lambda_050B():
        OP_6D(28050, 7800, 2290, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_050B)

    @scena.Lambda('lambda_0523')
    def lambda_0523():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0523)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0002)
    OP_8C(0x0008, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170220004V#231F#5P呵呵，时间刚刚好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220005V你还是那个守规矩的男人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220006V偶尔迟到一下\n',
            '也没什么关系吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05C6')
    def lambda_05C6():
        ChrTurnDirection(0x0008, 0x0009, 400)
        Yield()

        Jump('lambda_05C6')

    DispatchAsync2(0x0008, 0x0003, lambda_05C6)

    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)
    SetChrChipByIndex(0x0009, 9)
    SetChrSubChip(0x0009, 1)
    OP_99(0x0009, 0x01, 0x02, 0x000005DC)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_05F7')
    def lambda_05F7():
        OP_6D(23740, 7800, 1150, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_05F7)

    @scena.Lambda('lambda_060F')
    def lambda_060F():
        OP_67(0, 7500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_060F)

    @scena.Lambda('lambda_0627')
    def lambda_0627():
        OP_96(0x0009, 0x00005B5E, 0x00001E78, 0xFFFFFDDA, 0x000007D0, 0x00001770)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0627)

    WaitForThreadExit(0x0009, 0x0001)
    OP_7D(0x01, 0x0009, 0x0000, 0x0000)
    SetChrChipByIndex(0x0009, 1)
    SetChrSubChip(0x0009, 0)
    ChrTurnDirection(0x0009, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0140220007V#124F这是天性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220008V#120F事不宜迟\n',
            '赶快报告给我听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_96(0x0008, 0x00005B90, 0x00001E78, 0x000008AC, 0x00000064, 0x00001388)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170220009V#230F#5P哈哈，别那么着急嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220010V今晚心情多好。\n',
            '让我稍微沉浸一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220011V#123F哎呀哎呀……\n',
            '看来相当中意啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220012V#231F#5P唔，美丽的公主\n',
            '越发夺去了我的心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220013V而且在意外之处\n',
            '还遇到了美妙的好对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220014V#230F呵呵呵……\n',
            '看来就要忙起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220015V#124F真拿你没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220016V#120F个人兴趣倒也无妨，\n',
            '但记住别因为兴趣而妨碍计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220017V#230F#5P呵呵，这个不必担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220018V那么收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0008, 0x0009, 0x000003E8, 0x000007D0, 0x00)
    Fade(250)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 11)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    Fade(250)
    SetChrSubChip(0x0008, 8)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 23740, 7500, 400, 0)
    OP_0D()
    Sleep(1000)

    Fade(250)
    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 7)
    SetChrFlags(0x000E, 0x0080)
    OP_0D()
    OP_8F(0x0008, 23440, 7800, 1900, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0140220019V#124F……确认回收。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220020V#120F那……\n',
            '实验成果怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220021V#232F#5P唔，这个啊。\n',
            '可以说成功了九成左右吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220022V投影装置生出的映像\n',
            '能够传送到相当远的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220023V只不过，最初的１，２次\n',
            '传送好像失败了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220024V超过３次以后\n',
            '运作就变得完美了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220025V#123F唔……\n',
            '虽然有不稳定因素，但还不坏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220026V赶快传达给教授吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220027V#230F#5P不过这个『福音』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220028V导力停止现象已经\n',
            '远远超越了现在的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220029V好像是『十三工房』制造的，\n',
            '到底是个怎样的装置呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220030V#124F谁知道……\n',
            '我也不清楚详情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220031V#120F只是据教授所说，这些现象\n',
            '只不过是『奇迹』的冰山一角。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220032V#233F#5P噢、奇迹吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220033V#230F嗯……\n',
            '奇迹是只有女神才能做到的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220034V到底代表着什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220035V#123F无论如何，真正的潜力\n',
            '就用今后的实验来弄清楚吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140220036V这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0CD1')
    def lambda_0CD1():
        OP_8C(0x0009, 250, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CD1)

    WaitForThreadExit(0x0009, 0x0001)
    Fade(1000)
    OP_6D(22960, 7800, 30, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(306000, 0)
    OP_6E(487, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0140220037V#121F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220038V#233F噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 250, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170220039V#231F呵呵，今晚似乎\n',
            '有不少意外的登场人物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170220040V那么，剧本该怎么写呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140220041V#124F#6P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrFlags(0x0009, 0x0800)
    SetChrChipByIndex(0x0009, 3)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140220042V#123F#6P那就要看藏身于此\n',
            '的小老鼠的态度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170220043V#231F呵呵，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170220044V#231F好了……\n',
            '小老鼠会用怎样的声音叫出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, 29570, 0, 20890, 180)
    SetChrPos(0x000B, 30570, 0, 21930, 180)
    SetChrPos(0x000C, 28570, 0, 21930, 180)

    NpcTalk(
        0x000A,
        '醉了的声音',
        (
            '#0450220045V#1P#1S……呜咿～………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0F75')
    def lambda_0F75():
        OP_6D(23740, 7800, 2150, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0F75)

    @scena.Lambda('lambda_0F8D')
    def lambda_0F8D():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F8D)

    @scena.Lambda('lambda_0FA5')
    def lambda_0FA5():
        OP_6C(35000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0FA5)

    OP_8C(0x0009, 0, 400)
    Sleep(200)

    OP_8C(0x0008, 0, 400)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    WaitForThreadExit(0x000A, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0170220046V#230F#5P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(300)

    OP_8C(0x0008, 250, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0170220047V#231F#5P虽不知道是哪里的小老鼠，\n',
            '看来是捡回了条小命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 1)
    OP_0D()
    Sleep(300)

    OP_8C(0x0009, 250, 400)

    ChrTalk(
        0x0009,
        (
            '#0140220048V#121F#2P呵……\n',
            '感谢女神吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10BC')
    def lambda_10BC():
        OP_6D(23020, 7800, -6000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_10BC)

    @scena.Lambda('lambda_10D4')
    def lambda_10D4():
        OP_6C(75000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_10D4)

    Sleep(500)

    CreateThread(0x0009, 0x00, 0x00, 0x0003)
    OP_8C(0x0008, 180, 400)
    WaitForThreadExit(0x0009, 0x0000)
    CreateThread(0x0008, 0x00, 0x00, 0x0004)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_1112')
    def lambda_1112():
        OP_6D(29380, 0, 7350, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1112)

    @scena.Lambda('lambda_112A')
    def lambda_112A():
        OP_6C(108000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_112A)

    @scena.Lambda('lambda_113A')
    def lambda_113A():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_113A)

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_1161')
    def lambda_1161():
        OP_90(0x00FE, 0, 0, -14500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1161)

    Sleep(50)

    @scena.Lambda('lambda_1181')
    def lambda_1181():
        OP_90(0x00FE, 0, 0, -14000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1181)

    Sleep(50)

    OP_90(0x000C, 0, 0, -14500, 2000, 0x00)
    WaitForThreadExit(0x0009, 0x0002)
    OP_8C(0x000B, 46, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0470220049V#1751F#5P嘎哈哈、拿～酒来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 135, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0450220050V#1745F唔咕，不能再喝了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 300, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0460220051V#1764F可恶…\n',
            '我也是……我也是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_1271')
    def lambda_1271():
        OP_90(0x00FE, 10000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1271)

    OP_8C(0x000A, 90, 400)

    @scena.Lambda('lambda_1293')
    def lambda_1293():
        OP_90(0x00FE, 10000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1293)

    OP_8C(0x000C, 90, 400)

    @scena.Lambda('lambda_12B5')
    def lambda_12B5():
        OP_90(0x00FE, 10000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12B5)

    Sleep(1000)

    SetChrPos(0x000D, 9100, 0, 1600, 268)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0002)
    SetChrChipByIndex(0x000D, 8)
    SetChrSubChip(0x000D, 1)

    @scena.Lambda('lambda_12FA')
    def lambda_12FA():
        OP_6D(9700, 0, 1630, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_12FA)

    @scena.Lambda('lambda_1312')
    def lambda_1312():
        OP_67(0, 8000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1312)

    @scena.Lambda('lambda_132A')
    def lambda_132A():
        OP_6C(90000, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_132A)

    WaitForThreadExit(0x000D, 0x0000)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000D, 0x0002)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0180220052V#1068F#5P唉～……\n',
            '真是折寿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180220053V#1067F嘿，就算在心中祈祷也要\n',
            '拼命感谢女神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000D, 0x01, 0x09, 0x000005DC)
    Sleep(500)

    OP_22(0x00D5, 0x00, 0x64)
    ClearChrFlags(0x000D, 0x0002)
    SetChrChipByIndex(0x000D, 7)
    SetChrSubChip(0x000D, 0)

    @scena.Lambda('lambda_13DB')
    def lambda_13DB():
        OP_6D(10100, 0, 2440, 3500)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_13DB)

    @scena.Lambda('lambda_13F3')
    def lambda_13F3():
        OP_6C(225000, 3500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_13F3)

    OP_8C(0x000D, 0, 400)
    SetChrFlags(0x000D, 0x0004)
    OP_8E(0x000D, 9210, 0, 2500, 1000, 0x00)
    OP_8E(0x000D, 10620, 0, 2900, 1000, 0x00)
    WaitForThreadExit(0x000D, 0x0000)
    WaitForThreadExit(0x000D, 0x0002)

    ChrTalk(
        0x000D,
        (
            '#0180220054V#1063F#5P……不过…\n',
            '真都是些怪物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180220055V#1065F那些就是结社的『执行者』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_AD(0x002400A5, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    FadeOut(0, 0, -1)
    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    OP_A2(0x1400)
    OP_A2(0x10F6)
    NewScene('ED6_DT21/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x14FF
@scena.Code('func_03_14FF')
def func_03_14FF():
    OP_8C(0x0009, 180, 400)
    OP_8E(0x0009, 23300, 7800, -2270, 6000, 0x00)
    SetChrChipByIndex(0x0009, 9)
    SetChrSubChip(0x0009, 1)
    OP_96(0x0009, 0x00005BAE, 0x00002260, 0xFFFFF0B0, 0x000003E8, 0x00001770)
    OP_22(0x00A3, 0x00, 0x64)
    OP_7D(0x00, 0x0009, 0x0032, 0x01F4)
    SetChrSubChip(0x0009, 2)

    @scena.Lambda('lambda_1553')
    def lambda_1553():
        OP_96(0x0009, 0x00005A14, 0x00001F40, 0xFFFFCD38, 0x000003E8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1553)

    Sleep(200)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_157B')
    def lambda_157B():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_157B)

    Return()

# id: 0x0004 offset: 0x1588
@scena.Code('func_04_1588')
def func_04_1588():
    OP_8E(0x0008, 23300, 7800, -2270, 6000, 0x00)
    SetChrChipByIndex(0x0008, 10)
    SetChrSubChip(0x0008, 0)
    OP_96(0x0008, 0x00005BAE, 0x00002260, 0xFFFFF0B0, 0x000003E8, 0x00001770)
    OP_22(0x00A3, 0x00, 0x64)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_15D0')
    def lambda_15D0():
        OP_96(0x0008, 0x00005A14, 0x00001F40, 0xFFFFCD38, 0x000003E8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15D0)

    CreateThread(0x0008, 0x03, 0x00, 0x0005)
    Sleep(200)

    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_15FF')
    def lambda_15FF():
        OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_15FF)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)

    Return()

# id: 0x0005 offset: 0x1616
@scena.Code('func_05_1616')
def func_05_1616():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_162B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_05_1616')

    def _loc_162B(): pass

    label('loc_162B')

    Return()

# id: 0x0006 offset: 0x162C
@scena.Code('func_06_162C')
def func_06_162C():
    SetPlaceName(0x0069)

    Return()

# id: 0x0007 offset: 0x1630
@scena.Code('func_07_1630')
def func_07_1630():
    SetPlaceName(0x0052)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
