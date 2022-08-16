import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0601   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0601.x'
    header.mapIndex       = 17
    header.bgm            = 16
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
            word_3A         = 17,
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵塞维安',
            x                   = -940,
            z                   = 7250,
            y                   = -94770,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xD2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xD3
@scena.Code('func_01_D3')
def func_01_D3():
    OP_16(0x02, 4000, -129000, -166000, 196626)

    Return()

# id: 0x0002 offset: 0xE6
@scena.Code('func_02_E6')
def func_02_E6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_E6')

    def _loc_FB(): pass

    label('loc_FB')

    Return()

# id: 0x0003 offset: 0xFC
@scena.Code('func_03_FC')
def func_03_FC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11F',
    )

    OP_8D(0x00FE, -3140, -97580, 1480, -73120, 3000)

    Jump('func_03_FC')

    def _loc_11F(): pass

    label('loc_11F')

    Return()

# id: 0x0004 offset: 0x120
@scena.Code('func_04_120')
def func_04_120():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_24E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1B0',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～……\n',
            '之前在这里执勤的时候，\n',
            '我好像看到了一个女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正觉得奇怪，\n',
            '想擦一下眼睛看清楚的时候，\n',
            '她却又不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B')

    def _loc_1B0(): pass

    label('loc_1B0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唔～……\n',
            '之前在这里执勤的时候，\n',
            '我好像看到了一个女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正觉得奇怪，\n',
            '想擦一下眼睛看清楚的时候，\n',
            '她却又不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～是不是我累了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B(): pass

    label('loc_24B')

    Jump('loc_DD9')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2D1',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会\n',
            '今天要进行决战了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是特务部队的家伙\n',
            '进入了决赛啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我不想承认，\n',
            '不过他们的确有两手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_2D1(): pass

    label('loc_2D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_337',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始，\n',
            '巡视的次数要增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不能及时传递情报的话，\n',
            '就无法抓住恐怖分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_337(): pass

    label('loc_337')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_488',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3C1',
    )

    ChrTalk(
        0x00FE,
        (
            '艾尔贝周游道绿意昂然，\n',
            '平时去那里散步是最合适不过的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '现在恐怖分子可能就潜藏在\n',
            '那花草树木中的某处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_485')

    def _loc_3C1(): pass

    label('loc_3C1')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '艾尔贝周游道绿意昂然，\n',
            '平时去那里散步是最合适不过的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对于格兰赛尔的市民来说，\n',
            '这一带就好像是个公园。\n',
            '实在是相当的漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '现在恐怖分子可能就潜藏在\n',
            '那花草树木中的某处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_485(): pass

    label('loc_485')

    Jump('loc_DD9')

    def _loc_488(): pass

    label('loc_488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4FD',
    )

    ChrTalk(
        0x00FE,
        (
            '我从来没有在这里\n',
            '看到过亲卫队的身影。\n',
            '今天一天还算平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是现在守卫王都的同志们\n',
            '一定很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_4FD(): pass

    label('loc_4FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_6ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 1, 0x6E9)),
            Expr.Return,
        ),
        'loc_5AB',
    )

    ChrTalk(
        0x00FE,
        (
            '城墙上太宽阔了，\n',
            '要巡视一遍非常辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在观光客\n',
            '都集中到王都去了，\n',
            '所以还算比较轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果恐怖分子\n',
            '混在观光客里进入王都，\n',
            '那就难以区分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6EA')

    def _loc_5AB(): pass

    label('loc_5AB')

    SetScenaFlags(ScenaFlag(0x00DD, 1, 0x6E9))

    ChrTalk(
        0x00FE,
        (
            '你们能来到这里也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把这个送给你们做纪念吧。\n',
            '哈哈，我还真是老土啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x021A, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第９卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '城墙上太宽阔了，\n',
            '要巡视一遍非常辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在观光客\n',
            '都集中到王都去了，\n',
            '所以还算比较轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果恐怖分子\n',
            '混在观光客里进入王都，\n',
            '那就难以区分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6EA(): pass

    label('loc_6EA')

    Jump('loc_DD9')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_757',
    )

    ChrTalk(
        0x00FE,
        (
            '平时这个时候定期船总会从我头上经过，\n',
            '今天却没来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '航运全部停止的传言\n',
            '看来是真的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_757(): pass

    label('loc_757')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_7F2',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，差不多到交班的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结束这里的执勤后，\n',
            '进入里面享受清爽的空气，\n',
            '心情真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好就没有去食堂喝一杯了，\n',
            '今天就去怀念一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_7F2(): pass

    label('loc_7F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_957',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这里偶尔也会有\n',
            '学者之类的人前来调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来这里果然是\n',
            '非常古老的遗迹呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对有兴趣的人来说，\n',
            '也许是一个不可思议的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我这个没有学问的人来说，\n',
            '这里除了是工作场所以外，一无是处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_954')

    def _loc_8CF(): pass

    label('loc_8CF')

    ChrTalk(
        0x00FE,
        (
            '这里偶尔也会有\n',
            '学者之类的人前来调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来这里果然是\n',
            '非常古老的遗迹呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对有兴趣的人来说，\n',
            '也许是一个不可思议的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_954(): pass

    label('loc_954')

    Jump('loc_DD9')

    def _loc_957(): pass

    label('loc_957')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_B58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AD6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '就在不久之前， \n',
            '我的女儿还来这里玩过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到我说在这里工作的时候，\n',
            '她可是非常羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小孩子这么率直，真好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在白天很温暖，\n',
            '但是冬天的晚上在这里执勤的话，\n',
            '可真的是非常痛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '又暗，又冷，风又强，\n',
            '皮肤冻裂，鼻涕也停不下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，夏天的白天热得不行，\n',
            '连意识都会模糊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，可以眺望到好风景，\n',
            '的确是让人欣喜的一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B55')

    def _loc_AD6(): pass

    label('loc_AD6')

    ChrTalk(
        0x00FE,
        (
            '就在不久之前， \n',
            '我的女儿还来这里玩过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到我说在这里工作的时候，\n',
            '她可是非常羡慕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小孩子这么率直，真好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B55(): pass

    label('loc_B55')

    Jump('loc_DD9')

    def _loc_B58(): pass

    label('loc_B58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_C05',
    )

    ChrTalk(
        0x00FE,
        (
            '今天没有什么特别异常的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都这边和洛连特那边\n',
            '不管什么时候都很平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '１０年前这座城墙外\n',
            '帝国大军的铁蹄到处肆虐，\n',
            '如今实在无法想象当年的情景啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_C05(): pass

    label('loc_C05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D54',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎来到亚宁堡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们到这里来，\n',
            '是观光还是来调查遗迹？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这座城墙将格兰赛尔地区\n',
            '整个围绕起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前的诗中曾说过，王都是颗珍珠，\n',
            '亚宁堡是将珍珠包起来的贝壳，\n',
            '好像就是这么比喻的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它已经十分古旧了，\n',
            '但至今人们仍没有弄明白\n',
            '建造这座长城的用意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了防止敌人侵入的说法，\n',
            '现在来看是最有力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_D54(): pass

    label('loc_D54')

    ChrTalk(
        0x00FE,
        (
            '这座城墙将格兰赛尔地区\n',
            '整个围绕起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前的诗中曾说过，王都是颗珍珠，\n',
            '亚宁堡是将珍珠包起来的贝壳，\n',
            '好像就是这么比喻的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DD9(): pass

    label('loc_DD9')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
