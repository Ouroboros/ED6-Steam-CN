import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1130_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10C7
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480164V#1002F那卡片里的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480165V……莫非是指这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480166V#022F嗯，虽然有这可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480167V稍后再进行那个事件的调查吧。\n',
            '现在要赶紧前往拉文努村哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BD')

    def _loc_1B0(): pass

    label('loc_1B0')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_262',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480169V#072F嗯，是有这可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480170V不过那个事件的调查稍后再进行吧。\n',
            '现在应该赶紧前往拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BD')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_314',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480172V#030F唔，是有这可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480173V不过那个事件的调查稍后再进行吧。\n',
            '现在先赶紧前往拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480168V#1002F啊，嗯……明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BD')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480175V#042F嗯，说不定就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480176V不过这里迟些再调查吧。\n',
            '现在得赶紧前往拉文努村啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480177V#1002F啊，嗯……说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BD(): pass

    label('loc_3BD')

    TalkEnd(0x00FF)

    Return()

    def _loc_3C1(): pass

    label('loc_3C1')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 15500, 4000, 43010, 90)
    SetChrPos(0x00F7, 15490, 4000, 44530, 180)
    SetChrPos(0x00F8, 14760, 4000, 45010, 180)
    SetChrPos(0x00F9, 15520, 4000, 45770, 180)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_429',
    )

    SetChrPos(0x0004, 14740, 4000, 46100, 180)

    def _loc_429(): pass

    label('loc_429')

    OP_6D(15000, 4500, 43060, 0)
    OP_67(0, 4940, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(47000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010480415V#1002F这个，是七耀教会的圣典吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480416V『女神的话语』\n',
            '莫非就是说这个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_538',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480417V#026F圣典被认为是女神\n',
            '赐予的美好教诲之书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480418V#020F大概是不会错的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67C')

    def _loc_538(): pass

    label('loc_538')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_59D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480419V#070F圣典是女神\n',
            '赐予的美好教诲之书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480420V恐怕不会有错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67C')

    def _loc_59D(): pass

    label('loc_59D')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_611',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480421V#035F圣典被认为是女神\n',
            '赐予的美好教诲之书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480422V#030F我想恐怕不会有错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67C')

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_67C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480423V#053F圣典好像是女神\n',
            '赐予的美好教诲之书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480424V#050F大概不会有错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_67C(): pass

    label('loc_67C')

    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480425V#1015F啊，这么说来在主日学校\n',
            '好像也听说过这个似的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480426V#1000F……那好。\n',
            '先调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查圣典\n',
            '发现其中夹着铁制的勋章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#16I宝剑天马大勋章',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480427V#1001F嘿嘿，找到啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480428V#1016F不，不过\n',
            '好夸张的勋章啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_860',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480429V#031F哈哈，厚重夸张\n',
            '正是埃雷波尼亚的国风嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480430V和利贝尔王国的那种俭朴悠闲的\n',
            '国风正好相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AD')

    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8D8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480431V#045F嗯，因为厚重夸张\n',
            '是那边的国风嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480432V但这种国风竟然还\n',
            '反映在勋章上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AD')

    def _loc_8D8(): pass

    label('loc_8D8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_943',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480433V#070F唔，是帝国国风吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480434V一般说来帝国\n',
            '很喜欢厚重夸张的风气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9AD')

    def _loc_943(): pass

    label('loc_943')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9AD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480435V#021F呵呵，这是帝国国风嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480436V帝国有喜好厚重夸张\n',
            '事物的倾向哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9AD(): pass

    label('loc_9AD')

    ChrTalk(
        0x0101,
        (
            '#0010480437V#1011F唔……原来如此。\n',
            '这就是所谓国民性的差异吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480438V#1016F嗯，不过想想也对，\n',
            '这种程度的震撼力大概还是有必要的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480439V因为这个可是\n',
            '达维尔大使的勋章呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480440V#051F哈哈，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480441V那大叔的脸\n',
            '和这勋章也不相上下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C03')

    def _loc_ACD(): pass

    label('loc_ACD')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B30',
    )

    ChrTalk(
        0x0107,
        (
            '#0070480442V#067F嘿嘿，大概吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070480443V那个大叔的脸\n',
            '也是蛮有震撼力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C03')

    def _loc_B30(): pass

    label('loc_B30')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B9D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480444V#020F呵呵，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480445V那个达维尔大使的脸\n',
            '也是相当有震撼力的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C03')

    def _loc_B9D(): pass

    label('loc_B9D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C03',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480446V#071F哈哈，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480447V那位大人的面孔\n',
            '也是相当的厚重夸张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C03(): pass

    label('loc_C03')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C8B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480448V#070F唔，现在看起来\n',
            '大概更加这么觉得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480449V但也可能由于这次勋章被偷，\n',
            '他心情变得非常地差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DEA')

    def _loc_C8B(): pass

    label('loc_C8B')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D05',
    )

    ChrTalk(
        0x0105,
        (
            '#0060480450V#040F嗯，现在\n',
            '更加觉得他的脸夸张了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060480451V可能因为勋章被盗\n',
            '令他更加焦虑导致的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DEA')

    def _loc_D05(): pass

    label('loc_D05')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D75',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480452V#020F现在说不定\n',
            '还更严重了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480453V由于这件事\n',
            '皱纹都多出好几条了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DEA')

    def _loc_D75(): pass

    label('loc_D75')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DEA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480454V#030F唔，现在说不定\n',
            '他的脸变得更夸张了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480455V勋章被偷的事\n',
            '好象让他相当焦虑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DEA(): pass

    label('loc_DEA')

    ChrTalk(
        0x0101,
        (
            '#0010480456V#1015F哎呀，这么说还真是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480457V#1001F那么就马上\n',
            '把勋章送还吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x01, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1132._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0xE61
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E6E',
    )

    Return()

    def _loc_E6E(): pass

    label('loc_E6E')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_E80',
    )

    Return()

    def _loc_E80(): pass

    label('loc_E80')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_EBB',
    )

    Call(1, 0x0002)

    Jump('loc_F60')

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_ECA',
    )

    Call(1, 0x0002)

    Jump('loc_F60')

    def _loc_ECA(): pass

    label('loc_ECA')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_F22',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_F60')

    def _loc_F22(): pass

    label('loc_F22')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_F60(): pass

    label('loc_F60')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0002 offset: 0xF67
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_FEC',
    )

    ChrTalk(
        0x0008,
        (
            '#1340490586V我也为你们祈祷，\n',
            '一定能找到照片上的少女的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340490585V不到最后不要放弃希望，\n',
            '请一定要完成使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BD')

    def _loc_FEC(): pass

    label('loc_FEC')

    ChrTalk(
        0x0008,
        (
            '#1340490582V嗬，在追寻\n',
            '照片中少女的脚步吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340490583V实在遗憾，\n',
            '我没有印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340490584V如果有女神的指引，\n',
            '就一定能遇见的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1340490585V不到最后不要放弃希望，\n',
            '请一定要完成使命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_10BD(): pass

    label('loc_10BD')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
