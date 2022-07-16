import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0011_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0011   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '摩尔根将军'),
    TXT(0x02, '王国军士兵Ａ'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0011.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1BD4
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
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -7752,
            z                   = -2000,
            y                   = 4527,
            direction           = 270,
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
            x                   = -7116,
            z                   = -2000,
            y                   = -197,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
    )

# id: 0x0000 offset: 0xFA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 5, 0x325)),
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 4, 0x324)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 3, 0x323)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 0, 0x328)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_115',
    )

    SetScenaFlags(ScenaFlag(0x0065, 0, 0x328))
    Event(0, 0x0003)

    def _loc_115(): pass

    label('loc_115')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_123',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0005)

    def _loc_123(): pass

    label('loc_123')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_12F'),
        (-1, 'loc_145'),
    )

    def _loc_12F(): pass

    label('loc_12F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 0, 0x328)),
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 1, 0x329)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_142',
    )

    SetScenaFlags(ScenaFlag(0x0065, 1, 0x329))
    Event(0, 0x0004)

    def _loc_142(): pass

    label('loc_142')

    Jump('loc_145')

    def _loc_145(): pass

    label('loc_145')

    Return()

# id: 0x0001 offset: 0x146
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x147
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_15C(): pass

    label('loc_15C')

    Return()

