import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0000_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0000   ._SN')

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
    header.mapModel       = 'E0000.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x203E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000FA0,
            dword_08        = 0xFFFFEE6C,
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
        ('ED6_DT06/CH20134._CH', 'ED6_DT06/CH20134P._CP'),
    ]

# id: 0x10002 offset: 0xC2
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

# id: 0x10003 offset: 0x102
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x102
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x102
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x102
@scena.Code('PreInit')
def PreInit():
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0005)

    Return()

# id: 0x0001 offset: 0x10A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x10B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_120',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_120(): pass

    label('loc_120')

    Return()

# id: 0x0003 offset: 0x121
@scena.Code('func_03_121')
def func_03_121():
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
            '#0030840007V#020F正如刚才所见，\n',
            '定期船内的导力完全停止了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840008V这也就意味着，\n',
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
        (0x00000000, 'loc_506'),
        (0x00000001, 'loc_579'),
        (0x00000002, 'loc_5FC'),
        (0x00000003, 'loc_66F'),
        (0x00000004, 'loc_714'),
        (-1, 'loc_734'),
    )

    def _loc_506(): pass

    label('loc_506')

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

    Jump('loc_734')

    def _loc_579(): pass

    label('loc_579')

    ChrTalk(
        0x0103,
        (
            '#0030840009V#026F确实，在把人质转移到空贼飞艇上的过程中，\n',
            '定期船必须要着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_734')

    def _loc_5FC(): pass

    label('loc_5FC')

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

    Jump('loc_734')

    def _loc_66F(): pass

    label('loc_66F')

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

    Jump('loc_734')

    def _loc_714(): pass

    label('loc_714')

    ChrTalk(
        0x0103,
        (
            '#020F对，就是因为这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_734')

    def _loc_734(): pass

    label('loc_734')

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
            '#0030840010V也就是说只能让空贼飞艇\n',
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
            '#0030840011V毕竟他们拥有军用飞艇啊。',
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

# id: 0x0004 offset: 0xAC1
@scena.Code('func_04_AC1')
def func_04_AC1():
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
            '真是世态炎凉啊。\n',
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

# id: 0x0005 offset: 0xEF4
@scena.Code('func_05_EF4')
def func_05_EF4():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_12(0x0001ADB0, 0x000249F0, 0x00000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_20(0x00000000)
    CameraMove(600, 5000, 44810, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(7230, 0)
    OP_6C(143000, 0)
    OP_6E(332, 0)
    PlaySE(451, 0x00, 0x64)
    PlaySE(121, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0104, 0x0002)
    SetChrChipByIndex(0x0104, 2)
    SetChrSubChip(0x0104, 2)
    SetChrPos(0x0104, 0, 5000, -10200, 270)
    SetChrPos(0x0103, 2600, 5000, 1560, 0)
    FadeOut(0, 0, -1)
    Sleep(2000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('青年的声音')

    Talk(
        (
            '#0040040001V',
            (TxtCtl.SetColor, 0x0),
            '……以上就是\n',
            '在王国北部发生的空贼事件的始末。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    SetChrName('青年的声音')

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
    Sleep(1000)

    SetChrName('青年的声音')

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
    Sleep(1000)

    SetChrName('青年的声音')

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
    Sleep(1000)

    SetChrName('青年的声音')

    Talk(
        (
            '#0040040005V',
            (TxtCtl.SetColor, 0x0),
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    SetChrName('青年的声音')

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
    Sleep(1000)

    SetChrName('青年的声音')

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
    Sleep(1000)

    SetChrName('青年的声音')

    Talk(
        (
            '#0040040008V',
            (TxtCtl.SetColor, 0x0),
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    PlayBGM(34)
    FadeIn(6000, 0)
    OP_12(0x00009C40, 0x0001ADB0, 0x000032C8)

    @scena.Lambda('lambda_1229')
    def lambda_1229():
        CameraMove(250, 5000, -9420, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1229)

    @scena.Lambda('lambda_1241')
    def lambda_1241():
        OP_67(0, 10000, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1241)

    @scena.Lambda('lambda_1259')
    def lambda_1259():
        CameraSetDistance(2980, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1259)

    Sleep(4000)

    @scena.Lambda('lambda_126E')
    def lambda_126E():
        OP_6C(53000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_126E)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraSetDistance(2000, 0)
    OP_0D()
    Sleep(500)

    OP_99(0x0104, 0x02, 0x00, 1200)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040040009V#030F#2P呵呵，才不是。\n',
            '我也认识了一些有趣的朋友啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040010V#030F这里料理美味，美人又多。\n',
            '简直就是我梦寐以求的国度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040011V真想一辈子住在这里啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrSubChip(0x0104, 2)
    Sleep(50)

    SetChrSubChip(0x0104, 3)
    Sleep(50)

    SetChrSubChip(0x0104, 2)
    Sleep(50)

    SetChrSubChip(0x0104, 4)
    Sleep(200)

    SetChrSubChip(0x0104, 2)
    Sleep(50)

    SetChrSubChip(0x0104, 3)
    Sleep(50)

    SetChrSubChip(0x0104, 2)
    Sleep(50)

    SetChrSubChip(0x0104, 4)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040040012V#035F#2P知道啦，知道啦。\n',
            '拜托你不要发出那么吓人的声音嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040013V好的，那边就继续拜托你了，\n',
            '别忘了代我向宰相大人问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0104, 2)
    Sleep(200)

    OP_99(0x0104, 0x02, 0x00, 1200)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040040014V#030F#2P下次再联络吧，我的好友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Fade(500)
    SetChrSubChip(0x0104, 5)
    OP_0D()
    PlaySE(156, 0x00, 0x64)
    Sleep(1000)

    ClearChrFlags(0x0104, 0x0002)
    SetChrChipByIndex(0x0104, 65535)
    SetChrSubChip(0x0104, 0)
    SetChrDirection(0x0104, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040040015V#031F#5P呵呵，还是老样子，\n',
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
            '#0030040017V……是携带用的小型通信器呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0103,
        '女性的声音',
        (
            '#0030040018V就这么带在身边到处走，\n',
            '也太过显眼了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1594')
    def lambda_1594():
        CameraSetDistance(2300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1594)

    @scena.Lambda('lambda_15A4')
    def lambda_15A4():
        CameraMove(930, 5000, -4690, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_15A4)

    @scena.Lambda('lambda_15BC')
    def lambda_15BC():
        ChrWalkTo(0x00FE, 2710, 5000, -520, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_15BC)

    ChrTurnDirection(0x0104, 0x0103, 400)

    @scena.Lambda('lambda_15DE')
    def lambda_15DE():
        ChrTurnDirection(0x00FE, 0x0103, 0)
        Yield()

        Jump('lambda_15DE')

    DispatchAsync2(0x0104, 0x0001, lambda_15DE)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0103, 0x0002)
    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0104,
        (
            '#0040040019V#033F雪……雪拉君。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_161E')
    def lambda_161E():
        OP_67(0, 8510, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_161E)

    @scena.Lambda('lambda_1636')
    def lambda_1636():
        CameraSetDistance(2300, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1636)

    @scena.Lambda('lambda_1646')
    def lambda_1646():
        OP_6C(142000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1646)

    @scena.Lambda('lambda_1656')
    def lambda_1656():
        CameraMove(100, 5000, -9500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1656)

    ChrWalkTo(0x0103, 170, 5000, -6900, 2000, 0x00)
    ChrTurnDirection(0x0103, 0x0104, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#0030040020V#026F不过没想到的是，\n',
            '你竟然会有中央工房\n',
            '还未实用化的导力通信器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040021V#022F你，到底是什么人？',
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
            '#0040040024V#031F不过，如果想知道得更多的话，\n',
            '那就只能以枕边话的形式来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030040025V#027F很遗憾，\n',
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
            '#0040040027V#033F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040028V#035F呵呵，看来『银闪』这个称号\n',
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
            '#0030040030V#522F因为我不想让\n',
            '那两个孩子再担心多余的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040031V#020F别再把话题扯远了，\n',
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
            '#0040040034V#031F首先，本人可没演什么小丑戏。\n',
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
            '#0030040036V#025F啊～好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040037V就当白吃白喝\n',
            '是你真实的性情好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030040038V#022F不过那之后，借由被逮捕去到\n',
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
            '#0040040040V#031F呵呵……\n',
            '随你怎么想好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040041V#030F还有一点要澄清的是……\n',
            '这个装置并不是导力通信器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040042V而是帝国出土的『古代遗物』。',
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
            '#0030040045V#022F『古代遗物』……\n',
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
            '#0040040047V#031F哎呀，讨厌……\n',
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
            '#0030040049V#021F……………………………',
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
            '#0040040051V#036F不、不要啊，雪拉君。\n',
            '你就别和我开这种可怕的玩笑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040052V#030F还、还是先把说笑放在一边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030040053V#022F真是的。\n',
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
            '#0030040057V#023F一个人……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E78')
    def lambda_1E78():
        CameraSetDistance(2100, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E78)

    ChrTalk(
        0x0104,
        (
            '#0040040058V#035F是一个你很熟悉的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040059V一位被王国军尊奉为\n',
            '最强的剑士、稀世的战略家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040040060V整个大陆中拥有特殊称号的游击士\n',
            '不足五位，而他同时还是其中之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_24(0x01C3, 0x5A)
    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x01C3, 0x50)
    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x01C3, 0x46)
    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x01C3, 0x3C)
    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x01C3, 0x32)
    OP_24(0x0079, 0x32)
    Sleep(100)

    OP_24(0x01C3, 0x28)
    OP_24(0x0079, 0x28)
    Sleep(100)

    OP_24(0x01C3, 0x1E)
    OP_24(0x0079, 0x1E)
    Sleep(100)

    OP_24(0x01C3, 0x14)
    OP_24(0x0079, 0x14)
    Sleep(100)

    OP_24(0x01C3, 0x0A)
    OP_24(0x0079, 0x0A)
    Sleep(100)

    OP_23(0x01C3)
    OP_23(0x0079)
    OP_21()
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('奥利维尔')

    Talk(
        (
            '#0040040061V',
            (TxtCtl.SetColor, 0x0),
            '这个人就是——\n',
            '『剑圣』卡西乌斯·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS042._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    ClearMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T1101._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
