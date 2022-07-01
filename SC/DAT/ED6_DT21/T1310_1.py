import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1310_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1310_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1310_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x29AA
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 82350, 0, 53600, 180)
    SetChrPos(0x0106, 83210, 0, 53720, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_103',
    )

    SetChrPos(0x0105, 82610, 0, 54630, 180)
    SetChrPos(0x00F9, 81580, 0, 54720, 180)

    Jump('loc_157')

    def _loc_103(): pass

    label('loc_103')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_135',
    )

    SetChrPos(0x0105, 82610, 0, 54630, 180)
    SetChrPos(0x00F8, 81580, 0, 54720, 180)

    Jump('loc_157')

    def _loc_135(): pass

    label('loc_135')

    SetChrPos(0x00F8, 82610, 0, 54630, 180)
    SetChrPos(0x00F9, 81580, 0, 54720, 180)

    def _loc_157(): pass

    label('loc_157')

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_173',
    )

    SetChrPos(0x000C, 82940, 0, 52010, 0)

    def _loc_173(): pass

    label('loc_173')

    OP_4A(0x000C, 255)
    OP_6D(82800, 0, 53860, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(35000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x007A, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63B',
    )

    OP_28(0x007A, 0x01, 0x0008)

    ChrTalk(
        0x000C,
        (
            '#2890481000V呼，总算\n',
            '来到关所了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481001V就一直待在这里\n',
            '绝对不能回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481002V如果\n',
            '不安排人来迎接我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481003V#1004F#1P（啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_382',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481004V#042F#5P（那是……芙拉瑟小姐呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060481005V#045F（想、想不到她\n',
            '　竟然会来到这里……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481006V#050F#2P（是王立学院的学生呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481007V（她就是那个要\n',
            '　逃避相亲的『大小姐』吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481008V#1002F#1P（嗯、嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_421')

    def _loc_382(): pass

    label('loc_382')

    ChrTalk(
        0x0106,
        (
            '#0050481009V#050F#2P（看上去就像是\n',
            '　王立学院的学生呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481007V（她就是那个要\n',
            '　逃避相亲的『大小姐』吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481008V#1002F#1P（嗯、嗯……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_421(): pass

    label('loc_421')

    OP_8C(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#2890481012V#4P哎呀，你们是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_585',
    )

    ChrTalk(
        0x0101,
        (
            '#0010481013V#1016F#1P那个，好久不见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481014V……别来无恙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481015V#4P嗯，我很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481016V#4P以前我们在王立\n',
            '学院见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060481017V#040F#5P你好，芙拉瑟小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481018V#4P哎呀……\n',
            '科洛丝也在！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481019V#4P你们到底为什么会来到这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_638')

    def _loc_585(): pass

    label('loc_585')

    ChrTalk(
        0x0101,
        (
            '#0010481020V#1000F#1P那个，好久不见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481014V……别来无恙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481022V#4P嗯，以前我们在王立\n',
            '学院见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481023V#4P各位今天到底为什么\n',
            '会来到这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_638(): pass

    label('loc_638')

    Jump('loc_68C')

    def _loc_63B(): pass

    label('loc_63B')

    ChrTalk(
        0x000C,
        (
            '#2890481024V#4P哎呀，各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481025V#4P你们又来了，\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_68C(): pass

    label('loc_68C')

    ChrTalk(
        0x0101,
        (
            '#0010481026V#1000F#1P嗯，的确有个紧急的\n',
            '委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481027V#1015F其实我们是来\n',
            '找芙拉瑟小姐帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481028V#4P找……我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481029V#4P那我究竟要\n',
            '做什么才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481030V#1015F#1P很简单啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481031V#1002F希望你和我们一起……\n',
            '返回柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_96(0x000C, 0x000144C4, 0x00000000, 0x0000C8F0, 0x000001F4, 0x00002710)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_802',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481032V#044F芙拉瑟小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_802(): pass

    label('loc_802')

    ChrTalk(
        0x000C,
        (
            '#2890481033V#4P你、你们──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481034V#4P#3S应该……\n',
            '是蕾娜的爪牙吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481035V#1016F#1P爪、爪牙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481036V请不要把我们说得像是\n',
            '恶势力一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481037V#045F#5P真、真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A04')

    def _loc_8F4(): pass

    label('loc_8F4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070481038V#067F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A04')

    def _loc_92A(): pass

    label('loc_92A')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_991',
    )

    ChrTalk(
        0x0104,
        (
            '#0040481039V#035F呼，太伤人心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040481040V我明明一直都是\n',
            '站在女士这一边的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A04')

    def _loc_991(): pass

    label('loc_991')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A04',
    )

    ChrTalk(
        0x0108,
        (
            '#0080481041V#070F呵呵，因为有两个\n',
            '大男人在呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080481042V在对方看来，\n',
            '爪牙可能就是这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A04(): pass

    label('loc_A04')

    ChrTalk(
        0x0106,
        (
            '#0050481043V#551F#2P喂喂，大小姐。\n',
            '在学校没学过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481044V我们游击士都是中立的。\n',
            '既不是谁的爪牙也不是谁的手下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481045V#4P嗯、嗯……\n',
            '我当然知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481046V#4P但我不会被这种\n',
            '冠冕堂皇的话所欺骗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481047V#4P嘴上这么说，最后还是要\n',
            '用武力带我回去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481048V#057F#2P这就要看你的态度了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481049V如果不想被那样对待，\n',
            '就乖乖听我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0106, 83140, 0, 53270, 2000, 0x00)
    ChrTurnDirection(0x0106, 0x000C, 0)
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x000C, 0x00B4, 0x00000064, 0x000003E8, 0x00)

    ChrTalk(
        0x000C,
        (
            '#2890481050V#4P别、别过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481051V#4P你再靠近我就\n',
            '喊人了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481052V#1002F#1P你、你冷静点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481053V没事的，我们什么也不会做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481054V#552F#2P真是的……\n',
            '好一个会大惊小怪的大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010481055V#1007F#1P阿加特你也稍微等等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)
    Sleep(1000)

    OP_94(0x01, 0x0101, 0x0000, 0x0000015E, 0x000003E8, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010481056V#1002F#1P那个，芙拉瑟小姐你听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481057V我们是来\n',
            '保护你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481058V#1003F我知道你无法\n',
            '接受相亲的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481059V#4P当然，不可原谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481060V#4P但是，更让我感到\n',
            '不可原谅的是蕾娜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481061V#1002F#1P……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481062V#4P她……\n',
            '居然背叛了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481063V#4P本来这次来柏斯的\n',
            '目的应该是旅游的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481064V#4P虽然经常路过那座城市，\n',
            '但是却没来旅行过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481065V#4P所以我很期待\n',
            '这次的旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481066V#4P可是来了以后等着我的\n',
            '却是相亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481067V#4P蕾娜一开始就准备\n',
            '欺骗我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481068V#1015F#1P原来如此，之前\n',
            '就一直瞒着你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481069V#1002F但这样一来岂不是\n',
            '更应该返回城里了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481070V你应该向蕾娜小姐\n',
            '说出真实的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481071V#4P这、这个……\n',
            '绝对不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481072V#4P我根本就不想\n',
            '再见到蕾娜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 180, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010481073V#1019F#1P（呼、唔……\n',
            '这样下去好象很麻烦呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0106, 270, 400)

    ChrTalk(
        0x0106,
        (
            '#0050481074V#552F#2P（喂…………）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481075V（你要跟她说这些\n',
            '  说到什么时候啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010481076V#1016F#1P（再、再稍微等等。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481077V（我再劝劝她……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)
    ChrTurnDirection(0x0106, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010481078V#1002F#1P我说，芙拉瑟小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481079V你无～论如何\n',
            '都不愿意返回城里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481080V#4P嗯，我没那个打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481081V#4P只要还是和蕾娜一起参加相亲，\n',
            '我就不准备返回柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481082V#1007F#1P是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481083V唉，真是的…\n',
            '我们说什么你都听不进去，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【芙拉瑟小姐真是个顽固的人呢】\n'),
            TXT(0x01, '【芙拉瑟小姐真是个胆小鬼呢】\n'),
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
        'loc_1B99',
    )

    ChrTalk(
        0x0101,
        (
            '#0010481084V#1007F#1P……芙拉瑟小姐真是个顽固的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#2890481085V#4P我说，你们才\n',
            '是顽固的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481086V#4P就算是游击士，\n',
            '也不能不考虑别人的感受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481087V#4P难道你们要把自己的\n',
            '道理强加于人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481088V#1013F#1P我、我们\n',
            '可没这么想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481089V#4P那就不要管我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481090V#4P你们老缠着我不放的话\n',
            '我可真的要喊人了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010481091V#1008F#1P啊、啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481092V#053F#2P呼，说服失败。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481093V#057F真是太\n',
            '浪费时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0106, 83140, 0, 52040, 2000, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#2890481094V#4P呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481095V#4P你、你们要干什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481096V#057F#2P根据规约第二项的但书，\n',
            '对你进行强制保护。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481097V#1015F#1P规约的第二项……\n',
            '我记得是『民间人士保护』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481098V……可那个『但书』是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481099V#053F#2P嗯，那是条约中的\n',
            '特例措施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481100V它规定了非常时期\n',
            '可以强制执行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481101V#1004F#1P还、还有这一条啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481102V#4P太、太乱来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16E5')
    def lambda_16E5():
        OP_8E(0x000C, 83140, 0, 50500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_16E5)

    Sleep(200)

    OP_8E(0x0106, 83140, 0, 51100, 3000, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x000C, 0x00000032, 0x00000000, 0x000001F4, 0x000007D0)

    ChrTalk(
        0x000C,
        (
            '#2890481103V#4P#3S你、你要干什么！！\n',
            '放开我！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481104V#053F#2P这是合法的措施。\n',
            '你再哭再闹也没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481105V好了，赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17DF')
    def lambda_17DF():
        ChrTurnDirection(0x0101, 0x0106, 400)
        Yield()

        Jump('lambda_17DF')

    DispatchAsync2(0x0101, 0x0001, lambda_17DF)

    @scena.Lambda('lambda_17F0')
    def lambda_17F0():
        ChrTurnDirection(0x00F8, 0x0106, 400)
        Yield()

        Jump('lambda_17F0')

    DispatchAsync2(0x00F8, 0x0001, lambda_17F0)

    @scena.Lambda('lambda_1801')
    def lambda_1801():
        ChrTurnDirection(0x00F9, 0x0106, 400)
        Yield()

        Jump('lambda_1801')

    DispatchAsync2(0x00F9, 0x0001, lambda_1801)

    CreateThread(0x0106, 0x00, 0x01, 0x0004)
    CreateThread(0x000C, 0x00, 0x01, 0x0005)
    CreateThread(0x0101, 0x00, 0x01, 0x0001)
    CreateThread(0x00F9, 0x02, 0x01, 0x0003)

    ChrTalk(
        0x000C,
        (
            '#2890481106V#10A有、有人吗！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481107V#10A救命啊～有人要绑架我～！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481108V#054F#10A喂，别说话，快走。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0106, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_6D(80870, 0, 54440, 2500)

    ChrTalk(
        0x0101,
        (
            '#0010481109V#1016F嗯、嗯……\n',
            '要和她一起返回山道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481110V#1007F唉，感觉路上会有事发生…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481111V#2P啊啊啊，放开我！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0097, 0x00, 0x64)

    ChrTalk(
        0x0106,
        (
            '#0050481112V#2P喂、喂喂，别捣乱！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '士兵的声音',
        (
            '#2P怎、怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '士兵的声音',
        (
            '#2P莫、莫非是绑架！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A1B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080481115V#070F哈哈，真是个有活力的大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1A1B(): pass

    label('loc_1A1B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A5F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030481116V#021F呵呵，真是个有活力的大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1A5F(): pass

    label('loc_1A5F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481117V#045F不、不愧是芙拉瑟小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060481118V正在拼命抵抗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B1F')

    def _loc_1ABD(): pass

    label('loc_1ABD')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B1F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040481119V#031F哈哈哈。\n',
            '不愧是帝国的大小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040481120V确实是只难驯之马。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B1F(): pass

    label('loc_1B1F')

    ChrTalk(
        0x0101,
        (
            '#0010481121V#1019F总、总之我们上去帮忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481122V放任不管的话\n',
            '会有大麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B7E')
    def lambda_1B7E():
        OP_6D(80870, 10000, 54440, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1B7E)

    OP_28(0x007A, 0x01, 0x0020)

    Jump('loc_2836')

    def _loc_1B99(): pass

    label('loc_1B99')

    ChrTalk(
        0x0101,
        (
            '#0010481123V#1007F#1P……芙拉瑟小姐真是个胆小鬼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#2890481124V#4P胆、胆小鬼……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481125V#4P你、你刚才……\n',
            '说我是胆小鬼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481126V#1015F#1P嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481127V#4P我哪里\n',
            '胆小了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481128V#4P希望你解释一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481129V#1002F#1P因为，你刚才虽然\n',
            '说了很多理由……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481130V可是到头来还是\n',
            '在害怕相亲吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2890481131V#4P我、我没害怕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481132V#1002F#1P那就赶紧回\n',
            '柏斯不就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481133V虽然你想把相亲的事\n',
            '怪罪在蕾娜小姐头上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481134V可是她也不是自己\n',
            '愿意那么做的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481135V如果你试着站在蕾娜小姐的立场上\n',
            '考虑问题的话就能很容易地明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481136V#4P这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481137V#1010F#1P可是你却以此为借口\n',
            '来逃避相亲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481138V人的一生中会遇到\n',
            '很多不合理或者令人痛苦的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481139V#1002F因为讨厌而逃避就\n',
            '永远也无法前进。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481140V就因为你是这样的胆小鬼，\n',
            '所以蕾娜小姐才对你撒了谎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481141V#4P这、这个……\n',
            '这些我都知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481142V#4P#3S嗯！！\n',
            '你说得没错！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481143V#4P#3S所以我才无法\n',
            '原谅蕾娜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481144V#1020F#1P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481145V#4P蕾娜虽然平时\n',
            '总是夸我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481146V#4P#3S可是有这种大事的时候\n',
            '她还是不相信我！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    @scena.Lambda('lambda_2096')
    def lambda_2096():
        ChrTurnDirection(0x0106, 0x000C, 400)
        Yield()

        Jump('lambda_2096')

    DispatchAsync2(0x0106, 0x0001, lambda_2096)

    @scena.Lambda('lambda_20A7')
    def lambda_20A7():
        OP_92(0x000C, 0x0101, 0x000007D0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_20A7)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2890481147V#4P真正的朋友应该\n',
            '互相信任，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_20FA')
    def lambda_20FA():
        OP_92(0x000C, 0x0101, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_20FA)

    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2890481148V#4P那个？艾丝蒂尔小姐。\n',
            '朋友就应该是那样的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_216B')
    def lambda_216B():
        OP_92(0x000C, 0x0101, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_216B)

    OP_94(0x01, 0x0101, 0x00B4, 0x000000C8, 0x000003E8, 0x00)
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2890481149V#4P#3S我有什么地方\n',
            '说错了吗？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_221B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481150V#043F#5P芙拉瑟小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_221B(): pass

    label('loc_221B')

    ChrTalk(
        0x0101,
        (
            '#0010481151V#1008F#1P等、等等……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481152V别、别那么兴奋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481153V#4P呼、呼、呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050481154V#053F#2P……嗯，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481155V你也有很多的\n',
            '疑问呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050481156V#050F可是你是不是\n',
            '把质问的对象搞错了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481157V#4P……呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481158V是啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481159V#4P……也许你们是对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481160V#4P这份怒气应该\n',
            '保留给蕾娜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481161V#1011F#1P啊，那就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481162V你愿意回去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481163V#4P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481164V#4P把胸中的怒气宣泄出来，\n',
            '心情舒服多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481165V#4P总之……\n',
            '先回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481166V#4P我必须要告诉蕾娜\n',
            '她有多伤我的心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24E6',
    )

    ChrTalk(
        0x0105,
        (
            '#0060481167V#542F#5P呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060481168V太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E6(): pass

    label('loc_24E6')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2522',
    )

    ChrTalk(
        0x0103,
        (
            '#0030481169V#020F呵呵，轻松一点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D6')

    def _loc_2522(): pass

    label('loc_2522')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2596',
    )

    ChrTalk(
        0x0108,
        (
            '#0080481170V#070F哈哈，你看上去像是\n',
            '除去了一块心病。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080481171V怎么样？\n',
            '平静下来一点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25D6')

    def _loc_2596(): pass

    label('loc_2596')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25D6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040481172V#030F怎么样？\n',
            '平静下来一点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D6(): pass

    label('loc_25D6')

    ChrTalk(
        0x000C,
        (
            '#2890481173V#4P嗯，多少有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481174V#4P总之，我有勇气\n',
            '来面对相亲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010481175V#1001F#1P嘿嘿，那就好⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010481176V#1017F对不起，我说了很多\n',
            '很不客气的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481177V#4P不，我才是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481178V#4P好了，各位。\n',
            '那么我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2890481179V#4P归途的护卫工作……\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_274C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080481180V#070F嗯，你就放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27EE')

    def _loc_274C(): pass

    label('loc_274C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_278D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040481181V#031F呵呵，我非常乐意\n',
            '保护你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27EE')

    def _loc_278D(): pass

    label('loc_278D')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27C1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230855V#525F嗯，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27EE')

    def _loc_27C1(): pass

    label('loc_27C1')

    ChrTalk(
        0x0101,
        (
            '#0010481183V#1006F#1P嗯，就交给我们吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27EE(): pass

    label('loc_27EE')

    ChrTalk(
        0x0106,
        (
            '#0050481184V#051F#2P好了，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_281E')
    def lambda_281E():
        OP_6D(82800, 10000, 53860, 4500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_281E)

    OP_28(0x007A, 0x01, 0x0010)
    def _loc_2836(): pass

    label('loc_2836')

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T1131._SN', 101, 0, 0)
    IdleLoop()
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x2855
@scena.Code('Init')
def Init():
    Sleep(200)

    OP_8F(0x0101, 83160, 0, 53950, 2000, 0x00)

    Return()

# id: 0x0002 offset: 0x286F
@scena.Code('ReInit')
def ReInit():
    Sleep(400)

    OP_8F(0x00F8, 78960, 0, 54740, 2000, 0x00)

    Return()

# id: 0x0003 offset: 0x2889
@scena.Code('func_03_2889')
def func_03_2889():
    Sleep(1000)

    OP_6D(78140, 0, 53020, 3000)

    Return()

# id: 0x0004 offset: 0x28A0
@scena.Code('func_04_28A0')
def func_04_28A0():
    OP_8E(0x0106, 83140, 0, 52780, 2000, 0x00)
    OP_8E(0x0106, 82540, 0, 52780, 2000, 0x00)
    OP_A6(0x0006)
    OP_8E(0x0106, 75000, 0, 52780, 2000, 0x00)

    @scena.Lambda('lambda_28E5')
    def lambda_28E5():
        OP_9F(0x0106, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_28E5)

    OP_8E(0x0106, 73700, 0, 52780, 2000, 0x00)
    OP_8E(0x0106, 72700, 0, 52780, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0x291A
@scena.Code('func_05_291A')
def func_05_291A():
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrFlags(0x000C, 0x0040)
    OP_8F(0x000C, 83140, 0, 52040, 2000, 0x00)
    OP_8F(0x000C, 83140, 0, 53000, 2000, 0x00)
    OP_A2(0x0006)
    OP_8C(0x000C, 90, 0)
    OP_8F(0x000C, 75000, 0, 52780, 2000, 0x00)

    @scena.Lambda('lambda_297D')
    def lambda_297D():
        OP_9F(0x000C, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_297D)

    OP_8F(0x000C, 73700, 0, 52780, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