# id: 0x0003 offset: 0x15D
@scena.Code('func_03_15D')
def func_03_15D():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(1000, 5000, -3500, 0)
    SetChrPos(0x0101, 1000, 5000, -3590, 225)
    SetChrPos(0x0102, -360, 5000, -3840, 135)
    SetChrPos(0x0103, 730, 5000, -4940, 315)

    ChrTalk(
        0x0101,
        (
            '#002F虽然已经调查了一遍，\n',
            '可是一个人也没有发现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F看样子乘客被空贼用空贼飞艇\n',
            '用空贼飞艇带走的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……大概，是到他们的据点去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021848V好不容易\n',
            '才找到的线索就这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021849V#020F好了好了。\n',
            '不要这么愁眉苦脸的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021850V现在并不是\n',
            '一点线索都没有哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们想想，为什么那帮家伙\n',
            '会把定期船藏在这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F正如刚才所见，\n',
            '定期船内的导力完全停止了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这也就意味着，\n',
            '导力引擎被他们拿走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而那些家伙多次\n',
            '来回运送大量的货物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021857V考虑这样做所花费的时间和带来的风险，\n',
            '用定期船把货物运往自己的据点\n',
            '效率反倒应该高得多吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021859V那么，空贼把定期船\n',
            '藏在这个地方的原因就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '仔细考虑一下的话……',
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
            TXT(0x00, '【为了挑选货物】\n'),
            TXT(0x01, '【为了把人质转移到空贼飞艇上】\n'),
            TXT(0x02, '【为了抢夺导力引擎】\n'),
            TXT(0x03, '【为了逃避王国军的搜捕】\n'),
            TXT(0x04, '【因为据点在特殊的地方】\n'),
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
        (0x00000000, 'loc_534'),
        (0x00000001, 'loc_5A7'),
        (0x00000002, 'loc_623'),
        (0x00000003, 'loc_696'),
        (0x00000004, 'loc_73B'),
        (-1, 'loc_75B'),
    )

    def _loc_534(): pass

    label('loc_534')

    ChrTalk(
        0x0103,
        (
            '#0030021861V#026F确实，这里比较宽阔，\n',
            '挑选货物时也许很方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B')

    def _loc_5A7(): pass

    label('loc_5A7')

    ChrTalk(
        0x0103,
        (
            '#026F确实，在把人质转移到空贼飞艇上的过程中，\n',
            '定期船必须要着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B')

    def _loc_623(): pass

    label('loc_623')

    ChrTalk(
        0x0103,
        (
            '#0030021865V#026F确实，要把引擎拔除的话，\n',
            '定期船必须要着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B')

    def _loc_696(): pass

    label('loc_696')

    ChrTalk(
        0x0103,
        (
            '#0030021867V#026F确实，定期船很大，\n',
            '很容易会被王国军发现……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以把它藏在据点以外的\n',
            '据点以外的场所的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021869V但是，这个解释\n',
            '也不能说是决定性的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B')

    def _loc_73B(): pass

    label('loc_73B')

    ChrTalk(
        0x0103,
        (
            '#020F对，就是因为这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75B')

    def _loc_75B(): pass

    label('loc_75B')

    ChrTalk(
        0x0103,
        (
            '#0030021871V#020F根据我的推测，\n',
            '他们的据点应该是个地形特殊的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021872V１０～１５亚矩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也就是说只能让空贼飞艇\n',
            '这种小型艇降落的特殊场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F原、原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F像山峦、峡谷这样\n',
            '高低差很大的复杂地形……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '应该是最值得怀疑的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F对，我也这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果真是那样的话……\n',
            '那真是超出我们能力范围了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021879V他们的据点很有可能\n',
            '是在步行所涉足不到的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F怎、怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#022F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021882V虽然让人失望，但现在唯有\n',
            '向军队说明情况并请求他们协助了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '毕竟他们拥有军用飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎～……\n',
            '搞了半天还是要依靠军队啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F这艘定期船的事情\n',
            '最后肯定要报告给军队的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021886V不管他们的态度怎么样，\n',
            '我认为现在还是合作比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021887V这也是为了早点解放人质啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021889V现在不是任性的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021890V#020F总之，我们先回游击士协会\n',
            '向卢格兰爷爷汇报一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021891V使用协会的导力通信器，\n',
            '就可以和哈肯大门联络了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xADA
@scena.Code('func_04_ADA')
def func_04_ADA():
    EventBegin(0x00)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#004F哎、哎哎～～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这、这是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F哈……\n',
            '这真是意料之外的来者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F唔，看来这次\n',
            '连联络的功夫也省了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '发现一干\n',
            '手持武器的嫌疑犯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们！\n',
            '老实举起手来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是世态炎凉啊，\n',
            '连小女孩也做起空贼来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F谁、谁是空贼啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021900V没看到我身上的徽章吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '哼，游击士的徽章吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '凭这种东西\n',
            '就能证明自身的清白？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021903V#004F摩、摩尔根将军！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021904V#014F为什么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#160F根据各部队的报告，\n',
            '这里尚未进行细致的搜查。\n',
            '我们来这里也是理所当然的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是，万万没想到\n',
            '你们竟然和空贼勾结。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021907V#022F在没有真凭实据之前，\n',
            '请不要这样随意下结论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021908V我们只是先你们一步\n',
            '到这里做现场调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#160F那么空贼在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021910V船内的乘客又在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F只差一步就能抓住那些空贼了，\n',
            '这是我们的疏忽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021912V作为人质的乘客也不在定期船里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#160F哼，真是不打自招……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '原来在我们到来之前，\n',
            '你们已经向空贼通风报信了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021915V#005F等、等一下！\n',
            '你这样说实在是太过分了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#162F这是我该讲的台词！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '来人！\n',
            '把这三个嫌疑犯抓起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T1410._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xF0D
@scena.Code('func_05_F0D')
def func_05_F0D():
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-2670, 5000, -10370, 0)
    OP_6C(315000, 0)
    CameraSetDistance(2400, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x0104, 0, 5000, -10200, 180)
    SetChrPos(0x0103, 0, 5000, -1650, 180)
    FadeIn(2000, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('青年的声音')

    Talk(
        (
            '#0041050006V',
            (TxtCtl.SetColor, 0x0),
            '……以上就是\n',
            '在王国北部发生的空贼事件的始末。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040002V',
            (TxtCtl.SetColor, 0x0),
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040003V',
            (TxtCtl.SetColor, 0x0),
            '是啊……没想到没落的\n',
            '卡普亚家族子孙竟会沦落到如此田地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040004V',
            (TxtCtl.SetColor, 0x0),
            '对了，如果王国方面问起这件事，\n',
            '你可要帮我做一下适当的应对哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040005V',
            (TxtCtl.SetColor, 0x0),
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040006V',
            (TxtCtl.SetColor, 0x0),
            '嗯，结果还是没有遇上他。\n',
            '也许是因为发生了什么麻烦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040007V',
            (TxtCtl.SetColor, 0x0),
            '现在还不能确定这和空贼事件有没有关联，\n',
            '不过肯定的是有其他势力在暗中活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            '#0040040008V',
            (TxtCtl.SetColor, 0x0),
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '呵呵，才不是。\n',
            '我也认识了一些有趣的朋友啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '这里料理美味，美人又多。\n',
            '简直就是我梦寐以求的国度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '真想一辈子住在这里啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '知道啦，知道啦。\n',
            '拜托你不要发出那么吓人的声音嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '好的，那边就继续拜托你了，\n',
            '别忘了代我向宰相大人问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '下次再联络吧，我的好友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#030F呵呵，还是老样子，\n',
            '总是大惊小怪的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040016V做事一点也不通融，\n',
            '这该说是可爱呢还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0103,
        '女性的声音',
        (
            '……是携带用的小型通信器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0103,
        '女性的声音',
        (
            '就这么带在身边到处走，\n',
            '也太过显眼了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0104, 0x0103, 500)

    @scena.Lambda('lambda_138D')
    def lambda_138D():
        CameraSetDistance(3000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_138D)

    CameraMove(-190, 5000, -6110, 1000)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#030F雪……雪拉君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13CC')
    def lambda_13CC():
        CameraMove(100, 5000, -9000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13CC)

    ChrWalkTo(0x0103, 0, 5000, -7870, 2000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#020F不过没想到的是，\n',
            '你竟然会有中央工房\n',
            '还未实用化的导力通信器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你，到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040040022V#030F讨厌啦，干嘛跟人家这么见外～\n',
            '下次再这样说人家可不依哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040023V漂泊的诗人和天才演奏家——\n',
            '奥利维尔·朗海姆。\n',
            '你不是应该很清楚吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，如果想知道得更多的话，\n',
            '那就只能以枕边话的形式来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F很遗憾，\n',
            '你这种小丑戏对我来说是不管用的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040026V埃雷波尼亚帝国的谍报员先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040040027V#030F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呵呵，看来『银闪』这个称号\n',
            '果然不是浪得虚名啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040029V在艾丝蒂尔君他们面前，\n',
            '你也是假装不知道的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F因为我不想让\n',
            '那两个孩子再担心多余的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '别再把话题扯远了，\n',
            '老实交代清楚你自己的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040032V你的目的是什么？\n',
            '为什么要潜入利贝尔王国？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040040033V#030F在此之前，\n',
            '可以让我澄清两点吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '首先，本人可没演什么小丑戏。\n',
            '一直以来我都是以真实的性情待人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040035V说我伪装什么的是不对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F啊～好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040037V就当白吃白喝\n',
            '是你真实的性情好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过那之后，借由被逮捕去到\n',
            '哈肯大门收集情报则是经过计划的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040039V虽然应该不至于\n',
            '算计到我们会被抓这件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F呵呵……\n',
            '随你怎么想好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还有一点要澄清的是……\n',
            '这个装置并不是导力通信器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而是帝国出土的『古代遗物』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040043V它不仅能和所有导力通信器进行通信，\n',
            '而且还能将讯号加密，避免被监听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040044V对公务繁忙的人来说，可是十分有用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F『古代遗物』……\n',
            '是七耀教会管理的神圣遗物吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040046V我越来越想知道\n',
            '你来王国的目的到底是什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F哎呀，讨厌……\n',
            '雪拉君你真的好主动哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040048V一位神秘美人怎么能\n',
            '随便打听一位天才美男的秘密呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040050V想亲近真的美人吗？\n',
            '我的鞭子也许能帮帮你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F不、不要啊，雪拉君。\n',
            '你就别和我开这种可怕的玩笑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还、还是先把说笑放在一边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F真是的。\n',
            '一开始老实交代不就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040040054V#030F正如你所说的那样，\n',
            '本人的确是帝国的谍报人员。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040055V不过……\n',
            '我来这里的目的并不是为了收集情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040056V我是为了来见一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F一个人……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F是一个你很熟悉的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040059V一位被王国军尊奉为\n',
            '最强的剑士、稀世的战略家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '大陆上仅有的四个Ｓ级游击士之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『剑圣』卡西乌斯·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T1101._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
