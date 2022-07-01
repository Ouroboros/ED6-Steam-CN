import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3111_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3111_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x43D2
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
    SetChrPos(0x0101, -116560, -4000, -111330, 180)
    SetChrPos(0x00F7, -115650, -4000, -111150, 180)
    SetChrPos(0x00F8, -116560, -4000, -110220, 180)
    SetChrPos(0x00F9, -115500, -4000, -110020, 180)
    OP_8C(0x000E, 0, 0)
    OP_4A(0x000E, 0)
    OP_69(0x0101, 0x00000000)
    OP_6D(-116200, -4000, -111770, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 3, 0x142B)),
            Expr.Return,
        ),
        'loc_232',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450893V#1011F菲小姐，打扰一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450894V哎呀，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450895V难道\n',
            '是工作的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450896V#1006F嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450897V有事情想要问哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450898V咦，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450899V什么事，说说看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_448')

    def _loc_232(): pass

    label('loc_232')

    ChrTalk(
        0x00FE,
        (
            '#1980450894V哎呀，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450901V好久不见，还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450902V#1001F啊，菲小姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450903V#1000F嗯，真是好久不见了啊。\n',
            '菲小姐最近怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450904V哈哈，我还是和以前一样\n',
            '每天忙得要死。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_37B',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980450905V多亏你们\n',
            '不过和布拉姆重新和好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450906V总之，感觉还算是很充实啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B6')

    def _loc_37B(): pass

    label('loc_37B')

    ChrTalk(
        0x00FE,
        (
            '#1980450907V这里的输出也很顺利，\n',
            '地下工厂没有休息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B6(): pass

    label('loc_3B6')

    ChrTalk(
        0x00FE,
        (
            '#1980450908V你们也在\n',
            '这里工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450909V#1006F嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450910V跟你说，其实那件工作\n',
            '想问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450911V哎，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_448(): pass

    label('loc_448')

    ChrTalk(
        0x0101,
        (
            '#0010450912V#1015F能不能\n',
            '看一下这个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把布卢布兰留下的\n',
            '信息笔记给菲看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#1980450913V安静的地下……\n',
            '女神……之后是字符串吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450914V……这怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_587',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450915V#050F好像是在\n',
            '说这里……\n',
            '但是有些地方搞不明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450916V想着你可能知道\n',
            '就来找你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F5')

    def _loc_587(): pass

    label('loc_587')

    ChrTalk(
        0x0103,
        (
            '#0030450917V#020F好像是在\n',
            '说这个地方……\n',
            '但是有些地方搞不明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450918V想着你可能知道\n',
            '就来找你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F5(): pass

    label('loc_5F5')

    ChrTalk(
        0x00FE,
        (
            '#1980450919V这个文章\n',
            '是说地下工厂吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450920V那，那么可能是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450921V#1002F想到什么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450922V这，这个女神\n',
            '难道是说我！？',
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
            '#0010450923V#1016F不，这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450924V实、实在抱歉\n',
            '这个就别管了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450925V先不说这个，\n',
            '还有搞不明白的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980450926V啊……抱、抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450927V嗯，是这个字符串吧。\n',
            '『Ｃ－２６Ｄ－Ｅ』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450928V看起来的感觉，像是管理用的\n',
            '产品序号似的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450929V#1011F产品序号？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8EB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450930V#064F我也不太清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450931V就是存放在仓库里的东西\n',
            '所带的序号吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450932V嗯，仓库里的物品\n',
            '全部都是用这个序号来管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450933V所以只要知道序号\n',
            '不管什么都能用传送带送出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_961')

    def _loc_8EB(): pass

    label('loc_8EB')

    ChrTalk(
        0x00FE,
        (
            '#1980450934V嗯，这个序号是仓库里\n',
            '所有物品都有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450933V所以只要知道序号\n',
            '不管什么都能用传送带送出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_961(): pass

    label('loc_961')

    ChrTalk(
        0x0101,
        (
            '#0010450936V#1015F这么说……\n',
            '这个号码的东西也能送出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450937V当然能了。\n',
            '要不试试看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9FC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450938V#050F可以的话就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A27')

    def _loc_9FC(): pass

    label('loc_9FC')

    ChrTalk(
        0x0103,
        (
            '#0030450939V#020F可以的话就麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A27(): pass

    label('loc_A27')

    ChrTalk(
        0x00FE,
        (
            '#1980450940V小事一桩。\n',
            '稍等片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_0A55')
    def lambda_0A55():
        OP_6D(-114050, -4000, -110140, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0A55)

    @scena.Lambda('lambda_0A6D')
    def lambda_0A6D():
        ChrTurnDirection(0x0101, 0x000E, 400)
        Yield()

        Jump('lambda_0A6D')

    DispatchAsync2(0x0101, 0x0001, lambda_0A6D)

    @scena.Lambda('lambda_0A7E')
    def lambda_0A7E():
        ChrTurnDirection(0x00F7, 0x000E, 400)
        Yield()

        Jump('lambda_0A7E')

    DispatchAsync2(0x00F7, 0x0001, lambda_0A7E)

    @scena.Lambda('lambda_0A8F')
    def lambda_0A8F():
        ChrTurnDirection(0x00F8, 0x000E, 400)
        Yield()

        Jump('lambda_0A8F')

    DispatchAsync2(0x00F8, 0x0001, lambda_0A8F)

    @scena.Lambda('lambda_0AA0')
    def lambda_0AA0():
        ChrTurnDirection(0x00F9, 0x000E, 400)
        Yield()

        Jump('lambda_0AA0')

    DispatchAsync2(0x00F9, 0x0001, lambda_0AA0)

    OP_8E(0x00FE, -116160, -4000, -112400, 2000, 0x00)
    OP_8E(0x00FE, -113390, -4000, -111160, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980450941V我是菲。\n',
            '能打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450942V产品序号Ｃ－２６Ｄ－Ｅ\n',
            '麻烦送来这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450943V对，Ｃ－２６Ｄ－Ｅ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980450944V……谢了，拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980450945V有那个号码的物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450946V说是现在就送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450947V#1004F真、真的有吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450948V好像那边的负责人\n',
            '也吓了一大跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450949V好～了，会有什么过来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00A0, 0x01, 0x64)
    OP_76(0x00FF, 0x00000016, 0x0001, 0x00000002, 0x00000000, 0x000003E8, 0x00, 0x00)
    Sleep(1000)

    OP_8C(0x00FE, 90, 400)

    @scena.Lambda('lambda_0CA9')
    def lambda_0CA9():
        OP_6D(-109200, -4000, -110660, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0CA9)

    @scena.Lambda('lambda_0CC1')
    def lambda_0CC1():
        OP_67(0, 6920, -10000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0CC1)

    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x01, 0x0002)
    Sleep(600)

    CreateThread(0x0101, 0x01, 0x01, 0x0001)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x01, 0x0003)
    Sleep(1000)

    CreateThread(0x00F9, 0x01, 0x01, 0x0004)
    WaitForThreadExit(0x00F9, 0x0001)
    TerminateThread(0x000E, 0x00)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    CreateThread(0x000E, 0x03, 0x01, 0x000D)
    OP_A6(0x0011)

    @scena.Lambda('lambda_0D30')
    def lambda_0D30():
        ChrTurnDirection(0x0000, 0x0013, 400)
        Yield()

        Jump('lambda_0D30')

    DispatchAsync2(0x0000, 0x0001, lambda_0D30)

    @scena.Lambda('lambda_0D41')
    def lambda_0D41():
        ChrTurnDirection(0x0001, 0x0013, 400)
        Yield()

        Jump('lambda_0D41')

    DispatchAsync2(0x0001, 0x0001, lambda_0D41)

    @scena.Lambda('lambda_0D52')
    def lambda_0D52():
        ChrTurnDirection(0x0002, 0x0013, 400)
        Yield()

        Jump('lambda_0D52')

    DispatchAsync2(0x0002, 0x0001, lambda_0D52)

    @scena.Lambda('lambda_0D63')
    def lambda_0D63():
        ChrTurnDirection(0x0003, 0x0013, 400)
        Yield()

        Jump('lambda_0D63')

    DispatchAsync2(0x0003, 0x0001, lambda_0D63)

    @scena.Lambda('lambda_0D74')
    def lambda_0D74():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_0D74')

    DispatchAsync2(0x00FE, 0x0001, lambda_0D74)

    ChrTalk(
        0x0101,
        (
            '#0010450950V#1011F啊，好像来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450951V嗯？那是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450952V好像见过\n',
            '又好像没见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0003)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)
    TerminateThread(0x0002, 0x01)
    TerminateThread(0x0003, 0x01)
    TerminateThread(0x00FE, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450953V#1007F啊～太好了。\n',
            '终－于找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1980450954V……啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450955V难、难不成这个\n',
            '是游击士协会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450956V#1007F嗯，就是那个难不成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EE7')
    def lambda_0EE7():
        OP_6D(-109730, -4000, -110940, 1000)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0EE7)

    @scena.Lambda('lambda_0EFF')
    def lambda_0EFF():
        ChrTurnDirection(0x00F7, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0EFF)

    Sleep(150)

    @scena.Lambda('lambda_0F12')
    def lambda_0F12():
        ChrTurnDirection(0x00F8, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F12)

    Sleep(100)

    ChrTurnDirection(0x00F9, 0x000E, 400)
    WaitForThreadExit(0x00F9, 0x0000)
    WaitForThreadExit(0x000E, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_F71',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450957V#051F#1P多亏你帮大忙了。\n',
            '多谢帮忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA8')

    def _loc_F71(): pass

    label('loc_F71')

    ChrTalk(
        0x0103,
        (
            '#0030450958V#021F#1P多亏你帮大忙了。\n',
            '多谢帮忙啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA8(): pass

    label('loc_FA8')

    ChrTurnDirection(0x000E, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '#1980450959V这、这个先不说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980450960V为什么协会的招牌\n',
            '会在我们的仓库里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450961V#1016F嗯、嗯～……\n',
            '从哪里开始说明好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450962V说来就话长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x142B)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T3100._SN', 110, 0, 0)
    IdleLoop()

    Return()

# id: 0x0001 offset: 0x107A
@scena.Code('Init')
def Init():
    OP_8E(0x00FE, -113280, -4000, -112010, 2000, 0x00)
    OP_8E(0x00FE, -109580, -4000, -111040, 2000, 0x00)
    OP_8E(0x00FE, -109200, -4000, -110660, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0002 offset: 0x10BE
@scena.Code('ReInit')
def ReInit():
    OP_8E(0x00FE, -113280, -4000, -112010, 2000, 0x00)
    OP_8E(0x00FE, -110380, -4000, -110660, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0003 offset: 0x10EE
@scena.Code('func_03_10EE')
def func_03_10EE():
    OP_8E(0x00FE, -114100, -4000, -112010, 2000, 0x00)
    OP_8E(0x00FE, -109200, -4000, -112180, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0004 offset: 0x111E
@scena.Code('func_04_111E')
def func_04_111E():
    OP_8E(0x00FE, -114100, -4000, -112010, 2000, 0x00)
    OP_8E(0x00FE, -110380, -4000, -112180, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0005 offset: 0x114E
@scena.Code('func_05_114E')
def func_05_114E():
    EventBegin(0x00)
    Call(1, 0x000E)

    ChrTalk(
        0x0008,
        (
            '#3160450257V欢迎光临中央工房\n',
            '的维修窗口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450258V在找什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450259V#1015F#4P嗯，在找东西的\n',
            '不是你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450260V找东西的是我……唔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#3160450261V啊，难道\n',
            '各位是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_127E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450262V#050F#1P啊啊，看了公告板才来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AE')

    def _loc_127E(): pass

    label('loc_127E')

    ChrTalk(
        0x0103,
        (
            '#0030450263V#020F#1P嗯嗯，看了公告板来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AE(): pass

    label('loc_12AE')

    ChrTalk(
        0x0008,
        (
            '#3160450264V得、得救了。\n',
            '其实是碰到点难事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450265V总之能听我说说吗？',
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
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13B0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450266V#1006F#4P嗯，好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450267V事不宜迟，\n',
            '好像在找什么是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x04)
    Call(1, 0x0007)

    Jump('loc_146B')

    def _loc_13B0(): pass

    label('loc_13B0')

    ChrTalk(
        0x0101,
        (
            '#0010450268V#1007F#4P啊，抱歉。\n',
            '现在有点忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450269V有时间的时候\n',
            '再来接受委托吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450270V啊，是这样吗？\n',
            '我倒是无所谓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450271V那么，稍后\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x01, 0x8000)
    EventEnd(0x00)

    def _loc_146B(): pass

    label('loc_146B')

    Return()

# id: 0x0006 offset: 0x146C
@scena.Code('func_06_146C')
def func_06_146C():
    EventBegin(0x00)
    Call(1, 0x000E)

    ChrTalk(
        0x0008,
        (
            '#3160450272V啊，各位。\n',
            '辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450273V那个，关于工作，\n',
            '现在有时间了吗？',
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
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_157B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450274V#1006F#4P嗯，没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450267V事不宜迟，\n',
            '好像在找什么是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x04)
    Call(1, 0x0007)

    Jump('loc_160D')

    def _loc_157B(): pass

    label('loc_157B')

    ChrTalk(
        0x0101,
        (
            '#0010450276V#1007F#4P抱、抱歉……\n',
            '其实还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450277V嗯～真忙啊。\n',
            '唉，没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450278V那么，如果有空闲了\n',
            '再请马上来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_160D(): pass

    label('loc_160D')

    Return()

# id: 0x0007 offset: 0x160E
@scena.Code('func_07_160E')
def func_07_160E():
    EventBegin(0x00)

    ChrTalk(
        0x0008,
        (
            '#3160450279V嗯嗯，我在找导力器用的\n',
            '小零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450280V地震后检查了\n',
            '各设施的备用品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450281V似乎是那时候从口袋的洞里\n',
            '全部漏掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010450282V#1004F#4P口袋上有洞？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450283V#1016F哎呀～\n',
            '那不丢才怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450284V是，是……\n',
            '完全是我的失误。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450285V虽然早就知道\n',
            '磨破了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450286V地震的时候一慌，\n',
            '想也没想就塞口袋里了。',
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
        'loc_180D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080450287V#070F然后走来走去\n',
            '就从洞口掉了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080450288V原来如此，事情明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DC')

    def _loc_180D(): pass

    label('loc_180D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1876',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450289V#040F然后走来走去\n',
            '就从洞口掉了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450290V原来如此，事情明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DC')

    def _loc_1876(): pass

    label('loc_1876')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18DC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450291V#030F然后走来走去\n',
            '就从洞口掉了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450292V原来如此，事情明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18DC(): pass

    label('loc_18DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_191F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450293V#050F#1P寻找那个零件\n',
            '就是这次的委托吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1958')

    def _loc_191F(): pass

    label('loc_191F')

    ChrTalk(
        0x0103,
        (
            '#0030450294V#020F#1P寻找那个零件\n',
            '就是这次的委托吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1958(): pass

    label('loc_1958')

    ChrTalk(
        0x0008,
        (
            '#3160450295V是，没错。',
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
        'loc_19FC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450296V#043F不过，导力器的零件\n',
            '一般来说都很细小吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450297V要找出来\n',
            '估计很麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B03')

    def _loc_19FC(): pass

    label('loc_19FC')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A82',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450298V#032F不过，导力器的零件\n',
            '好像都很细小吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450299V要找出来\n',
            '估计会很麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x104, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x104, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B03')

    def _loc_1A82(): pass

    label('loc_1A82')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B03',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450300V#063F不过，导力器的零件\n',
            '是很细小的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450301V要找出来\n',
            '估计会很麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x107, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x107, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B03(): pass

    label('loc_1B03')

    @scena.Lambda('lambda_1B09')
    def lambda_1B09():
        ChrTurnDirection(0x00F7, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1B09)

    @scena.Lambda('lambda_1B17')
    def lambda_1B17():
        ChrTurnDirection(0x00F8, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1B17)

    @scena.Lambda('lambda_1B25')
    def lambda_1B25():
        ChrTurnDirection(0x00F9, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1B25)

    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450302V#1015F#4P这么一说……\n',
            '确、确实很麻烦的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450303V嗯嗯，我也这么想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450304V不过请放心，\n',
            '这次有秘密武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BCD')
    def lambda_1BCD():
        OP_8C(0x00F7, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1BCD)

    @scena.Lambda('lambda_1BDB')
    def lambda_1BDB():
        OP_8C(0x00F8, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1BDB)

    @scena.Lambda('lambda_1BE9')
    def lambda_1BE9():
        OP_8C(0x00F9, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1BE9)

    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450305V#1011F#4P秘密武器……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450306V请使用这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['合金探测器']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['合金探测器'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010450307V#1004F#4P这是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450308V嗯，是我开发的\n',
            '材料可选金属探测器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450309V这个探测器啊……\n',
            '能选择需要探知的金属种类。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450310V也就是只选择特定的材质\n',
            '并且找出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450311V#1015F#4P好、好像很厉害……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450312V#1000F不过这和这次的工作有关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450313V当然，关系大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E53',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450314V#060F大概是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450315V把零件所使用的特定金属\n',
            '设定为探知目标……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x107, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x107, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F52')

    def _loc_1E53(): pass

    label('loc_1E53')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ED4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450316V#030F恐怕是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450317V把零件所使用的特定金属\n',
            '设定为探知目标……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x104, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x104, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1F52')

    def _loc_1ED4(): pass

    label('loc_1ED4')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F52',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450318V#040F大概是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450319V把零件所使用的特定金属\n',
            '设定为探知目标……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0014,
        0x01,
        (
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x03,
        (
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1F52(): pass

    label('loc_1F52')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FCD',
    )

    @scena.Lambda('lambda_1F66')
    def lambda_1F66():
        ChrTurnDirection(0x00F7, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1F66)

    @scena.Lambda('lambda_1F74')
    def lambda_1F74():
        ChrTurnDirection(0x0108, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1F74)

    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0108,
        (
            '#0080450320V#070F唔，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080450321V只对零件作出反应吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A7')

    def _loc_1FCD(): pass

    label('loc_1FCD')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_202D',
    )

    @scena.Lambda('lambda_1FE1')
    def lambda_1FE1():
        ChrTurnDirection(0x00F7, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1FE1)

    @scena.Lambda('lambda_1FEF')
    def lambda_1FEF():
        ChrTurnDirection(0x0105, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1FEF)

    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0105,
        (
            '#0060450322V#040F只对零件\n',
            '作出反应吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A7')

    def _loc_202D(): pass

    label('loc_202D')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A7',
    )

    @scena.Lambda('lambda_2041')
    def lambda_2041():
        ChrTurnDirection(0x00F7, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2041)

    @scena.Lambda('lambda_204F')
    def lambda_204F():
        ChrTurnDirection(0x0104, 0x0014, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_204F)

    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0104,
        (
            '#0040450323V#030F唔，原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450324V只对零件作出反应吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20A7(): pass

    label('loc_20A7')

    ChrTalk(
        0x0101,
        (
            '#0010450325V#1018F#4P啊，对哦。\n',
            '确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450326V嗯嗯，说得太对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450327V接近想调查的地方\n',
            '使用探测器就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450328V如果有零件\n',
            '应该会有反应的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2165')
    def lambda_2165():
        OP_8C(0x00F7, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2165)

    @scena.Lambda('lambda_2173')
    def lambda_2173():
        OP_8C(0x00F9, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2173)

    Sleep(30)

    @scena.Lambda('lambda_2186')
    def lambda_2186():
        OP_8C(0x00F8, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2186)

    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450329V#1006F#4P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2238',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450330V#050F#1P即使可以用这机器，\n',
            '地方还是个问题呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450331V掉落零件的时候，\n',
            '你记得都去哪儿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22AA')

    def _loc_2238(): pass

    label('loc_2238')

    ChrTalk(
        0x0103,
        (
            '#0030450332V#020F#1P即使可以用这机器，\n',
            '地方还是个问题呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450333V掉落零件的时候，\n',
            '你记得都去哪儿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22AA(): pass

    label('loc_22AA')

    ChrTalk(
        0x0008,
        (
            '#3160450334V我去检查的\n',
            '是３层的工作室和４层的实验室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450335V途中的电梯和走廊\n',
            '我已经自己调查过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450336V各位就到研究室中\n',
            '集中性地找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23B1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450337V#050F#1P３层的工作室和４层的实验室吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450338V……好，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2407')

    def _loc_23B1(): pass

    label('loc_23B1')

    ChrTalk(
        0x0103,
        (
            '#0030450339V#020F#1P３层的工作室和４层的实验室对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450340V嗯嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2407(): pass

    label('loc_2407')

    ChrTalk(
        0x0008,
        (
            '#3160450341V大概还有８个左右的\n',
            '零件丢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450342V至少找到一半\n',
            '我的工作也好办多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450343V#1000F#4P嗯，我们会努力看看的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450344V如果发现了零件\n',
            '再返回这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450345V嗯嗯，麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450346V那个时候探测器\n',
            '也请一起归还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2561',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450347V#050F#1P还有其他情报吗？\n',
            '没有我们就走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259E')

    def _loc_2561(): pass

    label('loc_2561')

    ChrTalk(
        0x0103,
        (
            '#0030450348V#027F#1P还有其他情报吗？\n',
            '没有我们就走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_259E(): pass

    label('loc_259E')

    ChrTalk(
        0x0008,
        (
            '#3160450349V啊，那么再说一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450350V４层的实验室\n',
            '请特别仔细调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450351V在那里和安东尼\n',
            '一起玩过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450352V零件一定也\n',
            '丢了很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450353V#1011F#4P安东尼是……\n',
            '住在工房里的猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450354V嗯嗯，就是那只安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450355V虽然很可爱，\n',
            '但这次可真有点冤哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450356V唉，虽然完全是迁怒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450357V#1016F#4P啊哈哈，确实\n',
            '安东尼有点可怜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2771',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450358V#053F#1P好，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_279B')

    def _loc_2771(): pass

    label('loc_2771')

    ChrTalk(
        0x0103,
        (
            '#0030450359V#020F#1P好了，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_279B(): pass

    label('loc_279B')

    ChrTalk(
        0x0008,
        (
            '#3160450360V那么，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450361V#1006F#4P嗯，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x08)
    OP_28(0x006F, 0x01, 0x0001)
    OP_28(0x006F, 0x01, 0x0002)
    OP_28(0x006F, 0x01, 0x0004)
    OP_A2(0x000C)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x2801
@scena.Code('func_08_2801')
def func_08_2801():
    ChrTalk(
        0x0008,
        (
            '#3160450362V要找到零件的话\n',
            '请去３层的工作室和４层的实验室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450363V到了调查的场所\n',
            '就在那里使用探测器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450364V如果有零件\n',
            '应该会有反应的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450365V那么，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0009 offset: 0x28C5
@scena.Code('func_09_28C5')
def func_09_28C5():
    EventBegin(0x00)
    Call(1, 0x000E)

    ChrTalk(
        0x0008,
        (
            '#3160450388V呀，各位。\n',
            '零件找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_2919',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2919(): pass

    label('loc_2919')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_2932',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2932(): pass

    label('loc_2932')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_294B',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_294B(): pass

    label('loc_294B')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_2964',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2964(): pass

    label('loc_2964')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_297D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_297D(): pass

    label('loc_297D')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_2996',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2996(): pass

    label('loc_2996')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_29AF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_29AF(): pass

    label('loc_29AF')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_29C8',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_29C8(): pass

    label('loc_29C8')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A24',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450389V#1007F#5P嗯～完全没找到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450390V多找找\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2A24(): pass

    label('loc_2A24')

    ChrTalk(
        0x0101,
        (
            '#0010450391V#1015F#4P正在努力……的样子吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450392V总之，\n',
            '报告一下状况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000001, 'loc_2AAF'),
        (0x00000002, 'loc_2ACB'),
        (0x00000003, 'loc_2AE7'),
        (0x00000004, 'loc_2B03'),
        (0x00000005, 'loc_2B1F'),
        (0x00000006, 'loc_2B3B'),
        (0x00000007, 'loc_2B57'),
        (0x00000008, 'loc_2B73'),
        (-1, 'loc_2B8F'),
    )

    def _loc_2AAF(): pass

    label('loc_2AAF')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了１个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2ACB(): pass

    label('loc_2ACB')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了２个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2AE7(): pass

    label('loc_2AE7')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了３个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B03(): pass

    label('loc_2B03')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了４个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B1F(): pass

    label('loc_2B1F')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了５个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B3B(): pass

    label('loc_2B3B')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了６个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B57(): pass

    label('loc_2B57')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了７个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B73(): pass

    label('loc_2B73')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '报告发现了８个零件。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2B8F')

    def _loc_2B8F(): pass

    label('loc_2B8F')

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BA9',
    )

    Return()

    def _loc_2BA9(): pass

    label('loc_2BA9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2F9C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_2D2C',
    )

    ChrTalk(
        0x0008,
        (
            '#3160450393V作为成果\n',
            '我想已经足够了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450394V打算怎么办？\n',
            '还继续搜索吗？',
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
            TXT(0x00, '【结束搜索】\n'),
            TXT(0x01, '【继续搜索】\n'),
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
        'loc_2CBB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450395V#1015F#4P嗯，既然委托人这么说了\n',
            '就搜索到这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_2CBB(): pass

    label('loc_2CBB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D29',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450396V#1006F#4P嗯，再稍微\n',
            '努力看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450397V那么，拜托你们\n',
            '继续搜索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_2D29(): pass

    label('loc_2D29')

    Jump('loc_2F99')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    ChrTalk(
        0x0008,
        (
            '#3160450398V啊，看来\n',
            '找到不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450399V嗯，只要有这些\n',
            '我想就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450400V#1004F#4P哎，但是\n',
            '还有零件没找到哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450401V嗯嗯，虽然是没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450402V嗯，难道\n',
            '你们想继续搜索吗？',
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
            TXT(0x00, '【结束搜索】\n'),
            TXT(0x01, '【继续搜索】\n'),
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
        'loc_2EAB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450395V#1015F#4P嗯，既然委托人这么说了\n',
            '就搜索到这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

    def _loc_2EAB(): pass

    label('loc_2EAB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F99',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450404V#1015F#4P你这样说\n',
            '我们是很高兴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450405V#1000F还是再稍微\n',
            '努力看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450406V原来如此，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450397V那么，拜托你们\n',
            '继续搜索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450408V#1006F#4P嗯，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x01, 0x0800)
    EventEnd(0x00)

    def _loc_2F99(): pass

    label('loc_2F99')

    Jump('loc_3068')

    def _loc_2F9C(): pass

    label('loc_2F9C')

    ChrTalk(
        0x0008,
        (
            '#3160450409V嗯，希望你们\n',
            '搜索顺利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450410V零件的数量\n',
            '还有点不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450411V#1011F#4P啊，果然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450412V#1006F那么，再稍微\n',
            '努力看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450413V嗯嗯，拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    def _loc_3068(): pass

    label('loc_3068')

    Return()

# id: 0x000A offset: 0x3069
@scena.Code('func_0A_3069')
def func_0A_3069():
    EventBegin(0x00)
    Call(1, 0x000E)

    ChrTalk(
        0x0008,
        (
            '#3160450414V哎！？\n',
            '要取消工作吗？',
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
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3494',
    )

    ChrTalk(
        0x0101,
        (
            '#0010450415V#1007F#4P是，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450416V非常抱歉，\n',
            '突然有急事要办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450417V这样啊……\n',
            '那就没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450418V嗯，明白了。\n',
            '我还是自己想想办法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_31C9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450419V#552F#1P啊啊，抱歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31F1')

    def _loc_31C9(): pass

    label('loc_31C9')

    ChrTalk(
        0x0103,
        (
            '#0030450420V#025F#1P嗯嗯，抱歉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31F1(): pass

    label('loc_31F1')

    ChrTalk(
        0x0008,
        (
            '#3160450421V哪里哪里，别在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450422V本来就是我自己不小心，\n',
            '当然该自己收拾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450423V那么，麻烦把找到的零件\n',
            '和探测器交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450424V#1015F#4P啊，对哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['合金探测器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_333B',
    )

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_333B(): pass

    label('loc_333B')

    RemoveItem(ItemTable['合金探测器'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_33C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450425V#050F#1P那么，我们\n',
            '这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450426V今天真是抱歉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3410')

    def _loc_33C1(): pass

    label('loc_33C1')

    ChrTalk(
        0x0103,
        (
            '#0030450427V#020F#1P那么，我们\n',
            '这就告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440842V今天真是对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3410(): pass

    label('loc_3410')

    ChrTalk(
        0x0008,
        (
            '#3160450429V哪里，我才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450430V那么请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450431V#1000F#4P嗯，那么再见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x40)
    OP_28(0x006F, 0x04, 0x80)
    OP_28(0x006F, 0x03, 0x08)
    OP_28(0x006F, 0x01, 0x4000)
    OP_A2(0x000D)

    Jump('loc_34EC')

    def _loc_3494(): pass

    label('loc_3494')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34EC',
    )

    ChrTalk(
        0x0008,
        (
            '#3160450432V呼，别吓人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450433V那么，拜托你们\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34EC(): pass

    label('loc_34EC')

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x34EF
@scena.Code('func_0B_34EF')
def func_0B_34EF():
    ChrTalk(
        0x0008,
        (
            '#3160450434V辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450435V那么零件\n',
            '和探测器就还给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['合金探测器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['合金探测器'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)
    RemoveItem(ItemTable['导力器零件'], 1)

    ChrTalk(
        0x0008,
        (
            '#3160450436V呼，今天真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450437V由于我的疏忽\n',
            '还给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450438V#1006F#4P哪里，别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450439V#1015F不过，这样\n',
            '工作真的没问题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450440V哈哈，别担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450441V有这些零件\n',
            '目前就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3753',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450442V#064F那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450443V#560F那个，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3824')

    def _loc_3753(): pass

    label('loc_3753')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37BB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450444V#047F那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450445V#045F不过，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3824')

    def _loc_37BB(): pass

    label('loc_37BB')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3824',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450446V#035F唔，那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450447V#030F但是，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3824(): pass

    label('loc_3824')

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#3160450448V啊，对，对哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450449V得去找针线包才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450450V#1006F#4P需要帮忙的话\n',
            '请马上联络协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450451V会带上针线\n',
            '立刻来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450452V啊哈哈，真是多谢你们关心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450453V那么，今天真是谢谢了。\n',
            '以后还请多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450454V……针线是另外一回事，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_39A1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450455V#051F#1P啊啊，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39C9')

    def _loc_39A1(): pass

    label('loc_39A1')

    ChrTalk(
        0x0103,
        (
            '#0030450456V#020F#1P嗯嗯，多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39C9(): pass

    label('loc_39C9')

    ChrTalk(
        0x0101,
        (
            '#0010450457V#1018F#4P那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x10)
    OP_28(0x006F, 0x01, 0x1000)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【零件搜索】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x000D)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x3A51
@scena.Code('func_0C_3A51')
def func_0C_3A51():
    ChrTalk(
        0x0008,
        (
            '#3160450458V咦，难道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450459V８，８个零件全都\n',
            '找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450460V#1011F#4P啊，全部找齐了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450461V好、好厉害啊。\n',
            '我本来早就死心了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450462V总、总之先把零件和\n',
            '探测器还给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['合金探测器']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '全部交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['合金探测器'], 1)
    RemoveItem(ItemTable['导力器零件'], 8)

    ChrTalk(
        0x0008,
        (
            '#3160450463V呀～今天真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450464V没想到全部零件\n',
            '都能找回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450465V#1017F#4P嘿嘿，能都找到\n',
            '真是再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450466V这样的话，工作的事情\n',
            '就没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450467V嗯嗯，当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450468V让你们这么费心，\n',
            '我真是过意不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#3160450469V……啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450470V这么说来，\n',
            '那个应该还在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 135, 400)
    OP_8E(0x0008, 10850, 0, -2440, 2000, 0x00)
    OP_8C(0x0008, 90, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0008)
    OP_8C(0x0008, 315, 400)
    OP_8E(0x0008, 8650, 0, -1430, 2000, 0x00)
    OP_8C(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#3160450471V请收下这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450472V虽然是微薄之物，\n',
            '就当是我的一点谢礼吧。',
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
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['预警之铃']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['预警之铃'], 1)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010450473V#1001F#4P哇，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3E96',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450474V#052F#1P可以收下它吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBE')

    def _loc_3E96(): pass

    label('loc_3E96')

    ChrTalk(
        0x0103,
        (
            '#0030450475V#023F#1P可以给我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EBE(): pass

    label('loc_3EBE')

    ChrTalk(
        0x0008,
        (
            '#3160450476V嗯嗯，别介意。\n',
            '只是我的一点心意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450477V不管怎样，大家\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450478V有各位，延迟的工作\n',
            '也总算能挽回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FC1',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450442V#064F那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450480V#560F那个，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4092')

    def _loc_3FC1(): pass

    label('loc_3FC1')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4029',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450444V#047F那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450445V#045F不过，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4092')

    def _loc_4029(): pass

    label('loc_4029')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4092',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450446V#035F唔，那就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450447V#030F但是，口袋上的洞\n',
            '最好是早点缝上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4092(): pass

    label('loc_4092')

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#3160450448V啊，对，对哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450449V得去找针线包才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010450450V#1006F#4P需要帮忙的话\n',
            '请马上联络协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450451V会带上针线\n',
            '立刻来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450452V啊哈哈，真是多谢你们关心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450490V那么，要是再有什么事\n',
            '我再联络协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3160450454V……针线是另外一回事，嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4209',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450492V#050F#1P啊啊，多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4231')

    def _loc_4209(): pass

    label('loc_4209')

    ChrTalk(
        0x0103,
        (
            '#0030450456V#020F#1P嗯嗯，多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4231(): pass

    label('loc_4231')

    ChrTalk(
        0x0101,
        (
            '#0010450457V#1018F#4P那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x006F, 0x04, 0x10)
    OP_28(0x006F, 0x01, 0x2000)
    OP_2B(0x006F, 0x0001)
    OP_2C(0x006F, 0x03E8)
    OP_22(0x0017, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【零件搜索】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x000D)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x42C3
@scena.Code('func_0D_42C3')
def func_0D_42C3():
    OP_A1(0x0013, 0x0019)
    SetChrPos(0x0013, -95360, -3200, -109100, 14)
    OP_72(0x0019, 0x0004)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0013, 0x0004)

    @scena.Lambda('lambda_42EE')
    def lambda_42EE():
        OP_8F(0x00FE, -109820, -3200, -109100, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_42EE)

    Sleep(2500)

    OP_A2(0x0011)
    WaitForThreadExit(0x0013, 0x0001)
    OP_75(0xFF, 0x00000016, 0x05)
    OP_23(0x00A0)

    Return()

# id: 0x000E offset: 0x431B
@scena.Code('func_0E_431B')
def func_0E_431B():
    Fade(1000)
    SetChrPos(0x0008, 8650, 0, -1430, 270)
    SetChrPos(0x0101, 6570, 0, -1750, 90)
    SetChrPos(0x00F7, 6440, 0, -780, 90)
    SetChrPos(0x00F8, 5430, 0, -1590, 90)
    SetChrPos(0x00F9, 5190, 0, -570, 90)
    OP_6D(7540, 0, -1430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
