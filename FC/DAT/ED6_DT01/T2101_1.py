import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2101_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2101.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
    TalkBegin(0x000F)

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x2000)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_274',
    )

    OP_28(0x0021, 0x01, 0x2000)

    ChrTalk(
        0x00FE,
        (
            '#1800170578V哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170579V关于委托的事情有点不好意思，\n',
            '因为钥匙我已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151307V#004F啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170581V果然就掉在\n',
            '『亚克罗萨』附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170582V这样的话，\n',
            '我就把委托撤销了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170583V真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170584V#000F嗯，没关系的。\n',
            '反正钥匙找到就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170585V是啊，现在我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170586V那如果以后钥匙又丢掉的话，\n',
            '我会和你们再联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170587V#509F……拜托你保管好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D1')

    def _loc_274(): pass

    label('loc_274')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x0200)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x8000)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3BE',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170233V#000F您好啊，哈古先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170234V我们有件事想问问您……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B7')

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_357',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170235V#010F您正在工作啊，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170236V有件事情想请教您。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B7')

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170237V#040F对不起，哈古先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170238V有件事情想向您打听一下……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B7(): pass

    label('loc_3B7')

    Call(1, 0x0001)

    Jump('loc_12D1')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C8F',
    )

    EventBegin(0x00)
    OP_28(0x0021, 0x04, 0x04)
    OP_28(0x0021, 0x04, 0x08)
    OP_28(0x0021, 0x01, 0x0001)
    OP_28(0x0021, 0x01, 0x0002)
    LoadEffect(0x00, 'map\\\\mp022_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0x00FF, 0, 0, 0, 0)
    OP_65(0x00, 0x0001)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170411V#000F打扰一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170412V叔叔您是叫哈古吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_525')

    def _loc_48D(): pass

    label('loc_48D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E5',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170413V#010F对不起，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170414V请问您是哈古先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_525')

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_525',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170415V#040F对不起，\n',
            '请问您是哈古先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_525(): pass

    label('loc_525')

    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170416V嗯，\n',
            '我就是哈古没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1800170417V啊！\n',
            '难道你们是游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170418V#006F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170419V#010F您好像把仓库的钥匙弄丢了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170420V嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170421V不久之前，\n',
            '我把起重机周围的\n',
            '那些木桶都搬进了仓库……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170422V似乎在搬完折返的途中，\n',
            '钥匙就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_7B7',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170423V#505F……嗯？\n',
            '起重机周围的木桶？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170424V#002F喂，约修亚。\n',
            '那个该不会是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170425V#010F嗯，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170426V是那个卡片上所写的可疑的木桶吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170427V#010F…………对不起，\n',
            '请继续说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170428V哦，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B7(): pass

    label('loc_7B7')

    ChrTalk(
        0x00FE,
        (
            '#1800170429V我记得\n',
            '在『亚克罗萨』里喝酒的时候，\n',
            '钥匙还好好地带在身上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170430V我想很可能\n',
            '就掉在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_917',
    )

    ChrTalk(
        0x00FE,
        (
            '#1800170431V嗯，\n',
            '我知道的线索差不多就是这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170432V#010F我们会作为参考的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170433V那么，如果有什么新的发现，\n',
            '我们会再与您联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170434V哦，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170435V回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    TalkEnd(0x000F)

    Jump('loc_C8C')

    def _loc_917(): pass

    label('loc_917')

    ChrTalk(
        0x00FE,
        (
            '#1800170436V因为刚才心情很愉快，\n',
            '就在这儿周围散步，\n',
            '可能就是那个时候弄丢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x00FE, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170437V#004F！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170438V喝醉酒之后\n',
            '还在海港这里走来走去？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170439V如果掉进海里那可怎么办啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170440V没办法啊，\n',
            '海风吹得我心情很好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010170441V#007F唉，真是无话可说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_AB7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170442V#045F……说的是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE9')

    def _loc_AB7(): pass

    label('loc_AB7')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_AE9',
    )

    ChrTalk(
        0x0136,
        (
            '#0060170442V#045F……说的是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE9(): pass

    label('loc_AE9')

    ChrTalk(
        0x00FE,
        (
            '#1800170444V因为这样的原因，\n',
            '应该就是掉在这个海港的某处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170445V#505F嗯，那就只有在这附近转转，\n',
            '看看能不能找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170446V#010F说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1800170447V啊，\n',
            '我不能再在这儿偷懒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170448V那么我就去继续工作了。\n',
            '如果找到了就通知我一声！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170449V#010F如果有什么新的发现，\n',
            '我们会再与您联络的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170434V哦，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    TalkEnd(0x000F)

    def _loc_C8C(): pass

    label('loc_C8C')

    Jump('loc_12D1')

    def _loc_C8F(): pass

    label('loc_C8F')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12CA',
    )

    EventBegin(0x00)
    OP_4A(0x000F, 255)
    OP_28(0x0021, 0x04, 0x10)
    OP_28(0x0021, 0x01, 0x0020)
    RemoveItem(0x0334, 1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E5A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170549V#000F哈古先生，\n',
            '打扰一下可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170550V是关于钥匙的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V对了，怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E57')

    def _loc_D4B(): pass

    label('loc_D4B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCF',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170552V#010F您正在工作啊，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170553V哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V对了，那件事怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E57')

    def _loc_DCF(): pass

    label('loc_DCF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E57',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170555V#040F对不起，哈古先生。\n',
            '打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170553V哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V对了，那件事怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E57(): pass

    label('loc_E57')

    Jump('loc_105B')

    def _loc_E5A(): pass

    label('loc_E5A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F4F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170558V#508F呀嗬～哈古先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170559V喂、喂！         \n',
            '你太大声了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170560V会被我的同事听到的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170561V#008F啊……对、对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170562V可是，钥匙那件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V哦，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105B')

    def _loc_F4F(): pass

    label('loc_F4F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FD3',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170552V#010F您正在工作啊，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170553V哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V对了，那件事怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105B')

    def _loc_FD3(): pass

    label('loc_FD3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_105B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170555V#040F对不起，哈古先生。\n',
            '打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170553V哦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170551V对了，那件事怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_105B(): pass

    label('loc_105B')

    ChrTalk(
        0x0101,
        (
            '#0010170570V#006F嗯，已经找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170571V是这把钥匙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '仓库的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170572V哦，\n',
            '就是它就是它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170573V哎呀～辛苦你们了。\n',
            '真是帮了我大忙啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170574V……可是这钥匙\n',
            '怎么会被钓鱼线缠住的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170575V#506F啊哈哈，\n',
            '这个的原因嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170576V嗯……算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170577V好了，那就这样吧。\n',
            '谢谢了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【仓库的钥匙】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x01, 0x8000)"),
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12C5',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170239V#014F啊，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170240V我们有件事想问问您。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)
    Call(1, 0x0001)

    def _loc_12C5(): pass

    label('loc_12C5')

    EventEnd(0x01)

    Jump('loc_12D1')

    def _loc_12CA(): pass

    label('loc_12CA')

    TalkEnd(0x000F)
    Call(0, 0x0006)

    def _loc_12D1(): pass

    label('loc_12D1')

    TalkEnd(0x000F)

    Return()

# id: 0x0001 offset: 0x12D5
@scena.Code('func_01_12D5')
def func_01_12D5():
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170241V问我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170242V什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170243V#010F我们想问问您\n',
            '刚才钥匙掉了的时候您所说的那件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170244V『把起重机周围的那些木桶\n',
            '　都搬进了仓库』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170245V……是这样的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170246V啊，对呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170247V起重机附近的\n',
            '木桶很碍事的，\n',
            '所以我就把它们搬进仓库里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170248V之后没多久\n',
            '钥匙就丢失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170249V#010F对不起，\n',
            '能不能让我们进一下仓库呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170250V我们有点事情，\n',
            '想调查一下里面的木桶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170251V唔……使用中的仓库\n',
            '在出入管理方面是很严格的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170252V因为那是一个\n',
            '放置着很多商品的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170253V所以外部人员\n',
            '是不能随意进出的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170254V#505F哎呀…………\n',
            '这可就不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170255V不过，\n',
            '既然你们刚才帮过我，\n',
            '我就稍微通融一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170256V就只是调查一下\n',
            '相关的木桶对吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170257V#010F嗯，就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170258V那么我就把它\n',
            '搬到仓库外来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170259V这样既不用进入仓库，\n',
            '又可以调查木桶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170260V#508F啊，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170261V#010F真是给您添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170262V你们不用这么客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170263V好了，那么我们就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(2000)
    OP_6C(135000, 0)

    @scena.Lambda('lambda_1745')
    def lambda_1745():
        CameraMove(23520, 1000, 4150, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1745)

    ChrSetPos(0x00FE, 23520, 1000, 4150, 180)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.PushLong, 0x5BE0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.PushLong, 0x3E8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.PushLong, 0x1036),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0102, 180, 0)

    ExecExpressionWithValue(
        0x0101,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.PushLong, 0x9C4),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0101, 180, 0)

    ExecExpressionWithValue(
        0x0105,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.PushLong, 0x12C),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0105,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0105,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.PushLong, 0xC80),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0105, 180, 0)
    OP_0D()
    Sleep(2000)

    OP_6F(0x0015, 0)
    OP_70(0x0015, 60)
    OP_73(0x0015)
    OP_6F(0x0015, 60)
    Sleep(1000)

    @scena.Lambda('lambda_1848')
    def lambda_1848():
        CameraMove(22780, 0, 5890, 2000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1848)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(400)

    ChrMoveToRelative(0x00FE, 0, 0, 1000, 1000, 0x00)
    WaitForThreadExit(0x0018, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#1800170264V#1P好，打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170265V#1P你们就先在这里\n',
            '等我一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18D6')
    def lambda_18D6():
        CameraMove(23920, 500, 4380, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_18D6)

    ChrClearFlags(0x0018, 0x0080)
    ChrWalkTo(0x0018, 23540, 1000, 4000, 1000, 0x00)
    ChrClearFlags(0x0018, 0x0004)
    OP_4A(0x0018, 255)
    WaitForThreadExit(0x0010, 0x0001)
    ChrSetDirection(0x00FE, 180, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x00FE,
        (
            '#1800170266V#1P咦？波尔多斯主任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170267V#1P您在这里面\n',
            '做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170268V#2P唔，我只是有点不放心，\n',
            '所以来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170269V#2P我用备用钥匙进去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170270V#1P啊？备用钥匙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170271V#1P奇怪了，\n',
            '有这样的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170272V#2P……对了，\n',
            '那边的几位是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170273V#1P啊，他们是游击士协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170274V#1P因为要调查一件事，\n',
            '所以要看看仓库里面的木桶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170275V#2P哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170276V#2P不过，保管中的仓库\n',
            '是不允许外部人员进入的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 180, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170277V#1P嗯，所以我才来\n',
            '帮他们把木桶取出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170278V#1P只是把木桶搬出来\n',
            '应该可以吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170279V#2P啊，那就没问题了。\n',
            '要协助调查嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170280V#2P唔，\n',
            '竟然可以找到这个地方来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170281V#2P虽然还很年轻，\n',
            '不过你们都是很优秀的游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170282V#1P#001F嘿嘿⊙\n',
            '您过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170283V#2P如果有什么不明白的，\n',
            '尽管问哈古就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170284V#2P那么我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170285V#1P辛苦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D0E')
    def lambda_1D0E():
        ChrTurnDirection(0x00FE, 0x0018, 0)
        Yield()

        Jump('lambda_1D0E')

    DispatchAsync2(0x00FE, 0x0001, lambda_1D0E)

    @scena.Lambda('lambda_1D1F')
    def lambda_1D1F():
        ChrTurnDirection(0x0101, 0x0018, 0)
        Yield()

        Jump('lambda_1D1F')

    DispatchAsync2(0x0101, 0x0001, lambda_1D1F)

    @scena.Lambda('lambda_1D30')
    def lambda_1D30():
        ChrTurnDirection(0x0102, 0x0018, 0)
        Yield()

        Jump('lambda_1D30')

    DispatchAsync2(0x0102, 0x0001, lambda_1D30)

    @scena.Lambda('lambda_1D41')
    def lambda_1D41():
        ChrTurnDirection(0x0105, 0x0018, 0)
        Yield()

        Jump('lambda_1D41')

    DispatchAsync2(0x0105, 0x0001, lambda_1D41)

    ChrSetFlags(0x0018, 0x0040)
    ChrWalkTo(0x0018, 28170, 0, 8540, 2000, 0x00)
    ChrWalkTo(0x0018, 29620, 1000, 14400, 2000, 0x00)
    ChrSetFlags(0x0018, 0x0080)
    TerminateThread(0x00FE, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)

    @scena.Lambda('lambda_1D94')
    def lambda_1D94():
        ChrSetDirection(0x0000, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1D94)

    @scena.Lambda('lambda_1DA2')
    def lambda_1DA2():
        ChrSetDirection(0x0001, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1DA2)

    @scena.Lambda('lambda_1DB0')
    def lambda_1DB0():
        ChrSetDirection(0x0002, 180, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1DB0)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(400)

    @scena.Lambda('lambda_1DCA')
    def lambda_1DCA():
        ChrSetDirection(0x0000, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1DCA)

    @scena.Lambda('lambda_1DD8')
    def lambda_1DD8():
        ChrSetDirection(0x0001, 180, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1DD8)

    ChrSetDirection(0x0002, 180, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170286V#1P好了，\n',
            '我这就帮你们把木桶拿出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(23740, 0, 5560, 0)
    OP_72(0x001D, 0x0004)
    OP_71(0x001D, 0x0002)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetPos(0x00FE, 23550, 500, 4740, 180)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetDirection(0x0102, 180, 0)
    ChrSetDirection(0x0105, 180, 0)
    ChrSetDirection(0x00FE, 180, 0)
    Sleep(800)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(800)

    OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000003E8, 0x00)
    OP_4A(0x00FE, 255)
    ChrClearFlags(0x00FE, 0x0040)
    Sleep(400)

    ChrSetDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170287V#1P呼～～久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170288V#1P你们要的木桶已经拿来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170289V#004F哇～～\n',
            '还真不小呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F2F')
    def lambda_1F2F():
        CameraMove(24500, 1000, 3980, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1F2F)

    CreateThread(0x0102, 0x01, 0x01, 0x0002)
    CreateThread(0x0105, 0x01, 0x01, 0x0003)
    CreateThread(0x00FE, 0x01, 0x01, 0x0004)
    ChrWalkTo(0x0101, 24540, 500, 4710, 1000, 0x00)
    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0010, 0x0001)
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170290V#000F#1P您一个人就能把它搬出来啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170291V#1P呵呵，对我们这些海港男儿来说，\n',
            '这都是些家常便饭啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)
    OP_63(0x0102)
    Sleep(800)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170292V#014F#2P艾丝蒂尔，\n',
            '这里又有一张卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2097')
    def lambda_2097():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2097)

    @scena.Lambda('lambda_20A5')
    def lambda_20A5():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_20A5)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170293V#004F#1P啊，真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_20E2')
    def lambda_20E2():
        CameraMove(23220, 500, 4740, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_20E2)

    CreateThread(0x0101, 0x01, 0x01, 0x0006)
    ChrSetDirection(0x0102, 45, 400)
    ChrSetDirection(0x0105, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170294V',
            (TxtCtl.SetColor, 0x0),
            '『唔，十分抱歉。\n',
            '　木桶被运走是我的失误。\n',
            '　\n',
            '　不过，一旦找到仓库的钥匙，\n',
            '　就可以顺藤摸瓜找到这里。\n',
            '　看来你们已经揭示出了真相。\n',
            '　\n',
            TxtCtl.Enter,
            '#0170170295V　作为奖赏，寻找的物品将完璧归赵。\n',
            '　你们调查这个木桶之中即可。\n',
            '　如果可以的话，\n',
            '　务必将烛台归还给其真正的主人。\n',
            '　\n',
            '　……嗯，时间已到。\n',
            '　期待我们的再次相会。\n',
            '　　　　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010170296V#003F#1P真、真是讨厌啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170297V就好像是从很近的地方\n',
            '一直观察着我们的行动一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170298V#043F的确是这样呢…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170299V#014F#2P咦，这张卡片……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170300V……上面的墨迹还没有干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060170302V#044F#4P#1K…………！？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010170301V#004F#1P#1K哎！？',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()
    ChrSetPos(0x0018, 31010, 0, 9300, 119)
    ChrClearFlags(0x0018, 0x0080)

    @scena.Lambda('lambda_2471')
    def lambda_2471():
        CameraMove(25540, 0, 5950, 2000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_2471)

    ChrWalkTo(0x0018, 29040, 0, 6510, 2000, 0x00)
    ChrSetDirection(0x0018, 270, 0)
    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0018, 26410, 0, 6450, 3000, 0x00)
    Sleep(400)

    ChrTalk(
        0x0018,
        (
            '#1810170303V喂，\n',
            '你们在这里做什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_251B')
    def lambda_251B():
        ChrTurnDirection(0x0000, 0x0018, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_251B)

    @scena.Lambda('lambda_2529')
    def lambda_2529():
        ChrTurnDirection(0x0001, 0x0018, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2529)

    @scena.Lambda('lambda_2537')
    def lambda_2537():
        ChrTurnDirection(0x0002, 0x0018, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2537)

    ChrTurnDirection(0x00FE, 0x0018, 400)

    ChrTalk(
        0x00FE,
        (
            '#1800170304V啊！？\n',
            '波、波尔多斯主任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1800170305V刚才您不是\n',
            '已经同意了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0018,
        (
            '#1810170306V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#1810170307V你在说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020170308V#012F#2P糟糕，被骗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_263A')
    def lambda_263A():
        CameraMove(24290, 500, 4740, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_263A)

    @scena.Lambda('lambda_2652')
    def lambda_2652():
        ChrTurnDirection(0x0105, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2652)

    @scena.Lambda('lambda_2660')
    def lambda_2660():
        ChrTurnDirection(0x0018, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_2660)

    @scena.Lambda('lambda_266E')
    def lambda_266E():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_266E)

    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010170309V#004F#1P难、难道是！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170310V刚才在这里的波尔多斯主任……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170311V#012F#2P是假扮的…………\n',
            '虽然相貌非常相似。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170312V犯人变装之后把卡片的内容更换了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170313V#043F#4P怎么会…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170314V#005F#1P赶、赶快追上去啊！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_27A7')
    def lambda_27A7():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_27A7')

    DispatchAsync2(0x00FE, 0x0001, lambda_27A7)

    @scena.Lambda('lambda_27B8')
    def lambda_27B8():
        ChrTurnDirection(0x0018, 0x0101, 0)
        Yield()

        Jump('lambda_27B8')

    DispatchAsync2(0x0018, 0x0001, lambda_27B8)

    @scena.Lambda('lambda_27C9')
    def lambda_27C9():
        ChrTurnDirection(0x0105, 0x0101, 0)
        Yield()

        Jump('lambda_27C9')

    DispatchAsync2(0x0105, 0x0001, lambda_27C9)

    @scena.Lambda('lambda_27DA')
    def lambda_27DA():
        ChrTurnDirection(0x0102, 0x0101, 0)
        Yield()

        Jump('lambda_27DA')

    DispatchAsync2(0x0102, 0x0001, lambda_27DA)

    @scena.Lambda('lambda_27EB')
    def lambda_27EB():
        ChrWalkTo(0x0101, 29790, 520, 13040, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27EB)

    OP_62(0x0018, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    ChrTalk(
        0x0105,
        (
            '#0060170315V#044F#4P啊！\n',
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x00FE, 0x01)
    TerminateThread(0x0018, 0x01)

    ChrTalk(
        0x0102,
        (
            '#0020170316V#014F#2P竟然就这样追上去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170317V#042F#4P约修亚，\n',
            '我们怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170318V#013F#2P虽然很遗憾，\n',
            '不过已经太迟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170319V那个伪装者离开的时候\n',
            '我们就已经输了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170320V#015F#2P大概艾丝蒂尔\n',
            '连犯人的影子也看不到吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170321V#043F是……这样啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170322V#012F#2P更重要的是，\n',
            '要先确认一下烛台是否还完好。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170323V与逮捕犯人相比，\n',
            '委托人更希望能够找回烛台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170324V#042F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170325V按照卡片写的，\n',
            '应该就在这个木桶里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170326V#010F#2P嗯，\n',
            '但愿真是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2AA1')
    def lambda_2AA1():
        ChrWalkTo(0x0018, 24900, 0, 6900, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_2AA1)

    @scena.Lambda('lambda_2ABC')
    def lambda_2ABC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2ABC)

    Sleep(400)

    @scena.Lambda('lambda_2ACF')
    def lambda_2ACF():
        ChrSetDirection(0x0102, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2ACF)

    ChrWalkTo(0x0105, 23450, 500, 4770, 1000, 0x00)
    ChrSetDirection(0x0105, 180, 400)
    Sleep(800)

    OP_62(0x0018, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    WaitForThreadExit(0x0018, 0x0001)
    Sleep(800)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170327V#018F#2P唉，真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170328V艾丝蒂尔赶快回来吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    ChrSetPos(0x00FE, 4620, -1800, 22750, 270)
    OP_4B(0x000F, 255)
    ChrSetFlags(0x0018, 0x0080)
    OP_71(0x001D, 0x0004)
    OP_28(0x0020, 0x01, 0x0200)
    NewScene('ED6_DT01/T2210._SN', 100, 0, 0)
    IdleLoop()
    EventEnd(0x00)
    TalkEnd(0x000F)

    Return()

# id: 0x0002 offset: 0x2BBF
@scena.Code('func_02_2BBF')
def func_02_2BBF():
    ChrWalkTo(0x0102, 22500, 1000, 3990, 1000, 0x00)
    ChrSetDirection(0x0102, 90, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    Return()

# id: 0x0003 offset: 0x2BED
@scena.Code('func_03_2BED')
def func_03_2BED():
    ChrWalkTo(0x0105, 22570, 0, 5330, 1000, 0x00)
    ChrWalkTo(0x0105, 22650, 250, 4930, 1000, 0x00)
    ChrSetDirection(0x0105, 135, 400)

    Return()

# id: 0x0004 offset: 0x2C1D
@scena.Code('func_04_2C1D')
def func_04_2C1D():
    ChrWalkTo(0x00FE, 23560, 0, 6650, 1000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0005 offset: 0x2C39
@scena.Code('func_05_2C39')
def func_05_2C39():
    ChrWalkTo(0x0102, 22670, 750, 4540, 2000, 0x00)
    ChrSetDirection(0x0102, 90, 400)

    Return()

# id: 0x0006 offset: 0x2C55
@scena.Code('func_06_2C55')
def func_06_2C55():
    ChrWalkTo(0x0101, 23870, 500, 4710, 2000, 0x00)
    ChrSetDirection(0x0101, 225, 400)

    Return()

# id: 0x0007 offset: 0x2C71
@scena.Code('func_07_2C71')
def func_07_2C71():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D55',
    )

    ChrTurnDirectionByPos(0x0000, 41070, 34470, 0)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170471V#002F（虽然很在意，\n',
            '　不过现在不赶快去仓库的话……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D4F')

    def _loc_2CE1(): pass

    label('loc_2CE1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D4F',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170472V#012F（没有时间再去别的地方了。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170473V（……赶快去最深处的仓库吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D4F(): pass

    label('loc_2D4F')

    TalkEnd(0x00FF)

    Jump('loc_32F9')

    def _loc_2D55(): pass

    label('loc_2D55')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_2E38',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_2D6F',
    )

    Call(1, 0x0008)

    Jump('loc_2E35')

    def _loc_2D6F(): pass

    label('loc_2D6F')

    ChrTalk(
        0x0101,
        (
            '#0010170474V#003F唔～掉进水里的到底是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170475V#013F如果可以的话最好调查一下，\n',
            '可是不知道该从何做起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170476V#505F如果有什么带钩的工具，\n',
            '就可以把它捞出来了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    def _loc_2E35(): pass

    label('loc_2E35')

    Jump('loc_32F9')

    def _loc_2E38(): pass

    label('loc_2E38')

    EventBegin(0x00)
    OP_28(0x0021, 0x01, 0x0004)
    OP_62(0x0000, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirectionByPos(0x0000, 41040, 1107513836, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EC2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010170451V#004F…………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170452V刚才那里好像有什么东西在发光……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2EC2(): pass

    label('loc_2EC2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F1A',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170453V#014F…………嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170454V好像有什么东西在发光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2F1A(): pass

    label('loc_2F1A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F72',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170455V#044F啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170456V刚才好像有什么东西在发光？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F72(): pass

    label('loc_2F72')

    Fade(1000)
    ChrSetPos(0x0101, 41040, -1650, 31310, 0)
    ChrSetPos(0x0102, 42040, -1650, 31230, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2FBA',
    )

    ChrSetPos(0x0105, 40040, -1650, 31130, 0)

    Jump('loc_2FD8')

    def _loc_2FBA(): pass

    label('loc_2FBA')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2FD8',
    )

    ChrSetPos(0x0136, 40040, -1650, 31130, 0)

    def _loc_2FD8(): pass

    label('loc_2FD8')

    CameraMove(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170457V#004F哎呀，果然，\n',
            '水里面好像有东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170458V#013F亮闪闪的东西，是什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170459V有可能是哈古先生想找的东西，\n',
            '如果可以的话最好调查一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3187',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170460V#043F可是，该怎么做呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170461V虽说跳下去看可能太夸张了点，\n',
            '但如果不确认一下的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170462V#505F嗯～是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170463V如果有什么带钩的工具就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E8')

    def _loc_3187(): pass

    label('loc_3187')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3253',
    )

    ChrTalk(
        0x0136,
        (
            '#0060170460V#043F可是，该怎么做呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170461V虽说跳下去看可能太夸张了点，\n',
            '但如果不确认一下的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170462V#505F嗯～是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170463V如果有什么带钩的工具就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E8')

    def _loc_3253(): pass

    label('loc_3253')

    ChrTalk(
        0x0101,
        (
            '#0010170468V#505F可是，该怎么做呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170469V虽说跳下去看可能太夸张了点，\n',
            '不确认一下的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170463V如果有什么带钩的工具就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32E8(): pass

    label('loc_32E8')

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_32F7',
    )

    Call(1, 0x0008)

    Jump('loc_32F9')

    def _loc_32F7(): pass

    label('loc_32F7')

    EventEnd(0x00)

    def _loc_32F9(): pass

    label('loc_32F9')

    Return()

# id: 0x0008 offset: 0x32FA
@scena.Code('func_08_32FA')
def func_08_32FA():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 41040, -1650, 31430, 0)
    ChrSetPos(0x0102, 42040, -1650, 31230, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3344',
    )

    ChrSetPos(0x0105, 40040, -1650, 31130, 0)

    Jump('loc_3362')

    def _loc_3344(): pass

    label('loc_3344')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3362',
    )

    ChrSetPos(0x0136, 40040, -1650, 31130, 0)

    def _loc_3362(): pass

    label('loc_3362')

    CameraMove(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170474V#003F唔～掉进水里的到底是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170475V#013F如果可以的话最好调查一下，\n',
            '可是不知道该从何做起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170476V#505F如果有什么带钩的工具，\n',
            '就可以把它捞出来了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170494V#004F啊，对了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    Fade(1000)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(25000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetPos(0x0101, 41040, -2000, 31900, 0)
    ChrSetChipByIndex(0x0101, 15)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170495V#001F怎～么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170496V#014F原来如此。\n',
            '是用钓钩把它钩上来吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170497V可是很不容易做到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170498V#502F嘿嘿嘿，\n',
            '现在就让你见识下\n',
            '艾丝蒂尔姐姐华丽的技巧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170499V#017F好吧好吧。\n',
            '我就等着你的表演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_363A',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170500V#040F艾丝蒂尔，加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170221V#508F哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3690')

    def _loc_363A(): pass

    label('loc_363A')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3690',
    )

    ChrTurnDirection(0x0136, 0x0101, 400)

    ChrTalk(
        0x0136,
        (
            '#0060170500V#040F艾丝蒂尔，加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170221V#508F哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3690(): pass

    label('loc_3690')

    Sleep(100)

    Fade(1000)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    PlaySE(132, 0x00, 0x64)
    OP_99(0x0101, 0x00, 0x06, 1500)
    Sleep(400)

    PlaySE(25, 0x00, 0x64)
    Sleep(1200)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x0101)
    Sleep(700)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    TerminateThread(0x0101, 0xFF)
    OP_99(0x0101, 0x06, 0x03, 1500)
    StopEffect(0x00, 0x00)
    OP_84(0x00)
    PlaySE(24, 0x00, 0x64)
    OP_99(0x0101, 0x03, 0x01, 1500)
    Sleep(1000)

    OP_99(0x0101, 0x10, 0x12, 1500)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '仓库的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrJumpTo(0x0101, 41040, -1650, 31430, 600, 3000)
    ChrClearFlags(0x0101, 0x0004)
    Sleep(400)

    @scena.Lambda('lambda_37B3')
    def lambda_37B3():
        OP_94(0x01, 0x0101, 0x0000, 0xFFFFFED4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37B3)

    Fade(1000)
    CameraMove(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170504V#508F你看你看！钓到了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0334, 1)
    OP_28(0x0021, 0x01, 0x0010)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170505V#014F艾丝蒂尔，你好厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170506V真没想到你居然对这个也如此在行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170507V#009F哼，\n',
            '听你的语气好像不是在称赞我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170508V#000F不过，运气不错呢。\n',
            '这个好像就是哈古\n',
            '先生所说的仓库的钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170509V#010F呵呵，\n',
            '竟然掉到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3992',
    )

    ChrTalk(
        0x0105,
        (
            '#0060170510V#040F呵呵，\n',
            '这样子哈古先生也可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39D9')

    def _loc_3992(): pass

    label('loc_3992')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_39D9',
    )

    ChrTalk(
        0x0136,
        (
            '#0060170510V#040F呵呵，\n',
            '这样子哈古先生也可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39D9(): pass

    label('loc_39D9')

    ChrTalk(
        0x0101,
        (
            '#0010170512V#000F我们把它交给哈古先生吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170513V#010F嗯，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x3A3A
@scena.Code('func_09_3A3A')
def func_09_3A3A():
    OP_28(0x0020, 0x01, 0x8000)
    OP_28(0x0020, 0x01, 0x0020)
    OP_64(0x01, 0x0001)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 20100, 0, 28900, 270)
    ChrSetPos(0x0102, 21200, 0, 29300, 270)
    ChrSetPos(0x0105, 22300, 0, 27900, 270)
    OP_6C(315000, 0)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 2000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010170182V#002F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170183V真奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170184V#014F#2P所谓『钢铁之鹤』应该\n',
            '就是指这个起重机吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170185V#043F不过却没看到最重要的『木桶』啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170186V#009F可恶，\n',
            '到底怎么回事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0101, 0x0015, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170187V#501F啊，那边那位大哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C05')
    def lambda_3C05():
        ChrTurnDirection(0x0102, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3C05)

    @scena.Lambda('lambda_3C13')
    def lambda_3C13():
        ChrTurnDirection(0x0105, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3C13)

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x15, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x15, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x15, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 2000)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0015, 0x0101, 400)
    OP_4A(0x0015, 255)

    ChrTalk(
        0x0015,
        (
            '#1790170188V哦，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170189V#501F你在这附近看到过木桶吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1790170190V木桶？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1790170191V那种东西\n',
            '我也记不太清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1790170192V不过每一个仓库里面都有木桶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0015, 255)
    ChrSetDirection(0x0015, 270, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_40B2',
    )

    OP_28(0x0020, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#0010170193V#505F#1P唔，这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170194V…………嗯？仓库？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 2000)
    OP_62(0x0105, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0105, 0x0101, 400)

    @scena.Lambda('lambda_3E29')
    def lambda_3E29():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3E29)

    ChrTalk(
        0x0105,
        (
            '#0060170195V#044F有什么发现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170196V#505F#1P嗯…………\n',
            '等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170197V#002F喂，\n',
            '我们之前不是找到过仓库的钥匙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170198V#010F#2P嗯…………\n',
            '哈古先生曾经委托过我们帮他找钥匙。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170199V#002F#1P那个人不是说过的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170200V起重机周围的那些木桶\n',
            '都被搬进仓库里面去了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020170201V#014F#2P对啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170202V原来这里的木桶\n',
            '都被搬运到仓库里面去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170203V#010F一定是这样没错。\n',
            '头脑很灵敏嘛，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170204V#001F#1P嘿嘿，偶尔啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170205V好，\n',
            '我们这就去问问哈古先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46EE')

    def _loc_40B2(): pass

    label('loc_40B2')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_4489',
    )

    OP_28(0x0020, 0x01, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010170193V#505F#1P唔，这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170207V……嗯？仓库？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 2000)
    OP_62(0x0105, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0105, 0x0101, 400)

    @scena.Lambda('lambda_4187')
    def lambda_4187():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4187)

    ChrTalk(
        0x0105,
        (
            '#0060170195V#044F有什么发现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170196V#505F#1P嗯…………\n',
            '等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170210V#002F#1P我说，\n',
            '之前我们不是听说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170211V#010F#2P嗯……\n',
            '哈古先生曾经委托过我们帮他找钥匙。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170212V仓库的钥匙丢失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170213V#002F#1P是啊是啊。\n',
            '那个人不是说过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170200V起重机周围的那些木桶\n',
            '都被搬进仓库里面去了…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020170201V#014F#2P对啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170202V原来这里的木桶\n',
            '都被搬运到仓库里面去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170217V#010F一定是这样没错。\n',
            '头脑很灵敏嘛，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170218V#001F#1P嘿嘿，偶尔啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170219V#010F#2P好，\n',
            '那么我们先把哈古先生的委托解决掉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170220V这样的话，\n',
            '事情就应该有所进展了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170221V#508F哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46EE')

    def _loc_4489(): pass

    label('loc_4489')

    OP_28(0x0020, 0x01, 0x0040)

    ChrTalk(
        0x0101,
        (
            '#0010170222V#505F#1P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170223V唉，真是不好办啊。\n',
            '线索就这样中断了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0010,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0010, 2000)

    @scena.Lambda('lambda_4530')
    def lambda_4530():
        ChrTurnDirection(0x0105, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4530)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170224V#013F#2P如果有关于木桶的消息就好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170225V可是我们目前\n',
            '也没有这方面的线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170226V#003F#1P可是，\n',
            '在这种地方发愁也没有用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170227V#010F#2P不如我们先去接受其他的任务吧？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170228V说不定会得到什么线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170229V#006F#1P嗯，就这样办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170230V当然，这件事也不能放弃，\n',
            '要继续调查下去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170231V#010F#2P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170232V好，我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46EE(): pass

    label('loc_46EE')

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x46F1
@scena.Code('func_0A_46F1')
def func_0A_46F1():
    If(
        (
            (Expr.Eval, "OP_40(0x0334)"),
            Expr.Return,
        ),
        'loc_4DC9',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C58',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48D3',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_47B6',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170514V#014F我说，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170515V说起来，\n',
            '还没有把仓库的钥匙交给哈古先生吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170516V#010F而且钓鱼竿也还没有还回去呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4816')

    def _loc_47B6(): pass

    label('loc_47B6')

    ChrTalk(
        0x0102,
        (
            '#0020170514V#014F我说，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170518V说起来，\n',
            '还没有把仓库的钥匙交给哈古先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4816(): pass

    label('loc_4816')

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170519V#008F啊，忘得一干二净了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170520V#010F出发之前去还了吧。\n',
            '哈古先生肯定正在港口工作吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170521V#006F嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C55')

    def _loc_48D3(): pass

    label('loc_48D3')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A89',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_497B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150766V#014F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170523V还没有把仓库的钥匙交给哈古先生吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170516V#010F而且钓鱼竿也还没有还回去呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49D3')

    def _loc_497B(): pass

    label('loc_497B')

    ChrTalk(
        0x0102,
        (
            '#0020150766V#014F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170526V还没有把仓库的钥匙交给哈古先生吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49D3(): pass

    label('loc_49D3')

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170519V#008F啊，忘得一干二净了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170528V#010F出发之前去还了吧。\n',
            '哈古先生应该在港口那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170521V#006F嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C55')

    def _loc_4A89(): pass

    label('loc_4A89')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C55',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_4B31',
    )

    ChrTalk(
        0x0102,
        (
            '#0020150766V#014F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170523V还没有把仓库的钥匙交给哈古先生吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170516V#010F而且钓鱼竿也还没有还回去呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B89')

    def _loc_4B31(): pass

    label('loc_4B31')

    ChrTalk(
        0x0102,
        (
            '#0020150766V#014F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170526V还没有把仓库的钥匙交给哈古先生吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B89(): pass

    label('loc_4B89')

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170519V#008F啊，忘得一干二净了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170536V#044F那么就先去哈古先生那里吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170537V#010F嗯，对啊。\n',
            '哈古先生应该正在港口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C55(): pass

    label('loc_4C55')

    Jump('loc_4DAB')

    def _loc_4C58(): pass

    label('loc_4C58')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CD7',
    )

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170538V#010F出发之前，\n',
            '把仓库的钥匙交给哈古先生把。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170539V哈古先生应该在港口那里的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DAB')

    def _loc_4CD7(): pass

    label('loc_4CD7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D2B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020170540V#010F先把仓库的钥匙交给哈古先生，\n',
            '然后再出发吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DAB')

    def _loc_4D2B(): pass

    label('loc_4D2B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DAB',
    )

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170538V#010F先把仓库的钥匙交给哈古先生，\n',
            '然后再出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170539V哈古先生应该在港口那里的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DAB(): pass

    label('loc_4DAB')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_4F22')

    def _loc_4DC9(): pass

    label('loc_4DC9')

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_4F22',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EA6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020170543V#010F对了，\n',
            '从酒吧借的钓鱼竿还没还，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170544V出发之前去还了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170545V#505F嗯～\n',
            '是在港口的酒吧借来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170546V#040F嗯，是『亚克罗萨』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F07')

    def _loc_4EA6(): pass

    label('loc_4EA6')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170547V#010F从港口的酒吧借来的钓鱼竿还没还。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170548V出发之前去还了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F07(): pass

    label('loc_4F07')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_4F22(): pass

    label('loc_4F22')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
