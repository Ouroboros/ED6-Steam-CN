import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3119_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3119_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3119.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1055
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_22C',
    )

    SetChrFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_198',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181057V#010F刚才已经问过话了，\n',
            '可是安东尼一点反应也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181058V我们在工房里面再调查一下吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181059V照米妮亚姆医生说的，\n',
            '在某个地方也许会有线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181060V#003F唔……也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223')

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AE',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_1B5')

    def _loc_1AE(): pass

    label('loc_1AE')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_1B5(): pass

    label('loc_1B5')

    ChrTalk(
        0x0102,
        (
            '#0020181057V#010F刚才已经问过话了，\n',
            '安东尼一点反应也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181067V我们还是去二楼\n',
            '工房长的房间调查看看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_223(): pass

    label('loc_223')

    TalkEnd(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)

    Return()

    def _loc_22C(): pass

    label('loc_22C')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_693',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_287',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#1960181045V哦，怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181046V我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

    def _loc_287(): pass

    label('loc_287')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    SetChrPos(0x0101, 450, 0, 9220, 358)
    SetChrPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E0',
    )

    SetChrPos(0x0107, 1160, 0, 8750, 357)

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FF',
    )

    SetChrPos(0x0106, -720, 0, 8630, 37)

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31E',
    )

    SetChrPos(0x013C, -590, 0, 9610, 42)

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_338',
    )

    @scena.Lambda('lambda_0330')
    def lambda_0330():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0330)

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_352',
    )

    @scena.Lambda('lambda_034A')
    def lambda_034A():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_034A)

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_36C',
    )

    @scena.Lambda('lambda_0364')
    def lambda_0364():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0364)

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_386',
    )

    @scena.Lambda('lambda_037E')
    def lambda_037E():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_037E)

    def _loc_386(): pass

    label('loc_386')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3A0',
    )

    @scena.Lambda('lambda_0398')
    def lambda_0398():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0398)

    def _loc_3A0(): pass

    label('loc_3A0')

    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181006V哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181007V你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181008V#000F啊，嗯。\n',
            '虽说已经找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181009V但是还需要找另外一件东西。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181010V另外一件东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181011V#010F嗯，\n',
            '我们还要寻找被人从医务室里\n',
            '拿出来的烟草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181012V哦哦……\n',
            '是这件事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181013V哎呀～\n',
            '你们也真是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181014V#010F特莱斯主任您今天去过医务室吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181015V没有，没有去过。\n',
            '我今天一直都在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181016V如果不相信的话，\n',
            '可以对这间屋子进行搜查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181017V#505F唔唔～\n',
            '好像没什么可怀疑的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181018V#017F是啊，白忙一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181019V怎么样？我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181020V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181021V可以的话，\n',
            '今后还要请您协助调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181022V啊，当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0020)

    Jump('loc_1047')

    def _loc_693(): pass

    label('loc_693')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_97D',
    )

    EventBegin(0x00)
    OP_4A(0x00FE, 255)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    SetChrPos(0x0101, 450, 0, 9220, 358)
    SetChrPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6FB',
    )

    SetChrPos(0x0107, 1160, 0, 8750, 357)

    def _loc_6FB(): pass

    label('loc_6FB')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71A',
    )

    SetChrPos(0x0106, -720, 0, 8630, 37)

    def _loc_71A(): pass

    label('loc_71A')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_739',
    )

    SetChrPos(0x013C, -590, 0, 9610, 42)

    def _loc_739(): pass

    label('loc_739')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_753',
    )

    @scena.Lambda('lambda_074B')
    def lambda_074B():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_074B)

    def _loc_753(): pass

    label('loc_753')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_76D',
    )

    @scena.Lambda('lambda_0765')
    def lambda_0765():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0765)

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_787',
    )

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_077F)

    def _loc_787(): pass

    label('loc_787')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7A1',
    )

    @scena.Lambda('lambda_0799')
    def lambda_0799():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0799)

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7BB',
    )

    @scena.Lambda('lambda_07B3')
    def lambda_07B3():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_07B3)

    def _loc_7BB(): pass

    label('loc_7BB')

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181045V哦，怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181046V我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181049V#000F不好意思。\n',
            '很快就会结束的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0830)

    @scena.Lambda('lambda_083E')
    def lambda_083E():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_083E)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181038V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x013C, 0x0101, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181039V………………喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181040V#063F没有反应呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181053V#010F抱歉打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181054V谢谢您配合我们工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08FF')
    def lambda_08FF():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_08FF)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181055V#000F那么再见了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1960181056V到、到底怎么回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0040)

    Jump('loc_E93')

    def _loc_97D(): pass

    label('loc_97D')

    EventBegin(0x00)
    OP_4A(0x00FE, 255)
    Fade(1000)
    CameraMove(400, 0, 9640, 0)
    SetChrPos(0x0101, 450, 0, 9220, 358)
    SetChrPos(0x0102, 1650, 0, 9460, 322)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9DA',
    )

    SetChrPos(0x0107, 1160, 0, 8750, 357)

    def _loc_9DA(): pass

    label('loc_9DA')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F9',
    )

    SetChrPos(0x0106, -720, 0, 8630, 37)

    def _loc_9F9(): pass

    label('loc_9F9')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A18',
    )

    SetChrPos(0x013C, -590, 0, 9610, 42)

    def _loc_A18(): pass

    label('loc_A18')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A32',
    )

    @scena.Lambda('lambda_0A2A')
    def lambda_0A2A():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A2A)

    def _loc_A32(): pass

    label('loc_A32')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A4C',
    )

    @scena.Lambda('lambda_0A44')
    def lambda_0A44():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0A44)

    def _loc_A4C(): pass

    label('loc_A4C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A66',
    )

    @scena.Lambda('lambda_0A5E')
    def lambda_0A5E():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0A5E)

    def _loc_A66(): pass

    label('loc_A66')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A80',
    )

    @scena.Lambda('lambda_0A78')
    def lambda_0A78():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0A78)

    def _loc_A80(): pass

    label('loc_A80')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_A9A',
    )

    @scena.Lambda('lambda_0A92')
    def lambda_0A92():
        ChrTurnDirection(0x0004, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_0A92)

    def _loc_A9A(): pass

    label('loc_A9A')

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1960181006V哟，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181007V你们要找的东西找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181008V#000F啊，嗯。\n',
            '虽说已经找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181009V但是还需要找另外一件东西。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181010V另外一件东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181011V#010F嗯，\n',
            '我们还要寻找被人从医务室里\n',
            '拿出来的烟草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181012V哦哦……\n',
            '是这件事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181013V哎呀～\n',
            '你们也真是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181014V#010F特莱斯主任您今天去过医务室吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181015V没有，没有去过。\n',
            '我今天一直都在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181016V如果不相信的话，\n',
            '可以对这间屋子进行搜查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181017V#505F唔唔～\n',
            '好像没什么可怀疑的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181018V#017F是啊，白忙一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1960181019V怎么样？我的嫌疑洗清了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181037V#004F啊，对了。\n',
            '安东尼，如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D2C')
    def lambda_0D2C():
        ChrTurnDirection(0x0102, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D2C)

    @scena.Lambda('lambda_0D3A')
    def lambda_0D3A():
        ChrTurnDirection(0x0107, 0x013C, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0D3A)

    ChrTurnDirection(0x0101, 0x013C, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181038V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x013C, 0x0101, 400)

    ChrTalk(
        0x013C,
        (
            '#2030181039V………………喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181040V#063F没有反应呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181041V#000F哎呀，\n',
            '这么说来果真是预料落空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181020V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181021V可以的话，\n',
            '今后还要请您协助调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E50')
    def lambda_0E50():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0E50)

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '#1960181022V啊，当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 400)
    OP_4B(0x00FE, 255)
    OP_28(0x002C, 0x01, 0x0020)
    OP_28(0x002C, 0x01, 0x0040)
    def _loc_E93(): pass

    label('loc_E93')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_1047',
    )

    @scena.Lambda('lambda_0EA4')
    def lambda_0EA4():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0EA4)

    ChrTurnDirection(0x0101, 0x0102, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_F63',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181068V#505F唔～对两个人都没有反应呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181069V还是去刚才安东尼\n',
            '有反应的地方调查一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181070V#010F是二楼工房长的房间对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181071V我们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1041')

    def _loc_F63(): pass

    label('loc_F63')

    ChrTalk(
        0x0101,
        (
            '#0010181061V#505F唔～\n',
            '对两个人都没有反应呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181062V#013F也就是说没有线索了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181063V#010F我们到工房里面再调查一下吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181059V照米妮亚姆医生说的，\n',
            '在某个地方也许会有线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181060V#003F唔……也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1041(): pass

    label('loc_1041')

    OP_28(0x002C, 0x01, 0x0080)

    def _loc_1047(): pass

    label('loc_1047')

    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
