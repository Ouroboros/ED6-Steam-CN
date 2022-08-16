import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4121_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4121.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('func_01_65')
def func_01_65():
    Return()

# id: 0x0002 offset: 0x66
@scena.Code('func_02_66')
def func_02_66():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_73',
    )

    Jump('loc_2AD')

    def _loc_73(): pass

    label('loc_73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_7D',
    )

    Jump('loc_2AD')

    def _loc_7D(): pass

    label('loc_7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_17B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            Expr.Return,
        ),
        'loc_F1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120141542V#812F作战一旦开始，\n',
            '就没有回旋余地了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141543V所以趁现在\n',
            '赶快整理好装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178')

    def _loc_F1(): pass

    label('loc_F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Return,
        ),
        'loc_178',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120141540V#854F事态很严重啊，\n',
            '刚才一时手足无措，\n',
            '现在终于弄明白情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141541V出了这么大的事，\n',
            '的确让人紧张啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178(): pass

    label('loc_178')

    Jump('loc_2AD')

    def _loc_17B(): pass

    label('loc_17B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_185',
    )

    Jump('loc_2AD')

    def _loc_185(): pass

    label('loc_185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_18F',
    )

    Jump('loc_2AD')

    def _loc_18F(): pass

    label('loc_18F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_199',
    )

    Jump('loc_2AD')

    def _loc_199(): pass

    label('loc_199')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1E3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120141544V#850F好～的，今天也一样，\n',
            '工作、比赛都要努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD')

    def _loc_1E3(): pass

    label('loc_1E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1ED',
    )

    Jump('loc_2AD')

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1F7',
    )

    Jump('loc_2AD')

    def _loc_1F7(): pass

    label('loc_1F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_242',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120141547V#850F哟，是两位新人啊，\n',
            '找到金大哥了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A3')

    def _loc_242(): pass

    label('loc_242')

    ChrTalk(
        0x00FE,
        (
            '#0120141545V#850F哟，是两位新人啊，\n',
            '找到金大哥了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120141546V我很期待\n',
            '和你们的对战哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A3(): pass

    label('loc_2A3')

    Jump('loc_2AD')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2AD',
    )

    def _loc_2AD(): pass

    label('loc_2AD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x2B1
@scena.Code('func_03_2B1')
def func_03_2B1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    Jump('loc_A37')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    Jump('loc_A37')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_3B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            Expr.Return,
        ),
        'loc_331',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141550V#830F突入的任务就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141551V没问题，\n',
            '你们一定能办到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B5')

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 3, 0x64B)),
            Expr.Return,
        ),
        'loc_3B5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141548V#832F这么大的一宗委托\n',
            '我也是第一次碰到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141549V这次只许成功不许失败，\n',
            '必须制定严密的作战计划才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B5(): pass

    label('loc_3B5')

    Jump('loc_A37')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_4E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_446',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141560V#831F真是很值得一看的比赛呢，\n',
            '对我们也很有参考价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141561V真想什么时候有机会\n',
            '和你们一起执行任务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E6')

    def _loc_446(): pass

    label('loc_446')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320141557V#831F呀，恭喜你们获胜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141558V真是很值得一看的比赛呢，\n',
            '对我们也很有参考价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141559V真想什么时候有机会\n',
            '和你们一起执行任务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E6(): pass

    label('loc_4E6')

    Jump('loc_A37')

    def _loc_4E9(): pass

    label('loc_4E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_4F3',
    )

    Jump('loc_A37')

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_610',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_568',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141552V#830F你们明天要参加决赛吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141556V作为游击士协会的代表，\n',
            '不要给协会蒙羞哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D')

    def _loc_568(): pass

    label('loc_568')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320141552V#830F你们明天要参加决赛吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141553V作为游击士协会的代表，\n',
            '不要给协会蒙羞哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141554V#835F不过，其实这些话\n',
            '也用不着对现在的你们说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60D(): pass

    label('loc_60D')

    Jump('loc_A37')

    def _loc_610(): pass

    label('loc_610')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_65C',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141562V#831F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141563V今天也要\n',
            '鼓足干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A37')

    def _loc_65C(): pass

    label('loc_65C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_9CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_6BC',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141577V#830F艾丝蒂尔、约修亚，\n',
            '我从现在开始就期待着\n',
            '能和你们交手哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C8')

    def _loc_6BC(): pass

    label('loc_6BC')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '#0320141564V#831F呀，是你们啊。\n',
            '恭喜你们首战告捷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141565V哈哈，\n',
            '你们没有想到会和\n',
            '渡鸦帮那群家伙交手吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141566V#505F是、是啊……\n',
            '吃了一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141567V#006F不过自从那次之后，\n',
            '他们已经有很大的变化了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141568V#019F是啊，他们如果能改过自身，\n',
            '说不定会成为像阿加特前辈那样的游击士了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141569V#009F哼……\n',
            '那样的家伙有一个都已经嫌多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320141570V#833F呵呵，\n',
            '虽然他们也很努力，\n',
            '但说实话让我吃惊的是你们呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320141571V#830F虽说通过卢安支部\n',
            '听说了你们的活跃表现，\n',
            '但实力的成长已经超出了我的想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141572V#008F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141573V让卡露娜姐姐这样一称赞，\n',
            '我都有些不好意思了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320141574V#831F哈哈，\n',
            '我非常期待和你们交手哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141575V#001F嗯，我也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020141576V#010F到时候还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C8(): pass

    label('loc_9C8')

    Jump('loc_A37')

    def _loc_9CB(): pass

    label('loc_9CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A26',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320141578V那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320141579V比赛之前就去找些\n',
            '通缉魔兽热一热身吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A37')

    def _loc_A26(): pass

    label('loc_A26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_A30',
    )

    Jump('loc_A37')

    def _loc_A30(): pass

    label('loc_A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A37',
    )

    def _loc_A37(): pass

    label('loc_A37')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xA3B
