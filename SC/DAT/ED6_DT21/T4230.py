import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4230   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4230.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02013._CH', 'ED6_DT07/CH02013P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红茶',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BC',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -104230, 200, 9990, 225)

    def _loc_1BC(): pass

    label('loc_1BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1CF',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_03_50E)

    def _loc_1CF(): pass

    label('loc_1CF')

    Return()

# id: 0x0001 offset: 0x1D0
@scena.Code('func_01_1D0')
def func_01_1D0():
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
        'loc_1EC',
    )

    OP_B1('t4230_y')

    Jump('loc_1F5')

    def _loc_1EC(): pass

    label('loc_1EC')

    OP_B1('t4230_n')

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_206',
    )

    OP_72(0x000B, 0x0004)

    def _loc_206(): pass

    label('loc_206')

    Return()

# id: 0x0002 offset: 0x207
@scena.Code('func_02_207')
def func_02_207():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_297',
    )

    Jump('loc_2D9')

    def _loc_297(): pass

    label('loc_297')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2B3',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D9')

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2CF',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D9')

    def _loc_2CF(): pass

    label('loc_2CF')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D9(): pass

    label('loc_2D9')

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_477',
    )

    ChrTalk(
        0x0008,
        (
            '#0630251052V#090F在卡西乌斯先生的帮助下\n',
            '王国军正在踏踏实实地重建。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251053V#094F选择最好的道路前进……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251054V#090F说起来虽然容易，\n',
            '不过做起来没有比这个更难的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251055V他是少数掌握了正确\n',
            '前进方向的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251056V#093F本来他肯定是很想和艾丝蒂尔\n',
            '享受天伦之乐的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251057V#090F所以即便是为了回应他的精神，\n',
            '我也要以我的方式\n',
            '来努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_505')

    def _loc_477(): pass

    label('loc_477')

    ChrTalk(
        0x0008,
        (
            '#0630251058V#090F卡西乌斯先生肯定是很想和艾丝蒂尔\n',
            '享受天伦之乐的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251059V所以即便是为了回应他的精神，\n',
            '我也要以我的方式\n',
            '来努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_505(): pass

    label('loc_505')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x50E
@scena.Code('func_03_50E')
def func_03_50E():
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0105, 0x0040)
    ChrSetFlags(0x0104, 0x0040)
    ChrSetFlags(0x0108, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0105, 0x0004)
    ChrSetFlags(0x0104, 0x0004)
    ChrSetFlags(0x0108, 0x0004)
    ChrSetPos(0x0008, -104230, 200, 9990, 225)
    ChrSetPos(0x0101, -105330, 200, 10390, 180)
    ChrSetPos(0x0105, -103780, 200, 9000, 270)
    ChrSetPos(0x0108, -105330, 50, 7670, 0)
    ChrSetPos(0x0104, -106680, 200, 9000, 90)
    ChrSetPos(0x0009, -104750, 550, 9430, 0)
    ChrSetPos(0x000A, -105280, 550, 9460, 0)
    ChrSetPos(0x000B, -104730, 550, 8950, 0)
    ChrSetPos(0x000C, -105280, 550, 8400, 0)
    ChrSetPos(0x000D, -105830, 550, 8950, 0)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0104, 2)
    ChrSetChipByIndex(0x0105, 3)
    ChrSetChipByIndex(0x0108, 4)
    ChrClearFlags(0x0101, 0x0010)
    ChrClearFlags(0x0105, 0x0010)
    ChrClearFlags(0x0008, 0x0010)
    ChrSetSubChip(0x0101, 1)
    ChrSetSubChip(0x0105, 2)
    CameraMove(-104610, 200, 9480, 0)
    OP_67(0, 5280, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(253, 0)
    OP_72(0x000B, 0x0004)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0630250958V#094F对了……\n',
            '你们是为了恐吓信的事来的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250959V竟然连各国的大使馆\n',
            '和教会都寄了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250960V#092F让人觉得这已经不是\n',
            '单纯的恶作剧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250961V#1002F#6P嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250962V所以我们要通过\n',
            '向相关人士打听情况\n',
            '来找到罪犯的线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250963V#043F#4P祖母大人，关于这起事件您\n',
            '有什么线索吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250964V特别是国内方面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250965V#094F让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0630250966V#090F科洛蒂娅 。\n',
            '你自己怎么认为？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250967V#044F#4P我吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250968V#090F你作为王位继承者，\n',
            '平时应该有就国内形势\n',
            '进行分析……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250969V你能不能对我说说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250970V#542F#4P是、是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250971V#047F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250972V#042F关于互不侵犯条约，\n',
            '国内应该几乎没有什么\n',
            '反对势力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250973V不过我听说在政变后\n',
            '极右势力有被逼到\n',
            '绝境的趋势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250974V他们有可能把这份情绪\n',
            '转换为恐吓信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250975V#094F呵呵……很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250976V#090F和我的意见大致相同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250977V#1004F#6P请问，这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0630250978V#094F除了理查德上校之外\n',
            '以前还有不少\n',
            '主张扩充军备的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250979V#092F不过在政变后，\n',
            '这种主张完全\n',
            '被封锁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250980V他们一定积聚了不安和\n',
            '不满的情绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250981V#1002F#6P那么就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250982V还有除了理查德上校\n',
            '之外的扩军主义者在记恨政府？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250983V#090F也可以\n',
            '这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250984V#094F如果是这样的话……\n',
            '与其说这是他们的罪，\n',
            '倒不如说是我的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250985V因为利贝尔的言论自由，\n',
            '是我所给予认可的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250986V#043F#4P祖母大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250987V#1015F#6P我觉得没必要\n',
            '太同情他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250988V#092F不，言论自由是\n',
            '至为宝贵的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250989V即便是扩军论，也是\n',
            '基于爱国的精神。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250990V对这些言论进行全面地研究，\n',
            '然后把握好国家的发展方向……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250991V这是作为国家元首的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250992V#049F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080250993V#070F嗯，不过这样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080250994V条约实际被阻碍的\n',
            '危险就很低了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630250995V#090F如果恐吓犯是扩军\n',
            '主义者的话可能是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250996V在理查德上校已经被捕的现在，\n',
            '他们没有闹事的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250997V#094F问题是恐吓犯如果是\n',
            '其他人的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630250998V关于这种可能性\n',
            '我也没什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250999V#1007F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251000V#030F#6P艾莉茜雅女王。\n',
            '能问您一个问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(75)

    ChrSetSubChip(0x0101, 2)
    ChrSetSubChip(0x0105, 0)

    ChrTalk(
        0x0008,
        (
            '#0630251001V#097F嗯，请问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251002V#032F#6P陛下为什么要在现在\n',
            '倡导互不侵犯条约呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251003V不管怎么说现在还是政变的\n',
            '混乱尚未完全平息的时期。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251004V我倒是认为应该先专注于\n',
            '国内问题而非外交。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010251005V#1019F喂喂，奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630251006V#094F呵呵，可能正如\n',
            '奥利维尔先生所说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251007V#090F不过关于互不侵犯条约，\n',
            '在政变之前我就\n',
            '向两国政府试探过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251008V如果推迟此事，\n',
            '势必影响到国家的威信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251009V而且『克洛斯贝尔问题』\n',
            '也正处于不断加热的过程中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251010V#033F#6P哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010251011V#1004F克洛斯贝尔是……\n',
            '小玲居住的自治州？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251012V#042F嗯，是位于帝国和\n',
            '共和国之间的自治州。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251013V近几年，围绕着该自治州的归属\n',
            '问题，两国的对立立场很激烈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251014V#070F就好像是哽在帝国和共和国\n',
            '之间的鱼骨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251015V这些纠纷被概括起来\n',
            '称为『克洛斯贝尔问题』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251016V#1015F是吗……\n',
            '原来是那样的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251017V#035F#6P也就是说由利贝尔通过\n',
            '互不侵犯条约来拔去这根鱼骨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251018V#030F您的目的是这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630251019V#090F这不是一朝一夕\n',
            '能解决的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251020V我只是想\n',
            '提供一种契机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251021V并且这跟大陆西部的稳定\n',
            '和提高利贝尔的发言权也\n',
            '有所关联。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251022V#035F#6P呼，我真是有眼不识泰山。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251023V看来侵略利贝尔的行为\n',
            '比我想象的还要愚蠢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251024V我再次深深地体会到了这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251025V#1007F现在还说这些干吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010251026V#1004F#6P啊，对了。\n',
            '稍微改变一下话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0105, 2)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向艾莉茜雅女王询问了关于玲的双亲的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0630251027V#097F啊……有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251028V#1008F#6P即便是女王陛下应该\n',
            '也不会对此有什么线索吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1672',
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
            TXT(0x00, '【◇已经和希尔丹夫人对话】\n'),
            TXT(0x01, '【◇尚未和希尔丹夫人对话】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1666'),
        (0x00000001, 'loc_166C'),
        (-1, 'loc_1672'),
    )

    def _loc_1666(): pass

    label('loc_1666')

    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))

    Jump('loc_1672')

    def _loc_166C(): pass

    label('loc_166C')

    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))

    Jump('loc_1672')

    def _loc_1672(): pass

    label('loc_1672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Return,
        ),
        'loc_1809',
    )

    ChrTalk(
        0x0008,
        (
            '#0630251029V#093F嗯……\n',
            '抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251030V#090F如果前去格兰赛尔城的话\n',
            '我想希尔丹夫人\n',
            '应该知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251031V你们已经去见过她了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251032V#1015F#6P是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251033V#043F#4P希尔丹夫人看来也\n',
            '没什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630251034V#094F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251035V#090F如果你们需要，我可以\n',
            '联系克洛斯贝尔自治政府。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251036V随时可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251037V#1018F#6P啊……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193F')

    def _loc_1809(): pass

    label('loc_1809')

    ChrTalk(
        0x0008,
        (
            '#0630251029V#093F嗯……\n',
            '抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251039V#090F如果来了格兰赛尔城的话\n',
            '我想希尔丹夫人会知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251040V你们去问问她看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251041V#1006F#6P是，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630251035V#090F如果你们需要，我可以\n',
            '联系克洛斯贝尔自治政府。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251036V随时可以来这我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251037V#1018F#6P啊……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_193F(): pass

    label('loc_193F')

    ChrTalk(
        0x0105,
        (
            '#0060251045V#041F#4P祖母大人。\n',
            '谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251046V#542F我们也该去进行\n',
            '下面的调查了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251047V#049F所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0630251048V#094F呵呵，我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251049V#090F你今晚会留在\n',
            '格兰赛尔城堡吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630251050V到时让我好好\n',
            '听听你的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251051V#047F#4P是……\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 65535)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0105, 0x0040)
    ChrClearFlags(0x0105, 0x0004)
    ChrClearFlags(0x0104, 0x0040)
    ChrClearFlags(0x0104, 0x0004)
    ChrClearFlags(0x0108, 0x0040)
    ChrClearFlags(0x0108, 0x0004)
    Sleep(500)

    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x1ACF
@scena.Code('func_04_1ACF')
def func_04_1ACF():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    CameraMove(-1000, 8000, 35200, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    Sleep(1000)

    OP_6F(0x0001, 0)
    OP_70(0x0001, 60)
    OP_72(0x0001, 0x0010)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, func_05_24D3)
    Sleep(800)

    CreateThread(0x0108, 0x01, 0x00, func_06_2522)
    Sleep(800)

    CreateThread(0x0104, 0x01, 0x00, func_07_2585)
    Sleep(800)

    CreateThread(0x0105, 0x01, 0x00, func_08_25E8)
    CameraMove(-200, 8000, 27500, 4000)
    WaitForThreadExit(0x0105, 0x0001)
    OP_71(0x0001, 0x0010)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040251060V#031F#6P哎呀，真是一位了不起的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251061V那种绝妙的平衡感\n',
            '可以说是大陆第一了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251062V#071F嗯……\n',
            '简直是理想的君主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251063V我还真羡慕利贝尔国民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251064V#1006F哼哼，那是当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251065V谁叫这是咱们的\n',
            '女王呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251066V#049F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010251067V#1004F怎么了？科洛丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251068V#542F#5P啊，不……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251069V#045F我又一次感受到了\n',
            '祖母大人的厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251070V我果然是\n',
            '望尘莫及啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210161V#1026F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0105, 400)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040251072V#035F#6P呼，公主殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251073V女王陛下是\n',
            '什么时候即位的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0104, 400)
    Sleep(300)

    ChrTalk(
        0x0105,
        (
            '#0060251074V#044F#5P啊，哦。\n',
            '应该是２０岁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251075V#030F#6P那么殿下的芳龄是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251076V#043F#5P快１６了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251077V#044F……啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251078V#031F#6P呵呵，就是这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251079V陛下刚即位时\n',
            '也不见得能施展\n',
            '现在的政治手腕吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251080V更不用说你现在还不到\n',
            '陛下即位时的年龄呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251081V这是没的比的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251082V#074F在武术领域，只有拥有\n',
            '『器』的人才能到达『理』的境界。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251083V可即便是拥有了『器』，\n',
            '不经过一步步坚实的积累，\n',
            '也绝对无法到达那一境界。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251084V#070F现在陛下已经看出你\n',
            '拥有能到达『理』的『器』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251085V所以你没必要着急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060251086V#542F#5P奥利维尔先生、金先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251087V#041F……谢谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251088V#1006F呵呵，你们俩\n',
            '还真有口才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251089V堪称老当益壮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040251090V#032F#6P你真没礼貌……\n',
            '我才２５岁哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251091V比金先生可要\n',
            '年轻５岁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251092V#075F你才是个没\n',
            '礼貌的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22A0',
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
            TXT(0x00, '【◇没和希尔丹夫人对话/已去女佣室问了行踪】\n'),
            TXT(0x01, '【◇没和希尔丹夫人对话/还没去女佣室】\n'),
            TXT(0x02, '【◇已经和希尔丹夫人对话】\n'),
            TXT(0x03, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2288'),
        (0x00000001, 'loc_2291'),
        (0x00000002, 'loc_229A'),
        (-1, 'loc_22A0'),
    )

    def _loc_2288(): pass

    label('loc_2288')

    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    SetScenaFlags(ScenaFlag(0x02C5, 1, 0x1629))

    Jump('loc_22A0')

    def _loc_2291(): pass

    label('loc_2291')

    ClearScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))
    ClearScenaFlags(ScenaFlag(0x02C5, 1, 0x1629))

    Jump('loc_22A0')

    def _loc_229A(): pass

    label('loc_229A')

    SetScenaFlags(ScenaFlag(0x02C4, 6, 0x1626))

    Jump('loc_22A0')

    def _loc_22A0(): pass

    label('loc_22A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2403',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 1, 0x1629)),
            Expr.Return,
        ),
        'loc_2353',
    )

    ChrTalk(
        0x0105,
        (
            '#0060251093V#045F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251094V#048F那么我们也去\n',
            '和希尔丹夫人聊聊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211266V#1006F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251096V那么我们去\n',
            '左侧的资料室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2400')

    def _loc_2353(): pass

    label('loc_2353')

    ChrTalk(
        0x0105,
        (
            '#0060251093V#045F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251098V#048F那么我们也去\n',
            '和希尔丹夫人聊聊吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251099V去女佣室问问，\n',
            '就应该能知道她在哪儿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251100V#1006F嗯，ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2400(): pass

    label('loc_2400')

    Jump('loc_24C2')

    def _loc_2403(): pass

    label('loc_2403')

    ChrTalk(
        0x0105,
        (
            '#0060251093V#045F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251102V#048F总之现在和祖母大人\n',
            '以及希尔丹夫人都对话过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251103V#1006F嗯……\n',
            '要不要回市区？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251104V#542F#5P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008B, 0x02, 0x0080)
    OP_28(0x008B, 0x01, 0x0100)
    def _loc_24C2(): pass

    label('loc_24C2')

    Sleep(100)

    SetScenaFlags(ScenaFlag(0x02C4, 5, 0x1625))
    OP_28(0x008B, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x24D3
@scena.Code('func_05_24D3')
def func_05_24D3():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -870, 8000, 37870, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_24FA')
    def lambda_24FA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_24FA)

    ChrWalkTo(0x00FE, -900, 8000, 26000, 2000, 0x00)
    ChrSetDirection(0x00FE, 360, 400)

    Return()

# id: 0x0006 offset: 0x2522
@scena.Code('func_06_2522')
def func_06_2522():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -870, 8000, 37870, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2549')
    def lambda_2549():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2549)

    ChrWalkTo(0x00FE, -1000, 8000, 28390, 2000, 0x00)
    ChrWalkTo(0x00FE, 70, 8000, 27000, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0007 offset: 0x2585
@scena.Code('func_07_2585')
def func_07_2585():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -870, 8000, 37870, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_25AC')
    def lambda_25AC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_25AC)

    ChrWalkTo(0x00FE, -1000, 8000, 28390, 2000, 0x00)
    ChrWalkTo(0x00FE, -1950, 8000, 27000, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0008 offset: 0x25E8
@scena.Code('func_08_25E8')
def func_08_25E8():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -870, 8000, 37870, 180)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_260F')
    def lambda_260F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 200)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_260F)

    ChrWalkTo(0x00FE, -1000, 8000, 35200, 2000, 0x00)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    ChrWalkTo(0x00FE, -700, 8000, 28200, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
