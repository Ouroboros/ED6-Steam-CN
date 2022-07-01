import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4202   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾莉茜雅女王'),
    TXT(0x02, '基库'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4202.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF32
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
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2090,
            triggerZ            = 12000,
            triggerY            = 67030,
            triggerRange        = 1000,
            actorX              = 5244,
            actorZ              = -10900,
            actorY              = 81768,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1920,
            triggerZ            = 12000,
            triggerY            = 58790,
            triggerRange        = 4700,
            actorX              = 1920,
            actorZ              = 12000,
            actorY              = 60790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x142
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_14C',
    )

    Jump('loc_173')

    def _loc_14C(): pass

    label('loc_14C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_156',
    )

    Jump('loc_173')

    def _loc_156(): pass

    label('loc_156')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_173',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 1800, 12000, 67020, 0)

    def _loc_173(): pass

    label('loc_173')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_17F'),
        (-1, 'loc_197'),
    )

    def _loc_17F(): pass

    label('loc_17F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 4, 0x1624)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_194',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    def _loc_194(): pass

    label('loc_194')

    Jump('loc_197')

    def _loc_197(): pass

    label('loc_197')

    Return()

# id: 0x0001 offset: 0x198
@scena.Code('Init')
def Init():
    OP_E8(0x88, 0x13, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B0',
    )

    OP_82(0x80, 0x00)
    OP_64(0x00, 0x0001)

    def _loc_1B0(): pass

    label('loc_1B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D6',
    )

    OP_B1('t4202_y')
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    Jump('loc_1DF')

    def _loc_1D6(): pass

    label('loc_1D6')

    OP_B1('t4202_n')

    def _loc_1DF(): pass

    label('loc_1DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EB',
    )

    OP_64(0x01, 0x0001)

    def _loc_1EB(): pass

    label('loc_1EB')

    Return()

# id: 0x0002 offset: 0x1EC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_201',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_201(): pass

    label('loc_201')

    Return()

# id: 0x0003 offset: 0x202
@scena.Code('func_03_202')
def func_03_202():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 1, 0x1651)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_747',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0630271333V#097F科洛蒂娅，还有\n',
            '艾丝蒂尔你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271334V#090F关于凯诺娜小姐的事\n',
            '我已经听尤莉亚报告了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271335V本来她的事\n',
            '是我应该应对的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271336V艾丝蒂尔小姐，还有诸位，\n',
            '给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271337V#1025F没、没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271338V#1000F而且玲……这次的罪犯\n',
            '也和我有关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630271339V#094F嗯，我听说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271340V#092F听说这么小的\n',
            '孩子也是结社的一员\n',
            '老实说我也很吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271341V她和巨大机器人的存在\n',
            '很可能招致市民的混乱，\n',
            '所以我想先封锁这一消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_45C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050271342V#050F虽然有点不舒服，\n',
            '不过还是这样比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A1')

    def _loc_45C(): pass

    label('loc_45C')

    ChrTalk(
        0x0103,
        (
            '#0030271343V#020F说实话，虽然\n',
            '有点不舒服，\n',
            '不过还是这样比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A1(): pass

    label('loc_4A1')

    ChrTalk(
        0x0105,
        (
            '#0060271344V#042F嗯，稍有不慎\n',
            '也有可能引发\n',
            '大的国际影响……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271345V#1004F这、这么严重啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271346V#1009F果然下次见到玲\n',
            '一定要严肃教育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630271347V#094F对他们的搜查就交给\n',
            '摩尔根将军和卡西乌斯先生吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271348V我也要以我的方式\n',
            '我们要尽自己所能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271349V#090F当前我们必须保证\n',
            '签字仪式的顺利进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271350V#1000F女王陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630271351V#090F艾丝蒂尔，你的担子\n',
            '也不轻，请努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271352V#1018F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#0630271353V#094F另外……科洛蒂娅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271354V#040F……在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630271355V#090F我期待着你不久之后\n',
            '会给出的答案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271356V#042F是，祖母大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630271357V#090F那么各位请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1651)

    Jump('loc_7B6')

    def _loc_747(): pass

    label('loc_747')

    ChrTalk(
        0x0008,
        (
            '#0630271358V#090F艾丝蒂尔小姐的担子\n',
            '虽然辛苦，也请你们多多努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630271359V科洛蒂娅就拜托\n',
            '你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7B6(): pass

    label('loc_7B6')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x7BA
@scena.Code('func_04_7BA')
def func_04_7BA():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 2000, 12000, 67000, 180)
    SetChrPos(0x0009, 1110, 12500, 67800, 180)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    OP_6D(2480, 12000, 54000, 0)
    OP_67(0, 10780, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    CreateThread(0x0101, 0x01, 0x00, 0x0005)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, 0x0006)
    Sleep(300)

    CreateThread(0x0108, 0x01, 0x00, 0x0008)
    Sleep(100)

    CreateThread(0x0104, 0x01, 0x00, 0x0007)
    FadeIn(2000, 0)
    WaitForThreadExit(0x0108, 0x0001)
    OP_0D()

    NpcTalk(
        0x0008,
        '老年妇女的声音',
        (
            '#0630250938V呵呵……\n',
            '终于来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250939V#1004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250940V#044F#6P祖母大人……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08F9')
    def lambda_08F9():
        OP_6D(2130, 12000, 66280, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08F9)

    @scena.Lambda('lambda_0911')
    def lambda_0911():
        OP_67(0, 6260, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0911)

    @scena.Lambda('lambda_0929')
    def lambda_0929():
        OP_6B(2610, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0929)

    @scena.Lambda('lambda_0939')
    def lambda_0939():
        OP_6E(279, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_0939)

    Sleep(1500)

    CreateThread(0x0101, 0x00, 0x00, 0x0009)
    Sleep(200)

    CreateThread(0x0105, 0x00, 0x00, 0x000A)
    Sleep(300)

    CreateThread(0x0108, 0x00, 0x00, 0x000C)
    Sleep(100)

    CreateThread(0x0104, 0x00, 0x00, 0x000B)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0440250941V#311F#1P啾～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250942V#1004F#4P咦？基库？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250943V#047F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250944V#048F呵呵，基库知道\n',
            '我们来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250945V#091F#5P嗯，是它告诉我\n',
            '你们来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250946V#090F欢迎回来，科洛蒂娅。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250947V还有艾丝蒂尔小姐……\n',
            '谢谢你们能来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250948V#094F情况我已经从卡西乌斯\n',
            '先生那里听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250949V真是……发生了不少事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250950V#1026F#4P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250951V#1016F嘿嘿，非常感谢您\n',
            '对我们的担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250952V#1006F不过我也找到了前进方向，\n',
            '科洛丝她们也帮了不少忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250953V所以，我没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250954V#094F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250955V#090F呵呵，一段时间不见，\n',
            '你真是变得可靠了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250956V也欢迎奥利维尔先生\n',
            '和金先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250957V#091F请回房间吧。\n',
            '红茶已经准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4230._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xC8B
@scena.Code('func_05_C8B')
def func_05_C8B():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 2740, 12000, 49900, 0)

    @scena.Lambda('lambda_0CA7')
    def lambda_0CA7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0CA7)

    OP_8E(0x00FE, 2620, 12000, 54000, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0xCC8
@scena.Code('func_06_CC8')
def func_06_CC8():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1630, 12000, 49890, 0)

    @scena.Lambda('lambda_0CE4')
    def lambda_0CE4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0CE4)

    OP_8E(0x00FE, 1630, 12000, 54000, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0xD05
@scena.Code('func_07_D05')
def func_07_D05():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 1650, 12000, 49050, 0)

    @scena.Lambda('lambda_0D21')
    def lambda_0D21():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D21)

    OP_8E(0x00FE, 1590, 12000, 52900, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0xD42
@scena.Code('func_08_D42')
def func_08_D42():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 2730, 12000, 49060, 0)

    @scena.Lambda('lambda_0D5E')
    def lambda_0D5E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D5E)

    OP_8E(0x00FE, 2620, 12000, 52900, 2000, 0x00)

    Return()

# id: 0x0009 offset: 0xD7F
@scena.Code('func_09_D7F')
def func_09_D7F():
    OP_8E(0x00FE, 2500, 12000, 65099, 3000, 0x00)

    Return()

# id: 0x000A offset: 0xD94
@scena.Code('func_0A_D94')
def func_0A_D94():
    OP_8E(0x00FE, 1320, 12000, 65099, 3000, 0x00)

    Return()

# id: 0x000B offset: 0xDA9
@scena.Code('func_0B_DA9')
def func_0B_DA9():
    OP_8E(0x00FE, 1240, 12000, 63730, 3000, 0x00)

    Return()

# id: 0x000C offset: 0xDBE
@scena.Code('func_0C_DBE')
def func_0C_DBE():
    OP_8E(0x00FE, 2450, 12000, 63690, 3000, 0x00)

    Return()

# id: 0x000D offset: 0xDD3
@scena.Code('func_0D_DD3')
def func_0D_DD3():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E0B')
    def lambda_0E0B():
        OP_6D(-2750, 12000, 67810, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E0B)

    @scena.Lambda('lambda_0E23')
    def lambda_0E23():
        OP_6B(3000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0E23)

    @scena.Lambda('lambda_0E33')
    def lambda_0E33():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0E33)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EBA',
    )

    OP_C0(0x0E, 0x0000002E, 0x00000852, 0x00002EE0, 0x000105D6, 0x00000168, 0x0000147C, 0xFFFFD56C, 0x00013F68)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_EC9')

    def _loc_EBA(): pass

    label('loc_EBA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC9',
    )

    EventEnd(0x01)

    def _loc_EC9(): pass

    label('loc_EC9')

    Return()

# id: 0x000E offset: 0xECA
@scena.Code('func_0E_ECA')
def func_0E_ECA():
    OP_8C(0x0000, 0, 0)
    OP_8C(0x0001, 0, 0)
    OP_8C(0x0002, 0, 0)
    OP_8C(0x0003, 0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x002400CE, 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    OP_A2(0x20EA)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