@scena.Code('func_04_A3B')
def func_04_A3B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_A48',
    )

    Jump('loc_D75')

    def _loc_A48(): pass

    label('loc_A48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_A52',
    )

    Jump('loc_D75')

    def _loc_A52(): pass

    label('loc_A52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_B4A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            Expr.Return,
        ),
        'loc_AD5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310141582V#824F情报部竟然也采取\n',
            '扣押人质这种低级的手段……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141583V#822F一定要将\n',
            '公主殿下他们救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B47')

    def _loc_AD5(): pass

    label('loc_AD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Return,
        ),
        'loc_B47',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310141580V#822F那位理查德上校\n',
            '竟然是政变的策划人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141581V没想到，\n',
            '我们一直被蒙在鼓里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B47(): pass

    label('loc_B47')

    Jump('loc_D75')

    def _loc_B4A(): pass

    label('loc_B4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_B54',
    )

    Jump('loc_D75')

    def _loc_B54(): pass

    label('loc_B54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_B5E',
    )

    Jump('loc_D75')

    def _loc_B5E(): pass

    label('loc_B5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_C61',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_BD7',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310141587V#820F今天我们虽然输了，\n',
            '但比赛本身一点也不让我后悔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141586V你们决赛可要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5E')

    def _loc_BD7(): pass

    label('loc_BD7')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0310141584V#820F哦，是你们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141585V今天我们虽然输了，\n',
            '但比赛本身一点也不让我后悔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141586V你们决赛可要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5E(): pass

    label('loc_C5E')

    Jump('loc_D75')

    def _loc_C61(): pass

    label('loc_C61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_C6B',
    )

    Jump('loc_D75')

    def _loc_C6B(): pass

    label('loc_C6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_D5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_CD2',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310141592V#821F连你们在内，\n',
            '明天全都是劲敌啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141591V我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D57')

    def _loc_CD2(): pass

    label('loc_CD2')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0310141589V#821F哟，今天辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141590V连你们在内，\n',
            '明天不管遇到那一组，都是强敌呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310141591V我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D57(): pass

    label('loc_D57')

    Jump('loc_D75')

    def _loc_D5A(): pass

    label('loc_D5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D64',
    )

    Jump('loc_D75')

    def _loc_D64(): pass

    label('loc_D64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_D6E',
    )

    Jump('loc_D75')

    def _loc_D6E(): pass

    label('loc_D6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_D75',
    )

    def _loc_D75(): pass

    label('loc_D75')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xD79
@scena.Code('func_05_D79')
def func_05_D79():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D86',
    )

    Jump('loc_1042')

    def _loc_D86(): pass

    label('loc_D86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_D90',
    )

    Jump('loc_1042')

    def _loc_D90(): pass

    label('loc_D90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_E80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 0, 0x650)),
            Expr.Return,
        ),
        'loc_DF5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330141596V#840F这次作战是我们\n',
            '孤注一掷的选择。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141597V所以一定要成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_DF5(): pass

    label('loc_DF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Return,
        ),
        'loc_E7D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330141594V#845F不好意思，\n',
            '刚才让你们见笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141595V虽说有点在意自己的记忆，\n',
            '但现在必须集中精力完成女王陛下的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7D(): pass

    label('loc_E7D')

    Jump('loc_1042')

    def _loc_E80(): pass

    label('loc_E80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_FFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F13',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330141601V#840F你们这样年轻的游击士\n',
            '能获得武术大会的优胜，\n',
            '对我们来说更是种激励。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141602V我也要更加\n',
            '努力修炼才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FFC')

    def _loc_F13(): pass

    label('loc_F13')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0330141598V#840F呀，恭喜你们获胜。\n',
            '那场比赛真是非常精彩刺激哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141599V你们这样年轻的游击士\n',
            '能获得武术大会的优胜，\n',
            '对我们来说更是种激励。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330141600V你们这样年轻的游击士\n',
            '能获得武术大会的优胜，\n',
            '对我们来说更是种激励。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FFC(): pass

    label('loc_FFC')

    Jump('loc_1042')

    def _loc_FFF(): pass

    label('loc_FFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1009',
    )

    Jump('loc_1042')

    def _loc_1009(): pass

    label('loc_1009')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1013',
    )

    Jump('loc_1042')

    def _loc_1013(): pass

    label('loc_1013')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_101D',
    )

    Jump('loc_1042')

    def _loc_101D(): pass

    label('loc_101D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1027',
    )

    Jump('loc_1042')

    def _loc_1027(): pass

    label('loc_1027')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1031',
    )

    Jump('loc_1042')

    def _loc_1031(): pass

    label('loc_1031')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_103B',
    )

    Jump('loc_1042')

    def _loc_103B(): pass

    label('loc_103B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1042',
    )

    def _loc_1042(): pass

    label('loc_1042')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
