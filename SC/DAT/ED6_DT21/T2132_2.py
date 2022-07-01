import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2132_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2132_2 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2132.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x22D0
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
            word_30         = 35,
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
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_106',
    )

    TalkBegin(0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    ChrTalk(
        0x0010,
        (
            '刚才开始\n',
            '外边就吵闹得很厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '……有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 346, 0)
    TalkEnd(0x0010)

    Jump('loc_16A')

    def _loc_106(): pass

    label('loc_106')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x0008)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_126',
    )

    EventBegin(0x00)
    OP_4A(0x0010, 255)
    Call(2, 0x0006)

    Jump('loc_16A')

    def _loc_126(): pass

    label('loc_126')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_143',
    )

    EventBegin(0x00)
    OP_4A(0x0010, 255)
    Call(2, 0x0005)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Jump('loc_16A')

    def _loc_143(): pass

    label('loc_143')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_160',
    )

    EventBegin(0x00)
    OP_4A(0x0010, 255)
    Call(2, 0x0002)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Jump('loc_16A')

    def _loc_160(): pass

    label('loc_160')

    TalkBegin(0x0010)
    Call(2, 0x0001)
    TalkEnd(0x0010)

    def _loc_16A(): pass

    label('loc_16A')

    Return()

# id: 0x0001 offset: 0x16B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1AA',
    )

    ChrTalk(
        0x0010,
        (
            '我在等人\n',
            '但怎么也不来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呼，就不能快点吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AF')

    def _loc_1AA(): pass

    label('loc_1AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_25A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_206',
    )

    ChrTalk(
        0x0010,
        (
            '据说近来危险的魔兽很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '自己１个人\n',
            '去调查实在是不行的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257')

    def _loc_206(): pass

    label('loc_206')

    OP_A2(0x0007)

    ChrTalk(
        0x0010,
        (
            '听协会的消息\n',
            '据说近来危险的魔兽很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '最好避免\n',
            '一个人走在大道上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_257(): pass

    label('loc_257')

    Jump('loc_2AF')

    def _loc_25A(): pass

    label('loc_25A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2AF',
    )

    OP_8C(0x0010, 346, 0)

    ChrTalk(
        0x0010,
        (
            '嗯～照相机准备了\n',
            '备用感光结晶回路也买了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '……好，准备ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AF(): pass

    label('loc_2AF')

    Return()

# id: 0x0002 offset: 0x2B0
@scena.Code('ReInit')
def ReInit():
    Call(2, 0x0007)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_312',
    )

    ChrTalk(
        0x0010,
        (
            '#2930430130V咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430132V难道\n',
            '其它的事已经完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A4')

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_362',
    )

    ChrTalk(
        0x0010,
        (
            '#2930430131V啊，是游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430133V已经有空闲了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A4')

    def _loc_362(): pass

    label('loc_362')

    ChrTalk(
        0x0101,
        (
            '#0010430120V#1011F对了，打扰一下行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0010, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#2930430121V好的，有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430122V#1015F我们看了公告板来的，\n',
            '您是森特先生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#2930430123V啊，是游击士们吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430124V呀～等候多时了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430125V我想马上拜托你们点事，\n',
            '现在有时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A4(): pass

    label('loc_4A4')

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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_522',
    )

    OP_28(0x0066, 0x01, 0x0001)
    OP_28(0x0066, 0x01, 0x0002)
    OP_28(0x0066, 0x04, 0x04)
    OP_28(0x0066, 0x04, 0x08)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_51B',
    )

    Call(2, 0x0004)

    Jump('loc_51F')

    def _loc_51B(): pass

    label('loc_51B')

    Call(2, 0x0003)

    def _loc_51F(): pass

    label('loc_51F')

    Jump('loc_730')

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_5DF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430134V#1007F嗯～抱歉。\n',
            '还不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430135V哎呀呀，是吗？\n',
            '唉，没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430136V如果有空闲了\n',
            '请再来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430137V#1000F嗯、我们会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_730')

    def _loc_5DF(): pass

    label('loc_5DF')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_684',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430138V#1015F嗯～还不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430139V哎呀呀，还不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430140V有空的话\n',
            '再拜托你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430141V#1007F嗯，抱歉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_730')

    def _loc_684(): pass

    label('loc_684')

    OP_28(0x0066, 0x01, 0x8000)

    ChrTalk(
        0x0101,
        (
            '#0010430126V#1007F啊，抱歉。\n',
            '现在不太方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430127V哎呀呀，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430128V那么，如果有空闲了\n',
            '再拜托你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430129V#1006F嗯，好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_730(): pass

    label('loc_730')

    Call(2, 0x0008)

    Return()

# id: 0x0003 offset: 0x735
@scena.Code('func_03_735')
def func_03_735():
    ChrTalk(
        0x0101,
        (
            '#0010430142V#1006F嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430143V那么，是怎样的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430144V嗯，想拜托你们去\n',
            '拍摄『绀碧之塔』的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430145V希望你们去塔顶，\n',
            '把某样东西拍下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_857',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430146V#050F说到『绀碧之塔』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430147V是说在阿伊纳街道岔路上，\n',
            '古代遗迹的塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BC')

    def _loc_857(): pass

    label('loc_857')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_8BC',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430148V#020F绀碧之塔就是指……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430149V是说在阿伊纳街道岔路上的\n',
            '古代遗迹塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BC(): pass

    label('loc_8BC')

    ChrTalk(
        0x0010,
        (
            '#2930430150V没错。\n',
            '知道得真清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430151V#1011F不过，为什么\n',
            '需要塔的照片呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430152V#1018F啊，难道是新办的杂志社吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430153V不不，不是啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430154V我是王都历史资料馆\n',
            '派遣来的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430155V所以，这次的调查\n',
            '是学术上的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_A23',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430156V#030F呼，学术调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4F')

    def _loc_A23(): pass

    label('loc_A23')

    ChrTalk(
        0x0101,
        (
            '#0010430157V#1008F是吗，是学术调查啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A4F(): pass

    label('loc_A4F')

    ChrTalk(
        0x0010,
        (
            '#2930430158V对，是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430159V……不过，这次调查\n',
            '稍微有点特别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430160V#1011F……特别？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_B2A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430161V#053F嗯，关于这个\n',
            '以后再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430162V#050F总之现在\n',
            '确认工作内容优先。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B91')

    def _loc_B2A(): pass

    label('loc_B2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B91',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430163V#026F嗯，关于这个\n',
            '以后再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430164V#020F总之现在\n',
            '确认工作内容优先哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B91(): pass

    label('loc_B91')

    SetChrName('森特')

    ChrTalk(
        0x0010,
        (
            '#2930430165V哦，对不起。\n',
            '跑题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430166V嗯～说到哪里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BE6')
    def lambda_0BE6():
        ChrTurnDirection(0x00F7, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0BE6)

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430167V#1011F要爬上塔顶，\n',
            '拍摄某样东西啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430168V#1015F……那个，『某样东西』是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430169V是塔顶上的『谜之装置』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430170V虽是古代文明的遗物，\n',
            '用途却完全不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430171V因此没办法，我们研究者\n',
            '仅仅称之为『装置』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430172V#1011F塔顶上的装置……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430173V就是那个台座一样的机械？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_E80',
    )

    ChrTalk(
        0x0010,
        (
            '#2930430174V咦，你知道吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430175V对对，就是那个。\n',
            '确实是像台座一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430176V#1002F嗯，其实我已经去看过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430177V总觉得那个『装置』，\n',
            '放射着奇怪的光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430178V嗯嗯，我知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430179V资料馆里也收到了\n',
            '可靠的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D5')

    def _loc_E80(): pass

    label('loc_E80')

    ChrTalk(
        0x0010,
        (
            '#2930430174V咦，你知道吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430175V对对，就是那个。\n',
            '确实是像台座一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430182V#1001F啊，果然是说那个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430183V虽然好像已经不能动了，\n',
            '但的的确确是『装置』的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430184V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430185V不，那其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430186V好像也不是这么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430187V#1011F咦？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430188V那个『装置』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430189V……好像还在动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430190V#1004F在、在动吗……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430191V那个奇怪的机械！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430192V是，我们也收到了\n',
            '可靠的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430193V误报的可能性很低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D5(): pass

    label('loc_10D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_112B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211830V#053F原来如此啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430195V#050F所以才急忙来调查吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1177')

    def _loc_112B(): pass

    label('loc_112B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1177',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430196V#027F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430197V所以才突然来调查吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1177(): pass

    label('loc_1177')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_12DB',
    )

    ChrTalk(
        0x0010,
        (
            '#2930430198V是、是的，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430199V总而言之有必要\n',
            '记录『装置』的现状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430200V#1003F确实很诡异……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430201V虽然现在那个『装置』\n',
            '好像还没有危险性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430202V但要发生什么也不足为奇。\n',
            '请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430203V#1002F嗯，我们不会大意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430204V那么，拍下了『装置』\n',
            '再回到这里就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_149D')

    def _loc_12DB(): pass

    label('loc_12DB')

    ChrTalk(
        0x0010,
        (
            '#2930430198V是、是的，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430206V总而言之\n',
            '有必要确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430207V#1002F确实很诡异……\n',
            '不能放任不理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1396',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430208V#050F『装置』没有危险吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C8')

    def _loc_1396(): pass

    label('loc_1396')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_13C8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430209V#022F『装置』没有危险吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C8(): pass

    label('loc_13C8')

    ChrTalk(
        0x0010,
        (
            '#2930430210V是，目前的状况来说\n',
            '『装置』本身没有危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430211V当然，即使如此\n',
            '也不能断言说很安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430212V#1002F嗯，我们会多加小心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430213V那么，摄影结束以后\n',
            '再回到这里就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_149D(): pass

    label('loc_149D')

    ChrTalk(
        0x0010,
        (
            '#2930430214V嗯嗯，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430215V现在借给你们的照相机\n',
            '也请在那时还给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 346, 400)
    Sleep(1000)

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_92(0x0010, 0x0101, 0x000002BC, 0x000007D0, 0x00)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#2930430216V那么，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力照相机'], 1)
    Sleep(400)

    OP_8F(0x0010, -46277, 0, 4360, 1000, 0x00)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430217V#1016F好、好大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x26)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_16D2',
    )

    ChrTalk(
        0x0127,
        (
            '#0280430218V#150F嗯～因为是拍摄\n',
            '记录照片的高级机型嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0127, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430219V#1011F咦，是很好的相机吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430220V#151F嘿嘿，真是\n',
            '坦率的好孩子啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430221V#1007F好、好孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1703')

    def _loc_16D2(): pass

    label('loc_16D2')

    ChrTalk(
        0x0010,
        (
            '#2930430222V那当然啦。\n',
            '是机械部件的组合嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1703(): pass

    label('loc_1703')

    ChrTalk(
        0x0010,
        (
            '#2930430223V啊，感光结晶回路\n',
            '已经设置好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430224V只要按下快门\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430225V#1000F嗯，了解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430226V#1015F那，再确认一次\n',
            '工作内容……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430227V到『绀碧之塔』的塔顶上去，\n',
            '拍下那里的『装置』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430228V然后再返回这里，\n',
            '归还这个相机就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430229V嗯嗯，就按这个程序走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430230V啊，还有一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430231V尽量避免设计的角度，\n',
            '照片的构图麻烦简单一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430232V怎么说都是资料用的照片，\n',
            '可以的话请从正面拍摄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430233V#1000F避免设计的角度\n',
            '简单点就好？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430234V#1000F……原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430235V等你们的好照片。\n',
            '那么，请小心注意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 346, 0)

    Return()

# id: 0x0004 offset: 0x1995
@scena.Code('func_04_1995')
def func_04_1995():
    ChrTalk(
        0x0010,
        (
            '#2930430236V嗯，大致的情况\n',
            '已经说明了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430237V#1011F嗯，已经听过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430238V#1015F以防万一，还是\n',
            '确认一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430227V到『绀碧之塔』的塔顶上去，\n',
            '拍下那里的『装置』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430240V然后再返回这里，\n',
            '归还借的照相机就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430229V嗯嗯，就按这个程序吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430242V那么请拿好照相机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0010, 0x0101, 0x000002BC, 0x000007D0, 0x00)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力照相机'], 1)
    Sleep(400)

    OP_8F(0x0010, -46277, 0, 4360, 1000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#2930430243V那么，请小心注意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430244V期待你们的照片哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430245V#1006F嗯，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0010, 346, 0)

    Return()

# id: 0x0005 offset: 0x1BCA
@scena.Code('func_05_1BCA')
def func_05_1BCA():
    Call(2, 0x0007)

    ChrTalk(
        0x0010,
        (
            '#2930430246V哎呀，怎么了？',
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
            TXT(0x00, '【确认工作内容】\n'),
            TXT(0x01, '【取消委托】\n'),
            TXT(0x02, '【没什么】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1C68'),
        (0x00000001, 'loc_1DB8'),
        (-1, 'loc_1F6A'),
    )

    def _loc_1C68(): pass

    label('loc_1C68')

    ChrTalk(
        0x0010,
        (
            '#2930430247V希望你们拍摄的，\n',
            '是在『绀碧之塔』塔顶上\n',
            '像台座一样形状的『装置』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430248V『绀碧之塔』在阿伊纳街道途中\n',
            '向南拐弯的岔道前面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430249V照片要避开设计的角度，\n',
            '构图麻烦简单一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430250V毕竟是资料用的东西嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430251V如果顺利拍摄好了，\n',
            '再请返回这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430252V那么，请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FA2')

    def _loc_1DB8(): pass

    label('loc_1DB8')

    OP_28(0x0066, 0x03, 0x08)
    OP_28(0x0066, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010430253V#1007F抱歉，稍微\n',
            '有点事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430254V哎呀呀……\n',
            '要取消委托吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430255V嗯～真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430256V#1000F总之，\n',
            '先归还照相机吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0010, 0x000002BC, 0x000007D0, 0x00)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '归还了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['导力照相机'], 1)
    Sleep(400)

    OP_8F(0x0101, -45180, 0, 3650, 1000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#2930430257V事情办完了\n',
            '就再来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2930430258V但是，请赶快哟。\n',
            '还有下一项调查计划呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370418V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FA2')

    def _loc_1F6A(): pass

    label('loc_1F6A')

    ChrTalk(
        0x0010,
        (
            '#2930430260V『装置』的原形还不明。\n',
            '请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FA2')

    def _loc_1FA2(): pass

    label('loc_1FA2')

    Call(2, 0x0008)

    Return()

# id: 0x0006 offset: 0x1FA7
@scena.Code('func_06_1FA7')
def func_06_1FA7():
    Call(2, 0x0007)

    ChrTalk(
        0x00FE,
        (
            '#2930430416V哦哦，诸位。\n',
            '正等着你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2930430417V照片拍好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430418V#1001F嗯，顺利完成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430419V#1011F啊，对了。\n',
            '首先得归还照相机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0010, 0x000002BC, 0x000007D0, 0x00)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力照相机']),
            (TxtCtl.SetColor, 0x0),
            '归还了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['导力照相机'], 1)
    Sleep(400)

    OP_8F(0x0101, -45180, 0, 3650, 1000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#2930430420V……嗯，确实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2930430421V那么，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430422V#1004F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430423V要去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2930430424V当然是\n',
            '导力器工房啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2930430425V得去冲洗\n',
            '感光结晶回路才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430426V#1016F啊～是这么回事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430427V#1006F嗯，那么\n',
            '马上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2120._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x21FB
@scena.Code('func_07_21FB')
def func_07_21FB():
    Fade(1000)
    OP_6D(-45110, 0, 4019, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x26)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_222F',
    )

    SetChrPos(0x0127, -43820, 0, 3580, 307)

    def _loc_222F(): pass

    label('loc_222F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_224D',
    )

    SetChrPos(0x0104, -43810, 0, 2360, 299)

    def _loc_224D(): pass

    label('loc_224D')

    SetChrPos(0x0101, -45180, 0, 3650, 289)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2279',
    )

    SetChrPos(0x0106, -44880, 0, 2770, 280)

    Jump('loc_2291')

    def _loc_2279(): pass

    label('loc_2279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2291',
    )

    SetChrPos(0x0103, -44880, 0, 2770, 280)

    def _loc_2291(): pass

    label('loc_2291')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x0066, 0x01, 0x8000)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x08)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_22B2',
    )

    ChrTurnDirection(0x0010, 0x0101, 0)

    def _loc_22B2(): pass

    label('loc_22B2')

    OP_0D()

    Return()

# id: 0x0008 offset: 0x22B4
@scena.Code('func_08_22B4')
def func_08_22B4():
    OP_30(0x00)
    OP_8C(0x0010, 346, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
